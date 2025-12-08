"""Tests for version management utilities."""

import pytest

from kudosx.utils.version import (
    normalize_version,
    parse_version,
    compare_versions,
    is_update_available,
    format_version,
)


class TestNormalizeVersion:
    """Tests for normalize_version function."""

    def test_removes_v_prefix(self):
        """Test v prefix is removed."""
        assert normalize_version("v1.0.0") == "1.0.0"

    def test_handles_no_prefix(self):
        """Test version without v prefix."""
        assert normalize_version("1.0.0") == "1.0.0"

    def test_strips_whitespace(self):
        """Test whitespace is stripped."""
        assert normalize_version("  v1.0.0  ") == "1.0.0"

    def test_returns_none_for_none(self):
        """Test None input returns None."""
        assert normalize_version(None) is None


class TestParseVersion:
    """Tests for parse_version function."""

    def test_parse_semver(self):
        """Test parsing semantic version."""
        assert parse_version("1.2.3") == (1, 2, 3)

    def test_parse_with_v_prefix(self):
        """Test parsing version with v prefix."""
        assert parse_version("v1.2.3") == (1, 2, 3)

    def test_parse_two_parts(self):
        """Test parsing version with two parts."""
        assert parse_version("1.2") == (1, 2)

    def test_parse_one_part(self):
        """Test parsing version with one part."""
        assert parse_version("1") == (1,)

    def test_parse_invalid_returns_default(self):
        """Test parsing invalid version returns default."""
        assert parse_version("") == (0, 0, 0)


class TestCompareVersions:
    """Tests for compare_versions function."""

    def test_installed_older(self):
        """Test installed version is older."""
        assert compare_versions("1.0.0", "1.1.0") == -1
        assert compare_versions("v1.0.0", "v2.0.0") == -1

    def test_installed_same(self):
        """Test versions are equal."""
        assert compare_versions("1.0.0", "1.0.0") == 0
        assert compare_versions("v1.0.0", "1.0.0") == 0

    def test_installed_newer(self):
        """Test installed version is newer."""
        assert compare_versions("2.0.0", "1.0.0") == 1

    def test_patch_version_difference(self):
        """Test patch version comparison."""
        assert compare_versions("1.0.0", "1.0.1") == -1
        assert compare_versions("1.0.2", "1.0.1") == 1

    def test_minor_version_difference(self):
        """Test minor version comparison."""
        assert compare_versions("1.0.0", "1.1.0") == -1
        assert compare_versions("1.2.0", "1.1.0") == 1

    def test_none_installed(self):
        """Test None installed version."""
        assert compare_versions(None, "1.0.0") is None

    def test_none_latest(self):
        """Test None latest version."""
        assert compare_versions("1.0.0", None) is None

    def test_both_none(self):
        """Test both None."""
        assert compare_versions(None, None) is None

    def test_different_length_versions(self):
        """Test versions with different number of parts."""
        assert compare_versions("1.0", "1.0.0") == 0
        assert compare_versions("1.0", "1.0.1") == -1


class TestIsUpdateAvailable:
    """Tests for is_update_available function."""

    def test_update_available(self):
        """Test update is available."""
        assert is_update_available("1.0.0", "1.1.0") is True

    def test_up_to_date(self):
        """Test already up-to-date."""
        assert is_update_available("1.0.0", "1.0.0") is False

    def test_newer_than_latest(self):
        """Test installed is newer than latest."""
        assert is_update_available("2.0.0", "1.0.0") is False

    def test_none_installed(self):
        """Test None installed returns False."""
        assert is_update_available(None, "1.0.0") is False

    def test_none_latest(self):
        """Test None latest returns False."""
        assert is_update_available("1.0.0", None) is False


class TestFormatVersion:
    """Tests for format_version function."""

    def test_format_version(self):
        """Test formatting version."""
        assert format_version("1.0.0") == "1.0.0"
        assert format_version("v1.0.0") == "v1.0.0"

    def test_format_none(self):
        """Test formatting None returns dash."""
        assert format_version(None) == "-"
