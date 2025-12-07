#!/usr/bin/env python3
"""Calculate Claude Code CLI usage from session files."""

import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
from typing import Literal

# Claude API pricing per 1M tokens (USD)
MODEL_PRICING = {
    "opus-4-5": {"input": 15.0, "output": 75.0, "cache_create": 18.75, "cache_read": 1.50},
    "sonnet-4-5": {"input": 3.0, "output": 15.0, "cache_create": 3.75, "cache_read": 0.30},
    "haiku-4-5": {"input": 0.80, "output": 4.0, "cache_create": 1.0, "cache_read": 0.08},
}
DEFAULT_PRICING = {"input": 3.0, "output": 15.0, "cache_create": 3.75, "cache_read": 0.30}

UsagePeriod = Literal["daily", "weekly", "monthly"]


def get_claude_usage(projects_dir: Path = None) -> dict:
    """Parse all Claude Code session files and calculate token usage."""

    if projects_dir is None:
        projects_dir = Path.home() / ".claude" / "projects"

    usage = {
        "total_input_tokens": 0,
        "total_output_tokens": 0,
        "cache_creation_tokens": 0,
        "cache_read_tokens": 0,
        "sessions": 0,
        "messages": 0,
        "by_model": defaultdict(lambda: {"input": 0, "output": 0}),
        "by_date": defaultdict(lambda: {
            "input": 0,
            "output": 0,
            "cache_create": 0,
            "cache_read": 0,
            "models": set(),
        }),
    }

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

                        # Extract usage from assistant messages
                        if data.get("type") == "assistant":
                            msg = data.get("message", {})
                            msg_usage = msg.get("usage", {})

                            if msg_usage:
                                usage["messages"] += 1

                                input_tokens = msg_usage.get("input_tokens", 0)
                                output_tokens = msg_usage.get("output_tokens", 0)
                                cache_creation = msg_usage.get("cache_creation_input_tokens", 0)
                                cache_read = msg_usage.get("cache_read_input_tokens", 0)

                                usage["total_input_tokens"] += input_tokens
                                usage["total_output_tokens"] += output_tokens
                                usage["cache_creation_tokens"] += cache_creation
                                usage["cache_read_tokens"] += cache_read

                                # Track by model
                                model = msg.get("model", "unknown")
                                usage["by_model"][model]["input"] += input_tokens
                                usage["by_model"][model]["output"] += output_tokens

                                # Track by date with full details
                                timestamp = data.get("timestamp", "")
                                if timestamp:
                                    date = timestamp[:10]  # YYYY-MM-DD
                                    usage["by_date"][date]["input"] += input_tokens
                                    usage["by_date"][date]["output"] += output_tokens
                                    usage["by_date"][date]["cache_create"] += cache_creation
                                    usage["by_date"][date]["cache_read"] += cache_read
                                    # Normalize model name
                                    model_short = normalize_model_name(model)
                                    usage["by_date"][date]["models"].add(model_short)

            except Exception as e:
                print(f"Error reading {session_file}: {e}")

    return usage


def normalize_model_name(model: str) -> str:
    """Normalize model name to short form."""
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
) -> float:
    """Calculate cost in USD based on token usage.

    Uses average pricing if multiple models, or specific model pricing if single model.
    """
    # Use average of models if multiple, or specific pricing if single
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
            cost = calculate_cost(
                data["input"], data["output"],
                data["cache_create"], data["cache_read"],
                data.get("models"),
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
            "input": 0, "output": 0, "cache_create": 0, "cache_read": 0, "models": set()
        })
        for date_str, data in by_date.items():
            week_key = get_week_key(date_str)
            by_week[week_key]["input"] += data["input"]
            by_week[week_key]["output"] += data["output"]
            by_week[week_key]["cache_create"] += data["cache_create"]
            by_week[week_key]["cache_read"] += data["cache_read"]
            by_week[week_key]["models"].update(data.get("models", set()))

        result = []
        for week_key in sorted(by_week.keys()):
            data = by_week[week_key]
            models = sorted(data["models"])
            total = data["input"] + data["output"] + data["cache_create"] + data["cache_read"]
            cost = calculate_cost(
                data["input"], data["output"],
                data["cache_create"], data["cache_read"],
                data["models"],
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
            "input": 0, "output": 0, "cache_create": 0, "cache_read": 0, "models": set()
        })
        for date_str, data in by_date.items():
            month_key = date_str[:7]  # YYYY-MM
            by_month[month_key]["input"] += data["input"]
            by_month[month_key]["output"] += data["output"]
            by_month[month_key]["cache_create"] += data["cache_create"]
            by_month[month_key]["cache_read"] += data["cache_read"]
            by_month[month_key]["models"].update(data.get("models", set()))

        result = []
        for month_key in sorted(by_month.keys()):
            data = by_month[month_key]
            models = sorted(data["models"])
            total = data["input"] + data["output"] + data["cache_create"] + data["cache_read"]
            cost = calculate_cost(
                data["input"], data["output"],
                data["cache_create"], data["cache_read"],
                data["models"],
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
