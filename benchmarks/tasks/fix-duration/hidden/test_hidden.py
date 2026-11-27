from duration import parse_duration, format_duration


def test_hours_only():
    assert parse_duration("2h") == 7200


def test_hours_and_seconds():
    assert parse_duration("1h5s") == 3605


def test_minutes_only():
    assert parse_duration("45m") == 2700


def test_full():
    assert parse_duration("1h30m15s") == 5415


def test_roundtrip():
    for s in (0, 59, 3600, 3725, 86399):
        assert parse_duration(format_duration(s)) == s
