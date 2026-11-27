from records import group_by


def test_group():
    rs = [{"t": "a", "v": 1}, {"t": "b", "v": 2}, {"t": "a", "v": 3}]
    assert group_by(rs, "t") == {"a": [rs[0], rs[2]], "b": [rs[1]]}


def test_empty():
    assert group_by([], "t") == {}
