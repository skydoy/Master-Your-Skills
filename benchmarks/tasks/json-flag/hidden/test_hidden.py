import json
import wordcount


def test_json(tmp_path, capsys):
    f = tmp_path / "a.txt"
    f.write_text("hello world\nbye\n", encoding="utf-8")
    wordcount.main([str(f), "--json"])
    assert json.loads(capsys.readouterr().out) == {"lines": 2, "words": 3, "chars": 16}


def test_plain_unchanged(tmp_path, capsys):
    f = tmp_path / "a.txt"
    f.write_text("hello world\nbye\n", encoding="utf-8")
    wordcount.main([str(f)])
    assert capsys.readouterr().out.strip() == "2 3 16"
