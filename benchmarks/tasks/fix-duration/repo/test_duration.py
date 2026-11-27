from duration import parse_duration, format_duration


def test_hours_and_minutes():
    assert parse_duration("1h30m") == 5400


def test_format_roundtrip():
    assert format_duration(5400) == "1h30m"
