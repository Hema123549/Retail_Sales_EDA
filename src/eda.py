import pandas as pd
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR, "outputs", "cleaned_retail_sales.csv"
)

# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

df["Date"] = pd.to_datetime(df["Date"])

print("\n========== RETAIL SALES EDA ==========")

# 1. Overall Sales Analysis
print("\n1. OVERALL SALES ANALYSIS")

print("Total Revenue:", df["Total Amount"].sum())
print("Total Transactions:", df["Transaction ID"].nunique())
print("Total Customers:", df["Customer ID"].nunique())
print("Total Products Sold:", df["Quantity"].sum())

print("Average Transaction Value:",
      round(df["Total Amount"].mean(), 2))

print("Highest Transaction:",
      df["Total Amount"].max())

print("Lowest Transaction:",
      df["Total Amount"].min())


# 2. Gender Analysis
print("\n2. GENDER-WISE SALES")

gender_sales = df.groupby("Gender").agg(
    Total_Sales=("Total Amount", "sum"),
    Transactions=("Transaction ID", "count"),
    Average_Sales=("Total Amount", "mean")
)

print(gender_sales)


# 3. Product Category Analysis
print("\n3. CATEGORY-WISE SALES")

category_sales = df.groupby("Product Category").agg(
    Total_Sales=("Total Amount", "sum"),
    Quantity_Sold=("Quantity", "sum"),
    Transactions=("Transaction ID", "count")
).sort_values(by="Total_Sales", ascending=False)

print(category_sales)


# 4. Monthly Sales Analysis
print("\n4. MONTHLY SALES")

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Total Amount"].sum()

print(monthly_sales)


# 5. Age Analysis
print("\n5. CUSTOMER AGE ANALYSIS")

print("Average Customer Age:",
      round(df["Age"].mean(), 2))

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0, 20, 30, 40, 50, 60, 100],
    labels=[
        "Below 20",
        "20-30",
        "30-40",
        "40-50",
        "50-60",
        "Above 60"
    ]
)

age_analysis = df.groupby(
    "Age Group", observed=False
).agg(
    Customers=("Customer ID", "count"),
    Total_Sales=("Total Amount", "sum")
)

print(age_analysis)


# 6. Top Customers
print("\n6. TOP 10 CUSTOMERS BY SALES")

top_customers = df.groupby(
    "Customer ID"
)["Total Amount"].sum().sort_values(
    ascending=False
).head(10)

print(top_customers)


# 7. Daily Sales Analysis
print("\n7. DAY-WISE SALES")

df["Day"] = df["Date"].dt.day_name()

daily_sales = df.groupby("Day")["Total Amount"].sum()

print(daily_sales)


# 8. Product Quantity Analysis
print("\n8. PRODUCT QUANTITY ANALYSIS")

print(df.groupby("Product Category")["Quantity"].sum())


print("\n========== EDA COMPLETED ==========")