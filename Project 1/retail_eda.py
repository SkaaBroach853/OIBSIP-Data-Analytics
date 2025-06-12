# ✅ 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ 2. Load the Dataset
data = pd.read_csv("retail_sales_dataset.csv")

# ✅ 3. Show First Few Rows
print("🔹 First 5 rows:")
print(data.head())

# ✅ 4. Dataset Information
print("\n🔹 Dataset Info:")
print(data.info())

# ✅ 5. Descriptive Statistics
print("\n🔹 Descriptive Statistics:")
print(data.describe())

# ✅ 6. Missing Values Check
print("\n🔹 Missing Values:")
print(data.isnull().sum())

# ✅ 7. Duplicate Check
duplicates = data.duplicated().sum()
print(f"\n🔹 Number of duplicate rows: {duplicates}")

# ✅ 8. Drop Duplicates
data.drop_duplicates(inplace=True)

# ✅ 9. Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# ✅ 10. Daily Total Sales Over Time
daily_sales = data.groupby('Date')['Total Amount'].sum()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title("📈 Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ 11. Top 10 Product Categories by Revenue
top_products = data.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='magma')
plt.title("🏆 Top 10 Product Categories by Revenue")
plt.xlabel("Total Revenue (₹)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.show()

# ✅ 12. Gender-Based Spending
gender_sales = data.groupby('Gender')['Total Amount'].sum()

plt.figure(figsize=(6, 4))
sns.barplot(x=gender_sales.index, y=gender_sales.values, palette='coolwarm')
plt.title("👥 Gender-based Spending")
plt.xlabel("Gender")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.show()

# ✅ 13. Age Distribution of Customers
plt.figure(figsize=(8, 5))
sns.histplot(data['Age'], bins=10, kde=True, color='skyblue')
plt.title("📊 Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# ✅ 14. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title("📌 Correlation Heatmap")
plt.tight_layout()
plt.show()
