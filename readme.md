# 🧠 Customer Churn Prediction

## 📘 Project Overview

This project predicts whether a customer is likely to churn from a telecom company using machine learning. The goal is to help businesses identify at-risk customers and take proactive measures to retain them. The project is deployed as a Streamlit web app for interactive predictions.

## 📊 Dataset Information

The dataset contains customer information from a telecom company, including:

- **Demographics**: Gender, Senior Citizen status, Partner, Dependents
- **Services**: Phone Service, Internet Service, Contract Type
- **Financials**: Monthly Charges, Total Charges
- **Tenure**: Number of months the customer has stayed with the company
- **Target Variable**: Churn (Yes/No)

> The dataset is commonly used for churn prediction and can be found in open-source repositories like Kaggle.

## 🧰 Tools & Technologies Used

- **Programming Language**: Python
- **Libraries**: pandas, scikit-learn, joblib, scipy
- **Web App Framework**: Streamlit
- **Machine Learning Model**: Support Vector Classifier (SVC)

## ⚙️ Project Workflow

1. **Data Preprocessing**: Handling categorical variables, encoding, and aligning features.
2. **Model Training**: Training an SVC model to predict churn.
3. **Model Saving**: Using `joblib` to save the trained model and feature list.
4. **Web App Deployment**: Building a Streamlit app for users to input customer details and get churn predictions.
5. **Prediction Handling**: Supporting both `predict_proba` (if available) or `decision_function` for models without probability enabled.

## 📈 Dashboard / Visualization

The Streamlit app allows users to:

- Input customer details interactively.
- Get real-time churn prediction: **Churn** or **No Churn**.
- Display probabilities (or decision scores) if available.
- Easily test multiple customer profiles using a CSV upload.

## 💡 Key Learnings

- Understanding how customer attributes influence churn.
- Handling categorical variables and aligning features for machine learning models.
- Deploying a machine learning model as a web app with Streamlit.
- Working with SVC models with/without probability estimates.

## 🚀 Future Improvements

- Integrate additional features like customer complaints, usage patterns, or engagement metrics.
- Add more models (Random Forest, XGBoost) for ensemble predictions.
- Enhance the Streamlit dashboard with charts and trend analysis.
- Add automated alerts for high-risk customers.

## 📬 Contact

For any queries or collaboration:

- **Name**: Abhinay Mahato
- **Email**: abhinaymahato10@gmail.cm
- **LinkedIn**: [linkedin.com/in/abhinay-mahato-a23b6b367](https://www.linkedin.com/in/abhinay-mahato-a23b6b367)
- **GitHub**: https://github.com/abhinay2708
