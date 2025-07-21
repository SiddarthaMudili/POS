from collections import defaultdict
from datetime import datetime

from config.db import get_db


def get_today_orders():
    """Retrieve all orders placed today."""
    db = get_db()
    today = datetime.now().strftime("%Y-%m-%d")
    start = datetime.strptime(today, "%Y-%m-%d")
    end = start.replace(hour=23, minute=59, second=59)

    return list(db.orders.find({"timestamp": {"$gte": start, "$lte": end}}))


def calculate_total_sales(orders):
    """Calculate total sales from a list of orders."""
    return sum(order.get("total", 0) for order in orders)


def get_top_selling_items(orders, top_n=3):
    """Return top N selling items based on quantity sold."""
    item_sales = defaultdict(int)

    for order in orders:
        for item in order["items"]:
            name = item["name"]
            qty = item.get("quantity", 0)
            item_sales[name] += qty

    # Sort items by quantity sold, descending
    sorted_items = sorted(item_sales.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:top_n]


def get_summary():
    """Bundle today's orders, total sales, and top sellers."""
    orders = get_today_orders()
    total_sales = calculate_total_sales(orders)
    top_sellers = get_top_selling_items(orders)

    return {"orders": orders, "total_sales": total_sales, "top_sellers": top_sellers}
