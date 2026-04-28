# 🛒 E-Commerce Return Analysis & Revenue Leakage Detection

## 📌 Overview
This project builds a complete data analytics pipeline to analyze e-commerce transactions and uncover revenue leakage caused by returns, cancellations, and data inconsistencies.

It combines ETL, exploratory data analysis (EDA), and statistical insights to help businesses reduce losses and improve profitability.

## 🚀 Objectives
*   Quantify revenue loss due to returns
*   Identify patterns in returns across products, regions, and customers
*   Clean and standardize messy real-world transactional data
*   Generate business insights for decision-making

## 📂 Project Structure
```
E-Commerce-Return-Analysis/
│
├── data/
│   ├── raw/
│   │   └── online_sales_dataset.csv
│   ├── processed/
│   │   └── cleaned_online_sales.csv
│
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   ├── 05_final_load_prep.ipynb
│
├── scripts/
│   └── etl_pipeline.py
│
├── docs/
│   └── data_dictionary.md
│
└── README.md
```

## 📊 Dataset
*   **Source:** Kaggle
*   **Dataset:** Online Retail Dataset
*   **Size:** ~44,000+ rows
*   **Type:** Transaction-level data

### Key Issues in Data
*   Missing values (CustomerID, Description)
*   Duplicate transactions
*   Negative quantities (returns)
*   Inconsistent formats

## ⚙️ Tech Stack
*   **Python** → Pandas, NumPy
*   **Jupyter Notebooks** → Data exploration & analysis
*   **ETL Pipeline** → Custom Python script
*   **Visualization** → Tableau (external)
*   **Version Control** → Git & GitHub

## 🔄 ETL Pipeline
The project follows a structured ETL workflow:

1.  **Extraction:** Load raw data from `data/raw/online_sales_dataset.csv`
2.  **Cleaning:**
    *   Handle missing values
    *   Remove duplicates
    *   Convert `InvoiceDate` to datetime
    *   Filter invalid values (Quantity ≤ 0, UnitPrice ≤ 0)
3.  **Feature Engineering:**
    *   Revenue = Quantity × UnitPrice
    *   Return Indicator (based on negative values)
    *   Time-based features (Month, Year)
4.  **Loading:** Save cleaned dataset to `data/processed/cleaned_online_sales.csv`

## 📈 Analysis Workflow

### 📓 Notebooks Breakdown
*   **01_extraction.ipynb:** Data loading and initial inspection
*   **02_cleaning.ipynb:** Data preprocessing and cleaning
*   **03_eda.ipynb:** Exploratory Data Analysis, trends and distributions
*   **04_statistical_analysis.ipynb:** Deeper insights and correlations
*   **05_final_load_prep.ipynb:** Final dataset preparation for dashboarding

### 📊 Key Metrics (KPIs)
*   Total Revenue
*   Total Return Value
*   Return Rate (%)
*   Net Revenue
*   Orders vs Returns Analysis

## 🧠 Key Insights (Typical Findings)
*   Certain product categories have disproportionately high return rates
*   Returns significantly impact net revenue margins
*   Specific regions/customer segments show higher return behavior
*   Data inconsistencies can distort revenue calculations if not cleaned properly

## ▶️ How to Run

### Option 1: Run Notebooks
1.  Open Jupyter Notebook: `jupyter notebook`
2.  Execute notebooks in order: 01 → 02 → 03 → 04 → 05

### Option 2: Run ETL Script
`python scripts/etl_pipeline.py`

## 📖 Documentation
*   `docs/data_dictionary.md` → Column definitions and dataset details

## ⚠️ Limitations
*   Missing customer behavioral data
*   No real-time data (static dataset)
*   Potential sampling bias
*   Limited business context (no logistics or inventory data)

## 🔮 Future Improvements
*   Build ML model to predict returns
*   Integrate real-time data pipeline
*   Add customer segmentation
*   Deploy as a dashboard + API system

## 💡 Why This Project Matters
This project demonstrates:
*   Real-world data cleaning & preprocessing
*   End-to-end analytics pipeline building
*   Strong business understanding of e-commerce metrics
*   Ability to convert raw data → actionable insights

<img width="724" height="434" alt="Screenshot 2026-04-29 at 12 11 20 AM" src="https://github.com/user-attachments/assets/fef554f9-411b-4552-b045-5f95dd74217b" />

