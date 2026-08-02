import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Retail Store Dashboard", layout="wide")
st.title("📊 Retail Store Dashboard")

# ==========================
# Load Dataset with Error Handling
# ==========================
try:
    df = pd.read_csv("Europe Sales Records.csv")
except FileNotFoundError:
    st.error("❌ `Europe Sales Records.csv` file dorakaledhu!")
    st.info("GitHub repo lo CSV file upload cheyandi")
    st.stop()

# Date format cheyadam
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ==========================
# KPI Cards
# ==========================
total_sales = df["Units Sold"].sum()
total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()

best_product = df.groupby("Item Type")["Units Sold"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)
col1.metric("🛒 Total Sales", f"{total_sales:,}")
col2.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
col3.metric("📈 Total Profit", f"${total_profit:,.2f}")
col4.metric("🏆 Best Product", best_product)

st.markdown("---")

# ==========================
# Monthly Sales
# ==========================
st.subheader("📅 Monthly Sales")

monthly_sales = df.groupby(df["Order Date"].dt.month)["Total Revenue"].sum()
# Month numbers ni names ga marchadam
monthly_sales.index = pd.to_datetime(monthly_sales.index, format='%m').strftime('%b')

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly_sales.index, monthly_sales.values, marker="o", linewidth=2)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
ax.set_title("Monthly Sales")
ax.grid(True)
plt.xticks(rotation=45)

st.pyplot(fig)

# ==========================
# Revenue by Region
# ==========================
st.subheader("🌍 Revenue by Region")

region = df.groupby("Region")["Total Revenue"].sum()

fig2, ax2 = plt.subplots(figsize=(8,8))
ax2.pie(region.values, labels=region.index, autopct="%1.1f%%", startangle=90)
ax2.set_title("Revenue by Region")
ax2.axis('equal')  # Circle ga undadaniki

st.pyplot(fig2)

# ==========================
# Best Selling Products
# ==========================
st.subheader("🏆 Best Selling Products")

top = df.groupby("Item Type")["Units Sold"].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.bar(top.index, top.values, color='skyblue')
ax3.set_xlabel("Products")
ax3.set_ylabel("Units Sold")
ax3.set_title("Top 10 Best Selling Products")
plt.xticks(rotation=45, ha='right')

st.pyplot(fig3)

# ==========================
# Dataset Preview
# ==========================
st.subheader("📋 Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

# ==========================
# Summary
# ==========================
st.success("Retail Store Dashboard Loaded Successfully ✅")