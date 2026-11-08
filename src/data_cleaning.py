import pandas as pd
import os

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
DATA_PATH = os.path.join(BASE_DIR, "dataset", "retail_sales_dataset.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "outputs", "cleaned_retail_sales.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\n========== DATA CLEANING STARTED ==========")

print("\nINITIAL DATASET SHAPE:")
print(df.shape)

# 1. Remove duplicate records
df.drop_duplicates(inplace=True)

# 2. Remove duplicate transaction IDs
df.drop_duplicates(subset="Transaction ID", inplace=True)

# 3. Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 4. Clean text columns
text_columns = ["Customer ID", "Gender", "Product Category"]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# 5. Convert numerical columns
numeric_columns = [
    "Transaction ID",
    "Age",
    "Quantity",
    "Price per Unit",
    "Total Amount"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 6. Remove rows with missing essential values
essential_columns = [
    "Transaction ID",
    "Date",
    "Customer ID",
    "Gender",
    "Age",
    "Product Category",
    "Quantity",
    "Price per Unit",
    "Total Amount"
]

df.dropna(subset=essential_columns, inplace=True)

# 7. Remove invalid numerical values
df = df[
    (df["Age"] > 0) &
    (df["Quantity"] > 0) &
    (df["Price per Unit"] > 0) &
    (df["Total Amount"] > 0)
]

# 8. Check transaction amount consistency
df["Calculated Amount"] = df["Quantity"] * df["Price per Unit"]

inconsistent_rows = (
    df["Total Amount"] != df["Calculated Amount"]
).sum()

print("\nINCONSISTENT TRANSACTION AMOUNTS:")
print(inconsistent_rows)

# Remove temporary column
df.drop(columns=["Calculated Amount"], inplace=True)

# 9. Reset index
df.reset_index(drop=True, inplace=True)

# 10. Save cleaned dataset
df.to_csv(OUTPUT_PATH, index=False)

print("\nCLEANED DATASET SHAPE:")
print(df.shape)

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

print("\nDUPLICATES AFTER CLEANING:")
print(df.duplicated().sum())

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")

print("\n========== DATA CLEANING COMPLETED ==========")