"""Generates sales_data.csv with 100 synthetic sales order records."""
import csv
import random
from datetime import date, timedelta

random.seed(42)

REGIONS = ["North", "South", "East", "West"]
PRODUCTS = {
    "Wireless Mouse": ("Electronics", 19.99),
    "Mechanical Keyboard": ("Electronics", 59.99),
    "USB-C Hub": ("Electronics", 34.99),
    "Office Chair": ("Furniture", 149.99),
    "Standing Desk": ("Furniture", 299.99),
    "Desk Lamp": ("Furniture", 24.99),
    "Notebook Set": ("Stationery", 8.99),
    "Ballpoint Pens (12pk)": ("Stationery", 5.49),
    "Whiteboard": ("Stationery", 45.00),
    "Bluetooth Speaker": ("Electronics", 39.99),
}
PAYMENT_METHODS = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
FIRST_NAMES = ["Aarav", "Priya", "John", "Emma", "Wei", "Fatima", "Liam", "Sofia", "Noah", "Mia",
               "Arjun", "Olivia", "Ravi", "Isabella", "Ken", "Ana", "Sam", "Zara", "Leo", "Nora"]
LAST_NAMES = ["Sharma", "Smith", "Chen", "Khan", "Patel", "Garcia", "Kim", "Rossi", "Silva", "Nguyen"]

start_date = date(2025, 1, 1)

rows = []
for i in range(1, 101):
    product, (category, unit_price) = random.choice(list(PRODUCTS.items()))
    quantity = random.randint(1, 8)
    total_price = round(unit_price * quantity, 2)
    order_date = start_date + timedelta(days=random.randint(0, 180))
    customer = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    rows.append({
        "order_id": f"ORD-{i:04d}",
        "order_date": order_date.isoformat(),
        "customer_name": customer,
        "region": random.choice(REGIONS),
        "product": product,
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price,
        "payment_method": random.choice(PAYMENT_METHODS),
    })

rows.sort(key=lambda r: r["order_date"])

with open("sales_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} records to sales_data.csv")
