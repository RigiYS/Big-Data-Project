# Big-Data-Project

# 📱 Shopee Smartphone Sales Prediction

This project is part of a Big Data final assignment. It aims to predict the number of smartphone units sold on Shopee based on product features using **Random Forest Regression**, and deploy the solution using **Streamlit**.

---

## 🚀 Project Overview

- **Objective**: Predict product sales volume on Shopee e-commerce platform
- **Model Used**: Random Forest Regression
- **Deployment**: Streamlit Web App
- **Dataset**: Scraped from Shopee search results for "smartphone"
- **Data Size**: 151 rows (cleaned to 140)

---

## 📊 Features Used

| Feature      | Type       | Description                             |
|--------------|------------|-----------------------------------------|
| `price`      | Numeric    | Product price in IDR                    |
| `rating`     | Float      | Average user rating                     |
| `address`    | Categorical| Seller location (one-hot encoded)       |

**Target:** `sold` (Number of units sold)

---

## 🧪 Model Performance

| Metric                 | Value         |
|------------------------|---------------|
| R² Score               | 0.5864        |
| Mean Squared Error     | 5,458,801.90  |

---

## 📦 Tech Stack

- **Python**
- **Scikit-Learn** – for model training
- **Pandas & NumPy** – for data preprocessing
- **Matplotlib & Seaborn** – for visualization
- **Streamlit** – for app deployment
- **Joblib** – for saving and loading the model
- **Shopee + Data Scraper Extension** – for data collection

---

## 🌐 Deployment

The app is deployed using **Streamlit Cloud**, allowing users to input product attributes (price, rating, location) and get a real-time prediction of estimated units sold.

🔗 **Live Demo**: https://big-data-project-fjwzcc2tqxxkpfkwmcswjw.streamlit.app/  
🔗 **Presentation Video**: https://youtu.be/VS13YPRA2Us

---

## 📁 Project Structure

```bash
📦 shopee-sales-prediction/
│
├── dataset_hp.csv            # Raw dataset (scraped)
├── model_rf.pkl              # Trained Random Forest model
├── model_features.npy        # Saved feature names for prediction
├── app.py                    # Streamlit app script
├── README.md                 # This file
└── requirements.txt          # Python dependencies
