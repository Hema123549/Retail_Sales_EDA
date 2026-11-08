# Retail Sales Data Analysis – Exploratory Data Analysis (EDA)

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a retail sales dataset to identify sales trends, customer purchasing patterns, and product category performance.

The analysis uses Python libraries to clean, analyze, and visualize retail transaction data.

## Objectives

- Understand overall retail sales performance.
- Analyze sales based on gender.
- Identify the best-performing product categories.
- Explore monthly sales trends.
- Understand customer age distribution and purchasing behaviour.
- Analyze daily sales patterns.
- Generate meaningful business insights through visualizations.

## Dataset Information

- Dataset: Retail Sales Dataset
- Source: Kaggle
- Total Records: 1,000
- Total Columns: 9

### Dataset Columns

1. Transaction ID
2. Date
3. Customer ID
4. Gender
5. Age
6. Product Category
7. Quantity
8. Price per Unit
9. Total Amount

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Project Structure

```text
Retail_Sales_EDA/
│
├── dataset/
│   └── retail_sales_dataset.csv
│
├── src/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── eda.py
│   └── visualizations.py
│
├── outputs/
│   ├── cleaned_retail_sales.csv
│   ├── sales_distribution.png
│   ├── monthly_sales_trend.png
│   ├── category_sales.png
│   ├── gender_analysis.png
│   ├── age_distribution.png
│   ├── category_quantity.png
│   ├── daily_sales.png
│   └── age_group_sales.png
│
├── venv/
├── README.md
└── requirements.txt
```

## Data Cleaning

The following preprocessing operations were performed:

- Checked and removed duplicate records.
- Checked duplicate transaction IDs.
- Converted the Date column into datetime format.
- Cleaned categorical text columns.
- Converted numerical columns into appropriate data types.
- Checked and handled missing values.
- Removed invalid numerical records.
- Verified transaction amount consistency.
- Saved the cleaned dataset.

### Cleaning Results

| Metric | Result |
|---|---:|
| Initial Records | 1,000 |
| Final Records | 1,000 |
| Missing Values | 0 |
| Duplicate Records | 0 |
| Inconsistent Transaction Amounts | 0 |

All 1,000 records were retained after validation.

## Exploratory Data Analysis

### 1. Overall Sales Performance

- Total Revenue: 456,000
- Total Transactions: 1,000
- Total Customers: 1,000
- Total Products Sold: 2,514
- Average Transaction Value: 456
- Highest Transaction Amount: 2,000
- Lowest Transaction Amount: 25

### 2. Gender-wise Sales Analysis

| Gender | Total Sales | Transactions |
|---|---:|---:|
| Female | 232,840 | 510 |
| Male | 223,160 | 490 |

Female customers contributed slightly more revenue than male customers.

### 3. Product Category Analysis

| Category | Total Sales | Quantity Sold |
|---|---:|---:|
| Electronics | 156,905 | 849 |
| Clothing | 155,580 | 894 |
| Beauty | 143,515 | 771 |

Electronics generated the highest revenue, while Clothing recorded the highest quantity sold.

### 4. Monthly Sales Analysis

- Highest Sales Month: May 2023 – 53,150
- Lowest Sales Month: September 2023 – 23,620

January 2024 recorded only 1,530 in sales. This month may represent partial-year data and should be interpreted cautiously.

### 5. Customer Age Analysis

- Average Customer Age: 41.39 years
- Highest Customer Count: 40–50 age group – 221
- Highest Revenue Age Group: 50–60 – 100,085

The 50–60 age group generated the highest total revenue.

### 6. Day-wise Sales Analysis

| Day | Total Sales |
|---|---:|
| Monday | 70,250 |
| Tuesday | 69,440 |
| Wednesday | 58,770 |
| Thursday | 53,835 |
| Friday | 66,290 |
| Saturday | 78,815 |
| Sunday | 58,600 |

Saturday recorded the highest sales, while Thursday recorded the lowest.

## Data Visualizations

The following visualizations were generated:

1. Sales Distribution
2. Monthly Sales Trend
3. Category-wise Sales
4. Gender-wise Sales
5. Customer Age Distribution
6. Quantity Sold by Category
7. Day-wise Sales Analysis
8. Sales by Customer Age Group

All visualizations are saved in the `outputs/` directory.

## Key Business Insights

- Electronics is the highest revenue-generating product category.
- Clothing has the highest quantity sold.
- Female customers contribute slightly more to total sales.
- May 2023 recorded the highest monthly sales.
- Customers aged 50–60 generated the highest revenue.
- Saturday is the strongest sales day in the dataset.
- Overall average transaction value is 456.

## Limitations

- The dataset contains only 1,000 transactions.
- Each transaction has a distinct customer ID, so repeat customer behaviour cannot be evaluated from this dataset.
- January 2024 contains very limited sales data.
- The analysis is based on historical transaction records and does not predict future sales.

## Conclusion

This project demonstrates how Exploratory Data Analysis can be used to understand retail sales performance and customer purchasing patterns.

Through data cleaning, statistical analysis, and visualization, meaningful insights were identified regarding product categories, customer demographics, and sales trends.

The findings can help businesses better understand their sales performance and support data-driven decision-making.

## Author

Data Science Internship Project – Oasis Infobyte