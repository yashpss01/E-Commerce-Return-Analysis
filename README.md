# 🛒 E-Commerce Returns & Revenue Leakage Analysis

## 📌 Project Overview

This project analyzes raw e-commerce transactional data to identify **revenue leakage caused by product returns, cancellations, and data inconsistencies**.

The goal is to build an **end-to-end data analytics pipeline** using Python for ETL and Tableau for visualization, ultimately delivering **data-driven business recommendations**.

---

## 🎯 Problem Statement

E-commerce businesses often face significant losses due to:

* High product return rates
* Inefficient order handling
* Inconsistent and messy transactional data

This project aims to:

* Quantify **revenue loss due to returns**
* Identify **patterns across products, customers, and regions**
* Provide **actionable insights** to improve profitability

---

## 📂 Dataset

* Source: Kaggle
* Dataset: *E-Commerce Data (Online Retail Dataset)*
* Link: https://www.kaggle.com/datasets/carrie1/ecommerce-data

### Dataset Characteristics

* ~500,000+ rows
* Transaction-level data
* Contains real-world issues:

  * Missing values
  * Duplicate records
  * Negative quantities (returns)
  * Inconsistent formats

---

## ⚙️ Tech Stack

* **Python** (Pandas, NumPy) → Data Cleaning & Analysis
* **Jupyter Notebook** → ETL & EDA
* **Tableau Public** → Dashboard & Visualization
* **GitHub** → Version Control & Collaboration

---

## 🧹 ETL Pipeline (Python)

### Step 1: Data Extraction

* Load raw dataset from `data/raw/`

### Step 2: Data Cleaning

* Handle missing values (CustomerID, Description)
* Remove duplicates
* Convert data types (InvoiceDate → datetime)
* Filter invalid values (Quantity ≤ 0, UnitPrice ≤ 0)

### Step 3: Feature Engineering

* Revenue = Quantity × UnitPrice
* Return Flag (IsReturn)
* Time-based features (Month, Year)

### Step 4: Load Processed Data

* Save cleaned dataset to `data/processed/`

---

## 📊 Key Performance Indicators (KPIs)

* **Total Revenue**
* **Total Returns Value**
* **Return Rate (%)**
* **Net Revenue**
* **Average Order Value**
* **Revenue by Country**
* **Top Products by Sales**
* **Top Products by Returns**

---

## 📈 Exploratory Data Analysis (EDA)

* Monthly sales trends
* Return patterns over time
* Product-level performance
* Country-wise revenue distribution
* Identification of outliers and anomalies

---

## 📉 Statistical Analysis

* Correlation analysis (price vs returns)
* Hypothesis testing:

  * Do higher-priced products have higher return rates?
* Basic regression for return behavior insights

---

## 📊 Tableau Dashboard

### Features

* KPI overview cards
* Sales vs Returns trend
* Product performance analysis
* Geographic revenue distribution
* Interactive filters

📎 Dashboard Link: [Dashboard files](https://drive.google.com/drive/folders/1y8mlpQwBGinrN4leqr96BEFkA4gSNZ2L?usp=sharing)

---

## 💡 Key Insights (Sample)

* A small subset of products contributes disproportionately to returns
* Certain regions show consistently higher return rates
* Returns spike during specific months (seasonal effect)
* Some products generate revenue but result in net loss after returns

---

## 📌 Business Recommendations

* Improve quality control for high-return products
* Optimize logistics in high-return regions
* Adjust pricing/discount strategies
* Enhance product descriptions to reduce mismatched expectations

---

## 📁 Project Structure

```
📦 Ecommerce-Returns-Analysis
 ┣ 📂 data
 ┃ ┣ 📂 raw
 ┃ ┗ 📂 processed
 ┣ 📂 notebooks
 ┃ ┣ 02_cleaning.ipynb
 ┃ ┣ 03_eda.ipynb
 ┃ ┣ 04_statistical_analysis.ipynb
 ┃ ┗ 05_final_load_prep.ipynb
 ┣ 📂 tableau
 ┃ ┣ screenshots/
 ┃ ┗ dashboard_links.md
 ┣ 📂 docs
 ┃ ┗ data_dictionary.md
 ┣ README.md
```

---

## 👥 Team Contributions

| Member                    | Role               | Responsibility                |
| ------------------------- | ------------------ | ----------------------------- |
| Ved Bhadani               | Data Engineer      | ETL & Cleaning Pipeline       |
| Archisman Nath Choudhury  | Analyst            | Feature Engineering & KPIs    |
| Krish Amit Modi           | Analyst            | EDA & Insights                |
| Yash Pratap Singh Solanki | Analyst            | Statistical Analysis          |
| Akanksha                  | Visualization Lead | Tableau Dashboard & Reporting |

---

## 🚀 How to Run the Project

1. Clone the repository
2. Install required libraries
3. Run notebooks in order:

   * `02_cleaning.ipynb`
   * `03_eda.ipynb`
   * `04_statistical_analysis.ipynb`
4. Open Tableau dashboard via provided link

---

## 📊 Outcome

This project demonstrates:

* End-to-end data analytics workflow
* Strong data cleaning and transformation skills
* Business-focused insight generation
* Interactive dashboard design

---

## ⚠️ Disclaimer

This dataset contains real-world inconsistencies and has been cleaned for analysis purposes. Insights are based on available data and assumptions.

---

## 📎 Future Scope

* Customer segmentation (RFM analysis)
* Predictive modeling for returns
* Recommendation systems for product optimization

---
