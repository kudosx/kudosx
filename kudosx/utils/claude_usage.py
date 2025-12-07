#!/usr/bin/env python3
"""Calculate Claude Code CLI usage from session files."""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict
from typing import Literal


def _create_unique_hash(data: dict) -> str | None:
    """Create a unique hash for deduplication using message.id and requestId.

    Returns None if either field is missing (entry won't be deduplicated).
    """
    msg = data.get("message", {})
    message_id = msg.get("id")
    request_id = data.get("requestId")

    if message_id is None or request_id is None:
        return None

    return f"{message_id}:{request_id}"


def _parse_timestamp_to_local_date(timestamp_str: str) -> str | None:
    """Parse ISO timestamp and convert to local date string (YYYY-MM-DD).

    Uses system local timezone for date grouping (matching ccusage behavior).
    """
    if not timestamp_str:
        return None

    try:
        # Parse ISO format (handles both 'Z' suffix and +00:00)
        if timestamp_str.endswith("Z"):
            dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        else:
            dt = datetime.fromisoformat(timestamp_str)

        # Convert to local timezone
        local_dt = dt.astimezone()
        return local_dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return None

# Claude API pricing per 1M tokens (USD) - from LiteLLM
# https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
MODEL_PRICING = {
    "opus-4-5": {"input": 5.0, "output": 25.0, "cache_create": 6.25, "cache_read": 0.50},
    "sonnet-4-5": {"input": 3.0, "output": 15.0, "cache_create": 3.75, "cache_read": 0.30},
    "haiku-4-5": {"input": 1.0, "output": 5.0, "cache_create": 1.25, "cache_read": 0.10},
}
DEFAULT_PRICING = {"input": 3.0, "output": 15.0, "cache_create": 3.75, "cache_read": 0.30}

UsagePeriod = Literal["daily", "weekly", "monthly"]


def get_claude_usage(projects_dir: Path = None) -> dict:
    """Parse all Claude Code session files and calculate token usage.

    Features:
    - Deduplication using message.id + requestId (matching ccusage behavior)
    - Local timezone for date grouping (matching ccusage behavior)
    """
    if projects_dir is None:
        projects_dir = Path.home() / ".claude" / "projects"

    usage = {
        "total_input_tokens": 0,
        "total_output_tokens": 0,
        "cache_creation_tokens": 0,
        "cache_read_tokens": 0,
        "sessions": 0,
        "messages": 0,
        "duplicates_skipped": 0,
        "by_model": defaultdict(lambda: {"input": 0, "output": 0}),
        "by_date": defaultdict(lambda: {
            "input": 0,
            "output": 0,
            "cache_create": 0,
            "cache_read": 0,
            "models": set(),
            "by_model": defaultdict(lambda: {
                "input": 0,
                "output": 0,
                "cache_create": 0,
                "cache_read": 0,
            }),
        }),
    }

    # Track processed entries for deduplication
    processed_hashes: set[str] = set()

    for project_dir in projects_dir.iterdir():
        if not project_dir.is_dir():
            continue

        for session_file in project_dir.glob("*.jsonl"):
            usage["sessions"] += 1

            try:
                with open(session_file, "r") as f:
                    for line in f:
                        if not line.strip():
                            continue

                        try:
                            data = json.loads(line)
                        except json.JSONDecodeError:
                            continue

                        # Validate required fields (matching ccusage schema)
                        msg = data.get("message")
                        if not isinstance(msg, dict):
                            continue

                        msg_usage = msg.get("usage")
                        if not isinstance(msg_usage, dict):
                            continue

                        # Require both input_tokens and output_tokens
                        input_tokens = msg_usage.get("input_tokens")
                        output_tokens = msg_usage.get("output_tokens")
                        if not isinstance(input_tokens, (int, float)):
                            continue
                        if not isinstance(output_tokens, (int, float)):
                            continue

                        # Deduplication: skip if we've seen this message+request combo
                        unique_hash = _create_unique_hash(data)
                        if unique_hash is not None:
                            if unique_hash in processed_hashes:
                                usage["duplicates_skipped"] += 1
                                continue
                            processed_hashes.add(unique_hash)

                        # Convert tokens to int
                        input_tokens = int(input_tokens)
                        output_tokens = int(output_tokens)
                        cache_creation = int(msg_usage.get("cache_creation_input_tokens", 0) or 0)
                        cache_read = int(msg_usage.get("cache_read_input_tokens", 0) or 0)

                        usage["messages"] += 1
                        usage["total_input_tokens"] += input_tokens
                        usage["total_output_tokens"] += output_tokens
                        usage["cache_creation_tokens"] += cache_creation
                        usage["cache_read_tokens"] += cache_read

                        # Track by model (skip synthetic)
                        model = msg.get("model", "unknown")
                        if model and model != "<synthetic>":
                            usage["by_model"][model]["input"] += input_tokens
                            usage["by_model"][model]["output"] += output_tokens

                        # Track by date using LOCAL timezone
                        timestamp = data.get("timestamp", "")
                        date = _parse_timestamp_to_local_date(timestamp)
                        if date:
                            usage["by_date"][date]["input"] += input_tokens
                            usage["by_date"][date]["output"] += output_tokens
                            usage["by_date"][date]["cache_create"] += cache_creation
                            usage["by_date"][date]["cache_read"] += cache_read
                            # Normalize model name (skip synthetic models)
                            model_short = normalize_model_name(model)
                            if model_short:
                                usage["by_date"][date]["models"].add(model_short)
                                # Track per-model tokens for accurate cost calculation
                                usage["by_date"][date]["by_model"][model_short]["input"] += input_tokens
                                usage["by_date"][date]["by_model"][model_short]["output"] += output_tokens
                                usage["by_date"][date]["by_model"][model_short]["cache_create"] += cache_creation
                                usage["by_date"][date]["by_model"][model_short]["cache_read"] += cache_read

            except Exception as e:
                print(f"Error reading {session_file}: {e}")

    return usage


def normalize_model_name(model: str) -> str | None:
    """Normalize model name to short form.

    Returns None for synthetic/unknown models that should be skipped.
    """
    if not model or model == "<synthetic>":
        return None
    if "opus" in model.lower():
        return "opus-4-5"
    elif "sonnet" in model.lower():
        return "sonnet-4-5"
    elif "haiku" in model.lower():
        return "haiku-4-5"
    return model


def format_tokens(tokens: int) -> str:
    """Format token count with K/M suffix."""
    if tokens >= 1_000_000:
        return f"{tokens / 1_000_000:.2f}M"
    elif tokens >= 1_000:
        return f"{tokens / 1_000:.1f}K"
    return str(tokens)


def format_number(n: int, max_width: int = 10) -> str:
    """Format number with thousand separator, truncate if needed."""
    formatted = f"{n:,}"
    if len(formatted) > max_width:
        return formatted[:max_width - 1] + "…"
    return formatted


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    cache_create: int,
    cache_read: int,
    models: set[str] | None = None,
    by_model: dict | None = None,
) -> float:
    """Calculate cost in USD based on token usage.

    If by_model is provided, calculates cost per-model for accuracy.
    Otherwise uses average pricing if multiple models, or specific model pricing if single.
    """
    # If we have per-model breakdown, calculate cost for each model separately
    if by_model:
        total_cost = 0.0
        for model_name, tokens in by_model.items():
            pricing = MODEL_PRICING.get(model_name, DEFAULT_PRICING)
            model_cost = (
                (tokens["input"] / 1_000_000) * pricing["input"]
                + (tokens["output"] / 1_000_000) * pricing["output"]
                + (tokens["cache_create"] / 1_000_000) * pricing["cache_create"]
                + (tokens["cache_read"] / 1_000_000) * pricing["cache_read"]
            )
            total_cost += model_cost
        return total_cost

    # Fallback: use single model pricing or default
    if models and len(models) == 1:
        model = next(iter(models))
        pricing = MODEL_PRICING.get(model, DEFAULT_PRICING)
    else:
        pricing = DEFAULT_PRICING

    cost = (
        (input_tokens / 1_000_000) * pricing["input"]
        + (output_tokens / 1_000_000) * pricing["output"]
        + (cache_create / 1_000_000) * pricing["cache_create"]
        + (cache_read / 1_000_000) * pricing["cache_read"]
    )
    return cost


def get_week_key(date_str: str) -> str:
    """Get ISO week key (YYYY-WNN) from date string."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    iso_cal = dt.isocalendar()
    return f"{iso_cal[0]}-W{iso_cal[1]:02d}"


def get_week_range(week_key: str) -> str:
    """Get date range string for a week key."""
    year, week = week_key.split("-W")
    # Get first day of the week (Monday)
    first_day = datetime.strptime(f"{year}-W{week}-1", "%Y-W%W-%w")
    last_day = first_day + timedelta(days=6)
    return f"{first_day.strftime('%m-%d')} - {last_day.strftime('%m-%d')}"


def get_current_keys() -> dict:
    """Get current date, week, and month keys."""
    today = datetime.now()
    iso_cal = today.isocalendar()
    return {
        "daily": today.strftime("%Y-%m-%d"),
        "weekly": f"{iso_cal[0]}-W{iso_cal[1]:02d}",
        "monthly": today.strftime("%Y-%m"),
    }


def aggregate_usage(usage_data: dict, period: UsagePeriod) -> list[dict]:
    """Aggregate usage data by period."""
    by_date = usage_data.get("by_date", {})
    current_keys = get_current_keys()

    if period == "daily":
        result = []
        for date_str in sorted(by_date.keys()):
            data = by_date[date_str]
            models = sorted(data.get("models", set()))
            total = data["input"] + data["output"] + data["cache_create"] + data["cache_read"]
            # Use per-model breakdown for accurate cost calculation
            by_model_data = dict(data.get("by_model", {}))
            cost = calculate_cost(
                data["input"], data["output"],
                data["cache_create"], data["cache_read"],
                data.get("models"),
                by_model=by_model_data if by_model_data else None,
            )
            result.append({
                "date": date_str,
                "date_display": date_str[5:],  # MM-DD
                "models": models,
                "input_tokens": data["input"],
                "output_tokens": data["output"],
                "cache_create": data["cache_create"],
                "cache_read": data["cache_read"],
                "total_tokens": total,
                "cost": cost,
                "is_current": date_str == current_keys["daily"],
            })
        return result

    elif period == "weekly":
        by_week = defaultdict(lambda: {
            "input": 0, "output": 0, "cache_create": 0, "cache_read": 0,
            "models": set(),
            "by_model": defaultdict(lambda: {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}),
        })
        for date_str, data in by_date.items():
            week_key = get_week_key(date_str)
            by_week[week_key]["input"] += data["input"]
            by_week[week_key]["output"] += data["output"]
            by_week[week_key]["cache_create"] += data["cache_create"]
            by_week[week_key]["cache_read"] += data["cache_read"]
            by_week[week_key]["models"].update(data.get("models", set()))
            # Aggregate per-model data
            for model_name, model_tokens in data.get("by_model", {}).items():
                by_week[week_key]["by_model"][model_name]["input"] += model_tokens["input"]
                by_week[week_key]["by_model"][model_name]["output"] += model_tokens["output"]
                by_week[week_key]["by_model"][model_name]["cache_create"] += model_tokens["cache_create"]
                by_week[week_key]["by_model"][model_name]["cache_read"] += model_tokens["cache_read"]

        result = []
        for week_key in sorted(by_week.keys()):
            data = by_week[week_key]
            models = sorted(data["models"])
            total = data["input"] + data["output"] + data["cache_create"] + data["cache_read"]
            by_model_data = dict(data.get("by_model", {}))
            cost = calculate_cost(
                data["input"], data["output"],
                data["cache_create"], data["cache_read"],
                data["models"],
                by_model=by_model_data if by_model_data else None,
            )
            result.append({
                "date": week_key,
                "date_display": week_key,
                "models": models,
                "input_tokens": data["input"],
                "output_tokens": data["output"],
                "cache_create": data["cache_create"],
                "cache_read": data["cache_read"],
                "total_tokens": total,
                "cost": cost,
                "is_current": week_key == current_keys["weekly"],
            })
        return result

    elif period == "monthly":
        by_month = defaultdict(lambda: {
            "input": 0, "output": 0, "cache_create": 0, "cache_read": 0,
            "models": set(),
            "by_model": defaultdict(lambda: {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}),
        })
        for date_str, data in by_date.items():
            month_key = date_str[:7]  # YYYY-MM
            by_month[month_key]["input"] += data["input"]
            by_month[month_key]["output"] += data["output"]
            by_month[month_key]["cache_create"] += data["cache_create"]
            by_month[month_key]["cache_read"] += data["cache_read"]
            by_month[month_key]["models"].update(data.get("models", set()))
            # Aggregate per-model data
            for model_name, model_tokens in data.get("by_model", {}).items():
                by_month[month_key]["by_model"][model_name]["input"] += model_tokens["input"]
                by_month[month_key]["by_model"][model_name]["output"] += model_tokens["output"]
                by_month[month_key]["by_model"][model_name]["cache_create"] += model_tokens["cache_create"]
                by_month[month_key]["by_model"][model_name]["cache_read"] += model_tokens["cache_read"]

        result = []
        for month_key in sorted(by_month.keys()):
            data = by_month[month_key]
            models = sorted(data["models"])
            total = data["input"] + data["output"] + data["cache_create"] + data["cache_read"]
            by_model_data = dict(data.get("by_model", {}))
            cost = calculate_cost(
                data["input"], data["output"],
                data["cache_create"], data["cache_read"],
                data["models"],
                by_model=by_model_data if by_model_data else None,
            )
            result.append({
                "date": month_key,
                "date_display": month_key,
                "models": models,
                "input_tokens": data["input"],
                "output_tokens": data["output"],
                "cache_create": data["cache_create"],
                "cache_read": data["cache_read"],
                "total_tokens": total,
                "cost": cost,
                "is_current": month_key == current_keys["monthly"],
            })
        return result

    return []


def calculate_totals(data: list[dict]) -> dict:
    """Calculate sum totals for all columns."""
    return {
        "input": sum(d["input_tokens"] for d in data),
        "output": sum(d["output_tokens"] for d in data),
        "cache_create": sum(d["cache_create"] for d in data),
        "cache_read": sum(d["cache_read"] for d in data),
        "total": sum(d["total_tokens"] for d in data),
        "cost": sum(d["cost"] for d in data),
    }


def main():
    usage = get_claude_usage()

    print("=" * 50)
    print("Claude Code Usage Summary")
    print("=" * 50)
    print(f"Sessions: {usage['sessions']}")
    print(f"Messages: {usage['messages']}")
    print()
    print("Token Usage:")
    print(f"  Input tokens:  {format_tokens(usage['total_input_tokens'])}")
    print(f"  Output tokens: {format_tokens(usage['total_output_tokens'])}")
    print(f"  Cache created: {format_tokens(usage['cache_creation_tokens'])}")
    print(f"  Cache read:    {format_tokens(usage['cache_read_tokens'])}")
    print()

    print("By Model:")
    for model, tokens in sorted(usage["by_model"].items()):
        print(f"  {model}:")
        print(f"    Input:  {format_tokens(tokens['input'])}")
        print(f"    Output: {format_tokens(tokens['output'])}")
    print()

    print("By Month:")
    # Aggregate by month
    by_month = defaultdict(lambda: {"input": 0, "output": 0})
    for date, tokens in usage["by_date"].items():
        month = date[:7]  # YYYY-MM
        by_month[month]["input"] += tokens["input"]
        by_month[month]["output"] += tokens["output"]

    for month, tokens in sorted(by_month.items(), reverse=True):
        print(f"  {month}: in={format_tokens(tokens['input'])}, out={format_tokens(tokens['output'])}")


if __name__ == "__main__":
    main()
