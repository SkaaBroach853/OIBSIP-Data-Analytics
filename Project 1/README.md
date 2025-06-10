# 📊 Project 1 – Exploratory Data Analysis on Retail Sales Data

This is Project 1 of the AICTE OASIS Infobyte Data Analytics Internship.  
In this project, we perform **Exploratory Data Analysis (EDA)** on a retail sales dataset using Python.  
EDA helps understand customer behavior, sales trends, and product performance using data visualization and statistical analysis.

---

## 📁 Dataset Description

The dataset contains transaction-level information from a retail store. Below are the columns:

| Column | Description |
|--------|-------------|
| `Transaction ID` | Unique ID for each transaction |
| `Date` | Date when the transaction occurred |
| `Customer ID` | Unique customer identifier |
| `Gender` | Gender of the customer |
| `Age` | Age of the customer |
| `Product Category` | Category of product purchased |
| `Quantity` | Number of units bought |
| `Price per Unit` | Price of one unit |
| `Total Amount` | Total transaction value = Quantity × Price |

---

## 🧠 Objectives

- Perform basic data cleaning (missing values, duplicates)
- Analyze time-based trends in sales
- Understand purchasing patterns by gender, age, and category
- Visualize patterns using plots
- Explore correlations between different numeric fields

---

## 🛠️ Tools Used

- **Python 3**
- **Pandas** – for data manipulation
- **NumPy** – for numerical calculations
- **Matplotlib & Seaborn** – for visualization

---

## 📈 Exploratory Data Analysis Performed

### 1. Dataset Overview
- Checked number of rows and columns
- Inspected data types and null values
- Removed duplicate entries (if any)

### 2. Time Series Sales Trends
- Converted the `Date` column to datetime format
- Aggregated and plotted **total daily sales** over time

### 3. Top 10 Product Categories
- Grouped data by `Product Category`
- Calculated total revenue and plotted the **top 10 categories**

### 4. Gender-wise Spending
- Grouped by `Gender` to see which gender spent more
- Created a **bar chart** comparison

### 5. Age Distribution
- Plotted a histogram to understand customer **age spread**

### 6. Correlation Heatmap
- Visualized correlation between numeric fields like `Quantity`, `Price`, `Total Amount`, and `Age`

---

## 📸 Sample Output Visuals

<Add screenshots here after running the project>  
Example:
- 📈 Daily Sales Trend
- 🏆 Top Product Categories
- 👥 Gender Spending Chart
- 📊 Age Histogram
- 📌 Correlation Heatmap

---

## 🚀 How to Run This Project

### 1. Clone or Download This Repository
```bash
Clone the File in your system
```
---
## 2. Install Required Python Packages
```bash

pip install -r requirements.txt
```
---
## 3. Run the Python Script
```bash

python retail_eda.py
```

## Author
- Name :- Aaditya Devadiga
- Oasis Internship - Data Analytics
