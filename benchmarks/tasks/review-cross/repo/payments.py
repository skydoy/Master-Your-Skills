"""Payments. All amounts are integer cents."""
import logging

log = logging.getLogger(__name__)
PAYMENTS = {}  # id -> {"captured": cents, "refunded": cents, "card": str}


def capture(payment_id, cents, card):
    PAYMENTS[payment_id] = {"captured": cents, "refunded": 0, "card": card}


def refund(payment_id, amount):
    """NEW in this PR: refund part of a payment."""
    p = PAYMENTS[payment_id]
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > p["captured"]:
        raise ValueError("cannot refund more than captured")
    p["refunded"] += amount
    log.info("refunded %s on card %s", amount, p["card"][-4:])
    return p["captured"] - p["refunded"]
