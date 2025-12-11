import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# Total revenue
total_revenue = df["Total"].sum()
print("Total Revenue:", total_revenue)

# Monthly revenue
monthly = df.groupby("Month")["Total"].sum()
print("\nMonthly Revenue:")
print(monthly)

# Top 5 products
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
print("\nTop Selling Products:")
print(top_products)

# Plot monthly trend
plt.figure(figsize=(8, 4))
monthly.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
