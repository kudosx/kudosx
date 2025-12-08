"""Version comparison utilities for Kudosx."""

import re


def normalize_version(version: str | None) -> str | None:
    """Normalize version string by removing 'v' prefix.

    Args:
        version: Version string (e.g., "v0.1.0" or "0.1.0")

    Returns:
        Normalized version without 'v' prefix, or None if input is None
    """
    if version is None:
        return None
    return version.strip().lstrip("v").strip()


def parse_version(version: str) -> tuple[int, ...]:
    """Parse version string into tuple of integers.

    Args:
        version: Version string (e.g., "0.1.0" or "v0.1.0")

    Returns:
        Tuple of version parts as integers
    """
    normalized = normalize_version(version)
    if not normalized:
        return (0, 0, 0)
    # Extract numeric parts
    parts = re.findall(r"\d+", normalized)
    return tuple(int(p) for p in parts) if parts else (0, 0, 0)


def compare_versions(installed: str | None, latest: str | None) -> int:
    """Compare two version strings.

    Args:
        installed: Installed version string
        latest: Latest version string

    Returns:
        -1 if installed < latest (update available)
         0 if installed == latest (up to date)
         1 if installed > latest (newer than remote)
        None if comparison not possible
    """
    if installed is None or latest is None:
        return None

    installed_parts = parse_version(installed)
    latest_parts = parse_version(latest)

    # Pad shorter tuple with zeros
    max_len = max(len(installed_parts), len(latest_parts))
    installed_parts = installed_parts + (0,) * (max_len - len(installed_parts))
    latest_parts = latest_parts + (0,) * (max_len - len(latest_parts))

    if installed_parts < latest_parts:
        return -1
    elif installed_parts > latest_parts:
        return 1
    return 0


def is_update_available(installed: str | None, latest: str | None) -> bool:
    """Check if an update is available.

    Args:
        installed: Installed version string
        latest: Latest version string

    Returns:
        True if update is available, False otherwise
    """
    result = compare_versions(installed, latest)
    return result == -1 if result is not None else False


def format_version(version: str | None) -> str:
    """Format version for display.

    Args:
        version: Version string or None

    Returns:
        Formatted version string or "-" if None
    """
    if version is None:
        return "-"
    return version
