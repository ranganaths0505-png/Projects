# Project 01 — Retail Sales Analysis
## 📌 Project Overview

This project analyzes retail sales transaction data to understand sales performance, customer behavior, product performance, regional sales, and customer value.

The project uses Python, Pandas, NumPy, Matplotlib, and Seaborn for data analysis and visualization.

A major part of the project is RFM Analysis, which is used to segment customers based on their purchasing behavior.

## 🎯 Business Objectives

The main objectives of this project are:

- Analyze overall retail sales performance
- Identify top-performing products
- Analyze sales by region
- Understand payment-mode patterns
- Analyze monthly sales trends
- Identify high-value customers
- Detect potential customer spending outliers
- Perform RFM analysis
- Segment customers based on purchasing behavior

## 📊 Dataset

The dataset contains 1,000 retail orders with the following information:

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Date of the order |
| Customer_ID | Customer identifier |
| Product | Product purchased |
| Category | Product category |
| Quantity | Number of units purchased |
| Unit_Price | Price per unit |
| Region | Sales region |
| Payment_Mode | Payment method |
| Sales | Total sales amount |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

## 🔍 Analysis Performed

### 1. Data Exploration

Performed:

- Dataset shape and structure analysis
- Column inspection
- Data type checking
- Missing-value analysis
- Duplicate checking
- Statistical summary

### 2. Product Analysis

Analyzed:

- Number of orders by product
- Total sales by product
- Average sales per order

Laptop generated the highest total sales because of its high unit price.

### 3. Regional Analysis

Analyzed total sales across:

- North
- South
- East
- West

### 4. Payment Analysis

Compared:

- Credit Card
- Debit Card
- UPI
- Cash

Analysis included order count, total sales, and average sales per order.

### 5. Monthly Sales Analysis

Converted order dates into datetime format and analyzed monthly sales trends.

A line chart was used because monthly sales represent an ordered time-based trend.

### 6. Category Analysis

Compared sales and quantity between:

- Electronics
- Accessories

### 7. Customer Analysis

Analyzed customers using:

- Total Sales
- Number of Orders
- Average Order Value

### 8. Outlier Analysis

Used the IQR (Interquartile Range) method to identify customers with unusually high total spending.

### 9. RFM Analysis

Performed RFM analysis using:

- Recency
- Frequency
- Monetary

Customers were scored and segmented based on their purchasing behavior.

## 👥 Customer Segmentation

Customers were segmented using project-specific RFM rules.

| Segment | Customers | Total Sales | Average Sales |
|---|---:|---:|---:|
| Need Attention | 54 | ₹1,55,19,100 | ₹2,87,390.74 |
| Potential Loyalists | 41 | ₹1,44,58,900 | ₹3,52,656.10 |
| Champions | 19 | ₹1,11,07,700 | ₹5,84,615.79 |
| Lost Customers | 61 | ₹82,92,800 | ₹1,35,947.54 |
| Loyal Customers | 13 | ₹74,16,700 | ₹5,70,515.38 |
| At Risk | 11 | ₹43,71,000 | ₹3,97,363.64 |

### Key Findings

- Champions have a relatively small customer count but high average sales per customer.
- Loyal Customers also show high average customer value.
- Need Attention is the largest revenue-generating segment in this analysis.
- Lost Customers contain the largest number of customers.
- Customer count and customer revenue do not always tell the same story.

## 📊 Visualizations

The project includes visualizations for:

- Sales by Product
- Sales by Region
- Sales by Payment Mode
- Monthly Sales Trend
- Sales by Category
- Customer Sales Distribution
- RFM Score Distribution
- Customer Segment Distribution
- Total Sales by Customer Segment
- Average Sales by Customer Segment
- Region vs Product Sales Heatmap

## 📁 Project Structure

```text
Project-01-Retail-Sales-Analysis/
│
├── data/
│   ├── retail_sales.csv
│   └── customer_rfm_segments.csv
│
├── notebooks/
│   └── retail_sales_analysis.ipynb
│
├── src/
│   └── create_dataset.py
│
├── visualizations/
│
├── .venv/
│
├── README.md
└── requirements.txt

## 🚀 Key Skills Practiced

- Python
- Pandas
- NumPy
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Aggregation
- GroupBy
- Data Visualization
- Outlier Detection
- RFM Analysis
- Customer Segmentation
- Business Interpretation

## 💡 Project Outcome

This project demonstrates how raw retail transaction data can be transformed into meaningful business insights using data analysis, visualization, customer behavior analysis, outlier detection, and RFM-based customer segmentation.

The final RFM segmentation was saved as:

`data/customer_rfm_segments.csv`