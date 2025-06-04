# 🐓 Predicting Poultry Mortality Using Environmental and Health Indicators

This project applies **data science and machine learning** to a critical issue in agriculture: **unexpected poultry deaths**. By integrating **health symptoms** with **environmental data**, we built a predictive model to identify mortality risks and support **early intervention** in poultry farming operations.

---

## 📌 Project Objective

To **predict poultry mortality**—specifically birds found dead—using:
- **Health indicators** like Wasting, Respiratory issues, Diarrhoea, and Skin conditions
- **Environmental factors**, particularly regional **Max and Min temperatures**

Early detection enables **proactive health management**, helping reduce economic losses and improve animal welfare.

---

## 🧠 What’s Inside?

- 📂 Cleaned and preprocessed dataset (with duplicates removed)
- 📈 Exploratory Data Analysis (EDA) using correlation heatmaps, boxplots, and pairplots
- 🧮 Linear Regression model to forecast mortality cases
- 🧪 Model evaluation using RMSE, R² Score, and statistical significance testing (t-test)
- 📊 Key insights on how **temperature and specific symptoms** affect bird deaths

---

## 🔍 Key Findings

- 📈 **High temperatures correlate** with increased poultry mortality
- ⚠️ Symptoms like **Wasting and Respiratory problems** are strong predictors of bird deaths
- 🛠 Predictive modeling can guide **real-time health interventions** in farms

---

## 🚀 Why It Matters

This project demonstrates the potential of **data-driven agriculture**. Our approach lays the foundation for building a **decision-support tool** for poultry managers and veterinarians—enhancing both productivity and sustainability in livestock farming.

---

## 🔧 How to Run the Project

### 📦 1. Install Required Libraries

Before running the project, ensure you have Python 3.8+ installed. Use the following command to install all dependencies:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn statsmodels
