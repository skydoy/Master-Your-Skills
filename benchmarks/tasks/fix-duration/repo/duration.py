import re

UNITS = {"h": 3600, "m": 60, "s": 1}


def parse_duration(text):
    """Parse strings like '1h30m', '45s', '2h' into seconds."""
    total = 0
    for value, unit in re.findall(r"(\d+)([hms])", text):
        if unit == "h" and "m" in text:
            total += int(value) * UNITS[unit]
        elif unit != "h":
            total += int(value) * UNITS[unit]
    return total


def format_duration(seconds):
    h, rest = divmod(seconds, 3600)
    m, s = divmod(rest, 60)
    return "".join(f"{v}{u}" for v, u in ((h, "h"), (m, "m"), (s, "s")) if v) or "0s"
