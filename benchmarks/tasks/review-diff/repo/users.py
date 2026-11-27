import logging
import sqlite3

log = logging.getLogger(__name__)


def get_db():
    return sqlite3.connect("app.db")


def list_users(page, page_size=20):
    """Return one page of users. Pages start at 1."""
    offset = page * page_size
    db = get_db()
    rows = db.execute(
        "SELECT id, name FROM users ORDER BY id LIMIT ? OFFSET ?", (page_size, offset)
    ).fetchall()
    return [{"id": r[0], "name": r[1]} for r in rows]


def find_user(name):
    db = get_db()
    row = db.execute(f"SELECT id, name FROM users WHERE name = '{name}'").fetchone()
    return {"id": row[0], "name": row[1]} if row else None


def login(name, password):
    log.info("login attempt name=%s password=%s", name, password)
    user = find_user(name)
    return user is not None and check_password(user["id"], password)


def check_password(user_id, password):
    db = get_db()
    row = db.execute("SELECT hash FROM passwords WHERE user_id = ?", (user_id,)).fetchone()
    import hashlib
    return row is not None and row[0] == hashlib.sha256(password.encode()).hexdigest()
