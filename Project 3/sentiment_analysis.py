# ✅ Imort Libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# ✅ Load dataset
data = pd.read_csv("Twitter_Data.csv")
print("✅ Data loaded. Shape:", data.shape)

# ✅ Rename columns (for consistency, optional)
data.rename(columns={"clean_text": "text", "category": "sentiment"}, inplace=True)

# ✅ Drop any rows with missing valuSses
data.dropna(subset=["text", "sentiment"], inplace=True)

# ✅ Convert sentiment from float to string labels
sentiment_map = {-1.0: "Negative", 0.0: "Neutral", 1.0: "Positive"}
data["sentiment"] = data["sentiment"].map(sentiment_map)

# ✅ Split the dataset
X = data["text"]
y = data["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Convert text to feature vectors
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ✅ Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# ✅ Make predictions
y_pred = model.predict(X_test_vec)

# ✅ Evaluate performance
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))

print("✅ Accuracy Score:", round(accuracy_score(y_test, y_pred), 2))

# ✅ Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=["Positive", "Neutral", "Negative"])
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Positive", "Neutral", "Negative"], yticklabels=["Positive", "Neutral", "Negative"])
plt.title("📊 Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()
