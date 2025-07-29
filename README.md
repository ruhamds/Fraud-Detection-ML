# 🛡️ Fraud Detection in E-Commerce and Banking with Machine Learning

> A full end-to-end machine learning pipeline for detecting fraudulent activity in both e-commerce and credit card transactions using interpretable models and SHAP-based explainability.

---

## 📌 Overview

This project builds a real-world fraud detection system using two distinct datasets:

* **🛍 E-Commerce Fraud**: Behavioral, time, and device-level signals from users making online purchases.
* **💳 Credit Card Fraud**: Bank transaction data with anonymized features.

We implemented the complete machine learning lifecycle including:

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Class imbalance handling with SMOTE
* Model training and threshold tuning
* SHAP-based model interpretation

---

## 📁 Project Structure

```plaintext
Fraud_detection/
├── data/                       # Raw and processed datasets
├── .github/
│   └── workflows/
│       ├── ci.yml              # Main test workflow
│       └── dvc-push.yml        # DVC-specific workflow
├── Notebooks/                  # Task-based Jupyter notebooks
│   ├── Task1/                  # Data cleaning, EDA, transformation
│   ├── Task2/                  # Model training and evaluation
│   └── Task3/                  # SHAP explainability and model insights
├── models/                     # Saved model files (.pkl, .npy)
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── README.md                   # You're here
```

---

## 🔢 Workflow Summary

### ✅ Task 1: Data Preparation

* Cleaned and merged IP addresses with geolocation (e-commerce)
* Parsed timestamp features (hour, weekday, is\_weekend, is\_night\_purchase)
* Engineered behavioral features like `time_since_signup`, `device_transaction_count`
* Binned `country`, `purchase_value`, `hour_of_day` for pattern recognition
* Applied **SMOTE** to address severe class imbalance
* Scaled numeric features using **StandardScaler**

### ✅ Task 2: Model Training & Evaluation

* Trained 3 models: Logistic Regression, Random Forest, XGBoost
* Tuned thresholds to improve fraud recall without spiking false positives
* Evaluated with:

  * ROC-AUC
  * PR-AUC (preferred in imbalanced cases)
  * Confusion matrix, Precision, Recall

#### 📊 Final Model Performance Summary

| Dataset     | Model                      | ROC-AUC | PR-AUC | F1-Score |
| ----------- | -------------------------- | ------- | ------ | -------- |
| E-Commerce  | Logistic Regression        | 0.83    | 0.67   | 0.69     |
|             | Random Forest              | 0.84    | 0.71   | 0.71     |
|             | ✅ **XGBoost** (Best)       | 0.83    | 0.72   | 0.71     |
| Credit Card | Logistic Regression        | 0.96    | 0.67   | 0.28     |
|             | XGBoost                    | 0.97    | 0.79   | 0.66     |
|             | ✅ **Random Forest** (Best) | 0.95    | 0.80   | 0.81     |

### ✅ Task 3: Explainability with SHAP

* Applied SHAP to XGBoost and Random Forest models
* Generated:

  * Summary plots (global feature importance)
  * Force plots (individual predictions)
  * Bar plots (mean impact on model output)
* Identified key fraud signals:

  * Odd transaction hours
  * Specific devices with repeated usage
  * Transaction country and value anomalies

---

## 🔎 Key Business Insights

*  Device 1 accounted for 87% of e-commerce transactions: strong fraud signal
*  Most fraudulent purchases occurred between 8 PM – 6 AM
*  Time since user signup had strong impact on fraud prediction
*  User-based frequency features were ineffective as each user had a single transaction
*  Threshold tuning reduced missed fraud cases by \~200+ with minimal increase in false positives

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
$ git clone https://github.com/ruhamds/fraud-detection-ml.git
$ cd fraud-detection-ml

# 2. Create and activate environment
$ python -m venv myenv
$ myenv\Scripts\activate      # Windows

# 3. Install dependencies
(myenv) $ pip install -r requirements.txt

# 4. Open notebooks
(myenv) $ jupyter notebook
```

---

## Technologies Used

* Python 3.10
* Pandas, NumPy, Scikit-learn
* XGBoost, imbalanced-learn (SMOTE)
* SHAP for explainability
* Matplotlib, Seaborn
* Jupyter Notebooks

---

## 🔗 Repository Link

> [GitHub Repository](https://github.com/ruhamds/fraud-detection-ml)


