import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "outputs", "cleaned_retail_sales.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])

sns.set_theme(style="whitegrid")

# 1. Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Total Amount"], bins=30, kde=True)
plt.title("Retail Sales Distribution")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sales_distribution.png"))
plt.close()

# 2. Monthly Sales Trend
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Total Amount"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "monthly_sales_trend.png"))
plt.close()

# 3. Category-wise Sales
category_sales = df.groupby("Product Category")["Total Amount"].sum()

plt.figure(figsize=(8, 5))
category_sales.sort_values().plot(kind="barh")
plt.title("Sales by Product Category")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "category_sales.png"))
plt.close()

# 4. Gender-wise Sales
gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(7, 5))
gender_sales.plot(kind="bar")
plt.title("Gender-wise Sales")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "gender_analysis.png"))
plt.close()

# 5. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "age_distribution.png"))
plt.close()

# 6. Category Quantity
quantity_sales = df.groupby("Product Category")["Quantity"].sum()

plt.figure(figsize=(8, 5))
quantity_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Quantity Sold by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "category_quantity.png"))
plt.close()

# 7. Day-wise Sales
df["Day"] = df["Date"].dt.day_name()

day_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

daily_sales = df.groupby("Day")["Total Amount"].sum().reindex(day_order)

plt.figure(figsize=(10, 5))
daily_sales.plot(kind="bar")
plt.title("Day-wise Sales Analysis")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "daily_sales.png"))
plt.close()

# 8. Sales by Age Group
df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0, 20, 30, 40, 50, 60, 100],
    labels=["Below 20", "20-30", "30-40", "40-50", "50-60", "Above 60"]
)

age_sales = df.groupby("Age Group", observed=False)["Total Amount"].sum()

plt.figure(figsize=(9, 5))
age_sales.plot(kind="bar")
plt.title("Sales by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "age_group_sales.png"))
plt.close()

print("\n========== VISUALIZATIONS COMPLETED ==========")
print("8 graphs saved successfully inside outputs folder!")