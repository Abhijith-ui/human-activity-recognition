# 🧠 Human Activity Recognition

## 📌 Problem
Classify human activities such as walking, sitting, and standing using smartphone sensor data.

## 📊 Dataset
UCI Human Activity Recognition Dataset  
🔗 https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

---

## ⚙️ Approach
- Data preprocessing
- Feature analysis
- Dimensionality reduction (PCA)
- Supervised learning (Random Forest)
- Unsupervised learning (KMeans clustering)

---

## 🤖 Supervised Learning (Classification)

### Model Performance

- Base Random Forest Accuracy: 92.57%
- Tuned Random Forest Accuracy: 92.29%
- PCA + Random Forest Accuracy: 91.14%

### Insights

- Random Forest performed strongly on high-dimensional sensor data
- PCA reduced features from 561 to ~69 with minimal accuracy loss (~1.4%)
- Hyperparameter tuning reduced overfitting but slightly lowered accuracy

---

## 🔍 Unsupervised Learning (Clustering Analysis)

### Approach

- Applied KMeans clustering
- Used PCA and t-SNE for visualization

### Results

- Silhouette Score: ~0.13 (low)
- Poor cluster separation observed

### Insights

- Activities overlap in feature space
- Clustering is not suitable for this dataset
- Supervised learning performs significantly better

---

## 🧠 Key Takeaways

- Dimensionality reduction is effective for high-dimensional data
- PCA helps simplify models without major performance loss
- Not all problems are suitable for clustering
- Choosing the right ML approach is critical

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```
