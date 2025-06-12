import pandas as pd
import numpy as np

# ✅ Step 1: Load the dataset
data = pd.read_csv("AB_NYC_2019.csv")
print("🔹 Original Data:")
print(data.head())

# ✅ Step 2: Dataset info
print("\n🔹 Data Info:")
print(data.info())

# ✅ Step 3: Drop irrelevant columns
data.drop(columns=["id", "name", "host_name", "last_review"], inplace=True)

# ✅ Step 4: Handle missing values
# Fill missing reviews with 0
data["reviews_per_month"] = data["reviews_per_month"].fillna(0)

# Drop rows with missing host_id or neighbourhood_group
data.dropna(subset=["host_id", "neighbourhood_group"], inplace=True)

# ✅ Step 5: Remove duplicates
before = data.shape[0]
data.drop_duplicates(inplace=True)
after = data.shape[0]
print(f"\n✅ Removed {before - after} duplicate rows")

# ✅ Step 6: Convert data types if needed
data["host_id"] = data["host_id"].astype(int)

# ✅ Step 7: Detect outliers in price
print("\n🔍 Price Outliers (above $500):")
print(data[data["price"] > 500].sort_values(by="price", ascending=False).head())

# Optional: Remove extreme outliers
data = data[data["price"] <= 500]

# ✅ Step 8: Rename columns for consistency
data.rename(columns={
    "neighbourhood_group": "borough",
    "neighbourhood": "area"
}, inplace=True)

# ✅ Step 9: Export cleaned data
data.to_csv("cleaned_airbnb_nyc.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_airbnb_nyc.csv'")
