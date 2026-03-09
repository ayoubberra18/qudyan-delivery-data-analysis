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
