from payments import refund


def handle_refund(request):
    """NEW in this PR: POST /refunds {"payment_id": "...", "amount": "12.50"} (euros, as typed by support staff)."""
    amount = float(request["amount"])
    left = refund(request["payment_id"], amount)
    return {"ok": True, "remaining": left}
