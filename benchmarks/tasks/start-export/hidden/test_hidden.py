import csv
import report


def rows(tmp_path):
    p = tmp_path / "o.csv"
    report.export_csv(str(p))
    with open(p, newline="") as f:
        return list(csv.reader(f))


def test_header(tmp_path):
    assert rows(tmp_path)[0] == ["region", "total"]


def test_sorted_two_decimals(tmp_path):
    assert rows(tmp_path)[1:4] == [["Norte", "1500.75"], ["Centro", "1500.00"], ["Sul", "1000.00"]]


def test_total_row(tmp_path):
    assert rows(tmp_path)[-1] == ["TOTAL", "4000.75"]


def test_custom_sales(tmp_path):
    p = tmp_path / "c.csv"
    report.export_csv(str(p), sales=[{"region": "X", "amount": 1}])
    assert list(csv.reader(open(p, newline=""))) == [["region", "total"], ["X", "1.00"], ["TOTAL", "1.00"]]
