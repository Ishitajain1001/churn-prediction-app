# churn-prediction-app

# Telco Customer Churn Prediction App

This Streamlit app predicts whether a telecom customer is likely to **churn** based on their account information, contract type, and service usage. It's powered by a decision tree machine learning model trained on real-world telco customer data.

![App Screenshot](https://user-images.githubusercontent.com/your-screenshot-placeholder.png)

---

## 📊 How It Works

- Built with a **Decision Tree Classifier**
- Takes in 30 customer features like:
  - Monthly charges
  - Tenure
  - Internet service type
  - Payment method
  - Streaming activity
  - Contract type
- Outputs a prediction of:
  - `✅ Likely to Stay`
  - `⚠️ Likely to Churn`
- Also displays the **probability** of churn for greater interpretability

---

## 🚀 Try It Live

🔗 [Launch the app on Streamlit Cloud](https://churn-prediction-app-fe7yidjcssfqxpttfksov9.streamlit.app/)

> 📌 Note: You can also clone this repo and run locally using Streamlit.

---

## 🧠 ML Model Details

- **Model**: Decision Tree Classifier (`scikit-learn`)
- **Training set**: Telco Customer Churn dataset
- **Feature Engineering**:
  - One-hot encoding for categorical variables
  - Scaling not required for tree-based model
- **Evaluation Metrics**:
  - Accuracy: ~78%
  - F1-score (churn class): ~0.58
  - Balanced precision/recall performance

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) for the frontend
- [scikit-learn](https://scikit-learn.org/) for model building
- [joblib](https://joblib.readthedocs.io/) for model persistence
- [Python 3.13] for backend logic

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app
pip install -r requirements.txt
streamlit run app.py
