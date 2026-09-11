import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build_nav import stamp


def test_stamp_replaces_marker_region():
    html = (
        "<body>\n"
        "<!-- NAV:START -->\n<!-- NAV:END -->\n"
        "<p>content</p>\n"
        "</body>"
    )
    result = stamp(html, "NAV", "<nav>Home</nav>")
    assert "<nav>Home</nav>" in result
    assert "<p>content</p>" in result


def test_stamp_is_idempotent():
    html = "<!-- NAV:START -->\nold\n<!-- NAV:END -->"
    once = stamp(html, "NAV", "<nav>new</nav>")
    twice = stamp(once, "NAV", "<nav>new</nav>")
    assert once == twice
    assert "old" not in once


def test_stamp_leaves_other_markers_alone():
    html = (
        "<!-- NAV:START -->\nnav\n<!-- NAV:END -->\n"
        "<!-- FOOTER:START -->\nfoot\n<!-- FOOTER:END -->"
    )
    result = stamp(html, "NAV", "<nav>new</nav>")
    assert "foot" in result
    assert "<!-- FOOTER:START -->" in result


def test_stamp_returns_unchanged_when_marker_absent():
    html = "<p>no markers here</p>"
    result = stamp(html, "NAV", "<nav>x</nav>")
    assert result == html
