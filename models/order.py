from datetime import datetime

from config.db import get_db


def save_order(form_data):
    db = get_db()
    item_ids = form_data.getlist("item_ids")
    items = []
    total_price = 0

    for data in item_ids:
        item_id, item_name, variant_name, unit_price = data.split("|")
        quantity_field = (
            f"quantity_{item_id}"
            if variant_name == "None"
            else f"quantity_{item_id}_{variant_name}"
        )
        quantity = int(form_data.get(quantity_field, 1))
        total_price += float(unit_price) * quantity

        item = {
            "item_id": item_id,
            "name": item_name,
            "variant": variant_name,
            "quantity": quantity,
            "unit_price": float(unit_price),
        }

        if variant_name != "None":
            item["variant"] = variant_name

        items.append(item)

    db.orders.insert_one(
        {"items": items, "total": float(total_price), "timestamp": datetime.now()}
    )
