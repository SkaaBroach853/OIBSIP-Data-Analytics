# 🎯 Project 2– Customer Segmentation using KMeans Clustering

This project 2 is part of the AICTE OASIS Infobyte Data Analytics Internship.

---

## 📌 Objective

To segment customers based on their behavior using **KMeans clustering**.  
The goal is to group customers with similar characteristics so that companies can target them with personalized marketing strategies.

---

## 📁 Dataset

- File: `ifood_df.csv`
- Sample Features:
  | Column           | Description                         |
  |------------------|-------------------------------------|
  | Age, Income, Spending | Numerical features used to group customers |
  | Campaign responses, Product purchases | Behavior-based metrics |
  | All features are numerical or encoded |

---

## 🛠️ Tools Used

- Python 3
- Pandas, NumPy – data manipulation
- Scikit-learn – ML models and PCA
- Matplotlib, Seaborn – visualization

---

## 🔍 Project Steps

### ✅ 1. Data Loading
- Loaded the dataset using `pandas.read_csv()`
- Printed shape and column names for inspection

### ✅ 2. Feature Scaling
- Used `StandardScaler()` to normalize all columns
- Ensured fair contribution from all features

### ✅ 3. Dimensionality Reduction (for visualization)
- Applied `PCA` to reduce data to 2 components
- This helps plot clusters visually in 2D

### ✅ 4. Elbow Method for Optimal Clusters
- Ran `KMeans` for 1 to 10 clusters
- Plotted **Within Cluster Sum of Squares (WCSS)** to choose best `k`
- Selected **k = 4** clusters for final segmentation

### ✅ 5. Apply KMeans
- Assigned cluster labels to each record
- Stored in new column: `Cluster`

### ✅ 6. Visualization
- Used `Seaborn` to plot clusters in 2D using PCA
- Clear separation shown by color

### ✅ 7. Cluster Analysis
- Used `.groupby('Cluster').mean()` to profile customer groups

---

## 📈 Visual Outputs

| Plot | Description |
|------|-------------|
| Elbow Curve | Helps choose the optimal number of clusters |
| Cluster Scatter Plot | Shows how customer groups are distributed |
| Cluster Stats | Gives insight into average behavior of each cluster |

---

## 🚀 How to Run

### Step 1: Install Libraries
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
---
### Step 2: Run the script
```bash
python customer_segmentation.py
```
---
## 🧠 Learning Outcomes
- ✅ Applied unsupervised learning (KMeans)

- ✅ Practiced data scaling and PCA

- ✅ Learned how to determine cluster count using the elbow method

- ✅ Visualized and interpreted customer segments
---
## Author
- Name :- Aaditya Devadiga
- Oasis Internship - Data Analytics
