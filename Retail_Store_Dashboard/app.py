import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="Retail Store Dashboard", layout="wide")

st.title("📊 Retail Store Dashboard")

# Load Dataset
df = pd.read_csv("Europe Sales Records.csv")

# ==========================
# KPI Cards
# ==========================
total_sales = df["Units Sold"].sum()
total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()

best_product = (
    df.groupby("Item Type")["Units Sold"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

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

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Total Revenue"]
    .sum()
)

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly_sales.index, monthly_sales.values, marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Monthly Sales")
ax.grid(True)

st.pyplot(fig)

# ==========================
# Revenue by Region
# ==========================
st.subheader("🌍 Revenue by Region")

region = df.groupby("Region")["Total Revenue"].sum()

fig2, ax2 = plt.subplots(figsize=(8,8))
ax2.pie(region.values,
        labels=region.index,
        autopct="%1.1f%%")

ax2.set_title("Revenue by Region")

st.pyplot(fig2)

# ==========================
# Best Selling Products
# ==========================
st.subheader("🏆 Best Selling Products")

top = (
    df.groupby("Item Type")["Units Sold"]
    .sum()
    .sort_values(ascending=False)
)

fig3, ax3 = plt.subplots(figsize=(10,5))

ax3.bar(top.index, top.values)

plt.xticks(rotation=45)

ax3.set_xlabel("Products")
ax3.set_ylabel("Units Sold")
ax3.set_title("Best Selling Products")

st.pyplot(fig3)

# ==========================
# Dataset Preview
# ==========================
st.subheader("📋 Dataset Preview")

st.dataframe(df.head(10))

# ==========================
# Summary
# ==========================
st.success("Retail Store Dashboard Loaded Successfully ✅")