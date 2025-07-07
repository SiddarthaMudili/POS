from datetime import datetime

from config.db import get_db


def get_menu():
    db = get_db()
    return list(db.menu.find({"category_id": {"$ne": "specials"}}))


def get_specials():
    db = get_db()
    day = datetime.now().strftime("%A")
    return list(db.menu.find({"category_id": "specials", "day": day}))

