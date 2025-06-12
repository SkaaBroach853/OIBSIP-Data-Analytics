# 🧠 Project 3 – Sentiment Analysis using Naive Bayes Classifier

This is Project 3 of the AICTE OASIS Infobyte Data Analytics Internship.

---

## 📌 Objective

To classify tweets as **Positive**, **Negative**, or **Neutral** by building a **text classification model** using Natural Language Processing (NLP) and a Naive Bayes algorithm.

---

## 📁 Dataset

- File: `Twitter_Data.csv`
- Columns:
  | Column      | Description                                |
  |-------------|--------------------------------------------|
  | `clean_text`| The tweet content, preprocessed            |
  | `category`  | Sentiment label: `-1.0`, `0.0`, or `1.0`   |

These values were mapped to:
- `-1.0` → Negative
- `0.0`  → Neutral
- `1.0`  → Positive

---

## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib & Seaborn
- Scikit-learn

---

## 🔍 Workflow Overview

### ✅ 1. **Data Preparation**
- Renamed columns for clarity
- Dropped missing values
- Mapped numeric sentiment values to readable labels

### ✅ 2. **Text Vectorization**
- Used **CountVectorizer** to convert tweets into numerical feature vectors

### ✅ 3. **Model Training**
- Used **Multinomial Naive Bayes**, a popular algorithm for text classification

### ✅ 4. **Model Evaluation**
- Used:
  - `classification_report` to show precision, recall, F1-score
  - `accuracy_score` to assess overall performance
  - `confusion_matrix` visualized using Seaborn’s heatmap

---

## 📈 Output Highlights

| Metric | Description |
|--------|-------------|
| Accuracy Score | Overall correctness of predictions |
| Classification Report | Detailed metrics for each sentiment class |
| Confusion Matrix | Matrix showing correct vs incorrect predictions |

---

## 🚀 How to Run

### Step 1: Install Required Packages
```bash
pip install pandas matplotlib seaborn scikit-learn
```
---
Step 2: Run the Script
```bash
python sentiment_analysis_final.py
```
---
## 🧠 Learning Outcomes
- ✅ Learned to clean and prepare text data

- ✅ Used vectorization to convert text into features

- ✅ Trained a Naive Bayes model for sentiment classification

- ✅ Evaluated model performance using metrics and plots

---
## 🙌 Acknowledgements
### This project is part of the AICTE OASIS Infobyte Data Analytics Internship.
---
## Author
- Name :- Aaditya Devadiga
- Oasis Internship - Data Analytics
