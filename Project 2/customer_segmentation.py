import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")

# ✅ Load the dataset
data = pd.read_csv("ifood_df.csv")
print("🔹 Data loaded successfully!")
print("🔹 Shape:", data.shape)

# ✅ View columns
print("🔹 Columns in dataset:")
print(data.columns)

# ✅ OPTIONAL: Drop columns you don't want to cluster on
# If you're sure some columns like 'ID' or similar exist and are unnecessary, drop them like this:
# data.drop(columns=["ID"], inplace=True)

# ✅ Scaling all features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# ✅ Apply PCA for 2D Visualization
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# ✅ Use Elbow Method to find optimal clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("📉 Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ Apply KMeans Clustering with optimal k (say, 4)
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_data)

# ✅ Visualize clusters (PCA-reduced 2D)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], hue=data['Cluster'], palette='Set2')
plt.title("🎯 Customer Segments (via PCA)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend(title='Cluster')
plt.tight_layout()
plt.show()

# ✅ Optional: View average profile of each cluster
print("\n🔍 Cluster Analysis (Averages):")
print(data.groupby('Cluster').mean())
