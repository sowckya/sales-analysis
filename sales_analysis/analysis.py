"""Analyzes sales_data.csv and writes summary stats + charts used in report.md."""
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

summary = {}

summary["total_orders"] = len(df)
summary["total_revenue"] = round(df["total_price"].sum(), 2)
summary["average_order_value"] = round(df["total_price"].mean(), 2)
summary["total_units_sold"] = int(df["quantity"].sum())
summary["date_range"] = [df["order_date"].min().date().isoformat(), df["order_date"].max().date().isoformat()]

revenue_by_region = df.groupby("region")["total_price"].sum().round(2).sort_values(ascending=False)
summary["revenue_by_region"] = revenue_by_region.to_dict()

revenue_by_category = df.groupby("category")["total_price"].sum().round(2).sort_values(ascending=False)
summary["revenue_by_category"] = revenue_by_category.to_dict()

top_products = df.groupby("product")["total_price"].sum().round(2).sort_values(ascending=False)
summary["top_products"] = top_products.to_dict()

revenue_by_payment = df.groupby("payment_method")["total_price"].sum().round(2).sort_values(ascending=False)
summary["revenue_by_payment_method"] = revenue_by_payment.to_dict()

revenue_by_month = df.groupby("month")["total_price"].sum().round(2)
summary["revenue_by_month"] = revenue_by_month.to_dict()

top_customers = df.groupby("customer_name")["total_price"].sum().round(2).sort_values(ascending=False).head(5)
summary["top_5_customers"] = top_customers.to_dict()

with open("summary.json", "w") as f:
    json.dump(summary, f, indent=2)

# Charts
revenue_by_month.plot(kind="bar", title="Revenue by Month", ylabel="Revenue ($)", figsize=(8, 4))
plt.tight_layout()
plt.savefig("charts/revenue_by_month.png")
plt.close()

revenue_by_region.plot(kind="bar", title="Revenue by Region", ylabel="Revenue ($)", figsize=(6, 4), color="orange")
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png")
plt.close()

top_products.plot(kind="barh", title="Revenue by Product", xlabel="Revenue ($)", figsize=(8, 5), color="green")
plt.tight_layout()
plt.savefig("charts/revenue_by_product.png")
plt.close()

print(json.dumps(summary, indent=2))
