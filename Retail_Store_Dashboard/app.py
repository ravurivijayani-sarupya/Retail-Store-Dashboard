import pandas as pd


df = pd.read_csv("Europe Sales Records.csv")
df.head()
total_sales = df["Units Sold"].sum()
total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()

print("Total Sales:", total_sales)
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
best_products = df.groupby("Item Type")["Units Sold"].sum().sort_values(ascending=False)

print(best_products)
!pip install matplotlib
import matplotlib.pyplot as plt

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.month)["Total Revenue"].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
region = df.groupby("Region")["Total Revenue"].sum()

plt.figure(figsize=(8,8))
plt.pie(region.values, labels=region.index, autopct="%1.1f%%")
plt.title("Revenue by Region")
plt.show()
top = df.groupby("Item Type")["Units Sold"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
plt.bar(top.index, top.values)
plt.xticks(rotation=45)
plt.title("Best Selling Products")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.show()
print("="*40)
print("RETAIL STORE DASHBOARD")
print("="*40)

print("Total Sales :", total_sales)
print("Total Revenue :", total_revenue)
print("Total Profit :", total_profit)

print("\nBest Selling Product :")
print(best_products.head(1))