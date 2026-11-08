import pandas as pd
import os

# Dataset path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "dataset", "retail_sales_dataset.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\n========== RETAIL SALES DATASET ==========")

# Dataset shape
print("\nDATASET SHAPE:")
print(df.shape)

# First five records
print("\nFIRST 5 RECORDS:")
print(df.head())

# Column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Data types
print("\nDATA TYPES:")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe(include="all"))

print("\n========== DATA LOADING COMPLETED ==========")