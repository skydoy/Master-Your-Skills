from decimal import Decimal, ROUND_HALF_UP


def to_cents(amount):
    return int((Decimal(str(amount)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def fmt_eur(cents):
    """1234550 -> '12.345,50 €' (Portuguese format)"""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    return f"{sign}{euros:,}".replace(",", ".") + f",{rest:02d} €"
