import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("qudyan_orders_portfolio.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

# Total orders
total_orders = len(df)
print("\nTotal Orders:", total_orders)

# Average order amount
avg_order = df["order_amount"].mean()
print("Average Order Amount:", round(avg_order, 2))

# Order status distribution
print("\nOrder Status Distribution:")
print(df["order_status"].value_counts())

# Payment status distribution
print("\nPayment Status Distribution:")
print(df["payment_status"].value_counts())

# Orders by type
print("\nOrder Type Distribution:")
print(df["order_type"].value_counts())

# Orders by delivery date
daily_orders = df.groupby("delivery_date")["order_id"].count()

plt.figure(figsize=(10, 5))
daily_orders.plot()
plt.title("Qudyan Delivery Orders Over Time")
plt.xlabel("Delivery Date")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("qudyan_orders_portfolio.csv")

# Orders by status
status_counts = df["order_status"].value_counts()

plt.figure(figsize=(6,4))
status_counts.plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("order_status_chart.png")

# Payment status
payment_counts = df["payment_status"].value_counts()

plt.figure(figsize=(6,4))
payment_counts.plot(kind="bar")
plt.title("Payment Status Distribution")
plt.xlabel("Payment Status")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("payment_status_chart.png")

# Orders over time
df["created_at"] = pd.to_datetime(df["created_at"])
daily_orders = df.groupby(df["created_at"].dt.date)["order_id"].count()

plt.figure(figsize=(8,4))
daily_orders.plot()
plt.title("Orders Over Time")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("orders_over_time_chart.png")
