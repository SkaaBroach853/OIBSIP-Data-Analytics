# 🧼 Project 4 – Data Cleaning of NYC Airbnb Dataset

This is Project 4 of the AICTE OASIS Infobyte Data Analytics Internship.

---

## 📌 Objective

To clean and prepare the **New York City Airbnb Open Data** dataset by:
- Removing irrelevant columns and duplicates  
- Handling missing values  
- Detecting and correcting outliers  
- Renaming and standardizing column names  

Clean data is essential for reliable data analysis, visualization, and modeling.

---

## 📁 Dataset

- 🗂️ Dataset Name: `AB_NYC_2019.csv`
- 📥 Source: [Kaggle - NYC Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

| Column | Description |
|--------|-------------|
| `id`, `name`, `host_name` | Identification info (not needed for analysis) |
| `host_id` | Unique ID of the host |
| `neighbourhood_group` | Borough (e.g., Manhattan) |
| `neighbourhood` | More specific area |
| `latitude`, `longitude` | Location coordinates |
| `room_type` | Type of accommodation (Entire home, Private room, etc.) |
| `price` | Price per night |
| `reviews_per_month` | Monthly average reviews (may be missing) |
| `last_review` | Last review date (many nulls) |

---

## 🛠️ Tools Used

- Python 3
- Pandas
- NumPy

---

## 🔍 Key Cleaning Steps

### ✅ 1. **Dropped Irrelevant Columns**
- Removed columns like `id`, `name`, `host_name`, `last_review`

### ✅ 2. **Handled Missing Values**
- Filled `reviews_per_month` with 0
- Dropped rows missing `host_id` or `neighbourhood_group`

### ✅ 3. **Removed Duplicates**
- Used `.drop_duplicates()` to ensure unique rows

### ✅ 4. **Converted Data Types**
- Converted `host_id` to integer

### ✅ 5. **Detected and Removed Outliers**
- Identified listings with **extremely high prices (above $500)**
- Removed them to prevent skewed analysis

### ✅ 6. **Renamed Columns**
- `neighbourhood_group` → `borough`
- `neighbourhood` → `area`

---
## 🚀 How to Run

### Step 1: Install Dependencies
```bash
pip install pandas numpy
```
---
## Step 2: Run the Script
```bash

python airbnb_data_cleaning.py
```
---
## Output:
- Cleaned file: cleaned_airbnb_nyc.csv
---
## 🧠 Learning Outcomes
- ✅ Learned to identify and remove irrelevant features

- ✅ Handled missing values and duplicates

- ✅ Performed outlier detection

- ✅ Gained experience in data wrangling using Pandas

---
## 🙌 Acknowledgements
### This project is part of the AICTE OASIS Infobyte Data Analytics Internship.
---
## Author
- Name :- Aaditya Devadiga
- Oasis Internship - Data Analytics
