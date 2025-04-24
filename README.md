# SalesDataAnalysisAndDashboard
## Objective:
To analyze and visualize a company's sales data to understand trends, top products, regional performance, and more using Python, Pandas and visualization libraries.

## Dataset Used:
File Name: sales_data_sample.csv
Columns Included (as per assumption and preprocessing steps):
  - Date
  - Product
  - Units Sold
  - Unit Price
  - Region
  - Category
## Tools and Libraries:
  - Pandas: For data manipulation
  - Matplotlib: For data visualization
  - Jupyter Notebook: Interactive development environment
## Step 1: Data Cleaning & Preparation
Actions Performed:
  - Converted the Date column to datetime64 format using pd.to_datetime()
  - Created a new column Revenue = Units Sold * Unit Price
  - Checked for missing values using .isnull().sum()
