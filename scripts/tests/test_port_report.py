import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from port_report import port

FRAGMENT = (
    '<meta charset="utf-8">\n'
    '<title>Example Report</title>\n'
    '<style>.viz-root { color: red; }</style>\n'
    '<div class="viz-root">\n'
    '  <p>hello</p>\n'
    '</div>\n'
)


def test_port_splits_head_and_body():
    result = port(FRAGMENT)
    assert "<title>Example Report</title>" in result
    assert result.index("<head>") < result.index("<title>Example Report</title>") < result.index("</head>")
    assert result.index("</head>") < result.index('<div class="viz-root">')


def test_port_inserts_empty_markers():
    result = port(FRAGMENT)
    assert "<!-- NAV:START -->\n<!-- NAV:END -->" in result
    assert "<!-- FOOTER:START -->\n<!-- FOOTER:END -->" in result


def test_port_preserves_body_content():
    result = port(FRAGMENT)
    assert "<p>hello</p>" in result


def test_port_raises_on_missing_viz_root():
    with pytest.raises(ValueError):
        port("<p>no viz-root div here</p>")
