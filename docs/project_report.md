# 📊 E-Commerce Return Analysis — Project Report

## 1. Cover Page
*   **Project Title:** E-Commerce Return Analysis
*   **Sector:** E-Commerce / Retail Analytics
*   **Team Members:** 
    *   Archisman Nath Choudhury
    *   Yash Pratap Singh Solanki
    *   Krish Amit Modi
    *   Ved Bhadani
    *   Akanksha Sharma
*   **Institute:** Newton School of Technology
*   **GitHub Repository:** [https://github.com/yashpss01/E-Commerce-Return-Analysis](https://github.com/yashpss01/E-Commerce-Return-Analysis)
*   **Tableau Dashboard:** [https://public.tableau.com/app/profile/ved.bhadani/viz/DASHBOARD_17773999460820/Dashboard?publish=yes](https://public.tableau.com/app/profile/ved.bhadani/viz/DASHBOARD_17773999460820/Dashboard?publish=yes)
*   **Submission Date:** 28/04/2026

---

## 2. Executive Summary
### Problem
E-commerce businesses face high return rates, leading to revenue loss, increased logistics cost, and poor customer experience. Understanding the drivers behind product returns is critical for improving profitability.

### Approach
Data was processed using Python for cleaning, transformation, and analysis. Exploratory Data Analysis (EDA) and statistical techniques were applied to uncover patterns. Insights were visualized using Tableau dashboards for decision-making.

### Key Insights
*   Certain product categories show significantly higher return rates.
*   Returns are influenced by factors like region, price range, and product type.
*   Specific customer segments contribute disproportionately to returns.
*   Seasonal trends affect return frequency.

### Key Recommendations
*   Improve product descriptions and quality checks in high-return categories.
*   Optimize logistics and return policies region-wise.
*   Implement predictive return risk models.

---

## 3. Sector & Business Context
The e-commerce sector has grown rapidly, but return rates remain a major challenge (often 20–40% in some categories).

*   **Decision Maker:** Operations Managers, Supply Chain Heads, Product Managers
*   **Why this problem:** Returns directly impact profit margins and operational efficiency.
*   **Business Value:** Reducing returns improves margins, customer satisfaction, and logistics efficiency.

---

## 4. Problem Statement & Objectives
### Problem Statement
Identify patterns and root causes behind product returns in an e-commerce dataset.

### Objectives
*   Analyze return trends
*   Identify high-risk categories/products
*   Understand customer and regional behavior
*   Provide actionable recommendations

### Scope
*   **In Scope:** Data analysis, visualization, insights
*   **Out of Scope:** Real-time system deployment

### Success Criteria
*   Clear identification of return drivers
*   Actionable business insights

---

## 5. Data Description
*   **Dataset Source:** [Kaggle - Online Retail Dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
*   **Structure:**
    *   **Rows:** 44,000+
    *   **Columns:** 23
*   **Key Fields:**
    *   `InvoiceNo` (Order ID) – Unique transaction identifier
    *   `Category` (Product Category) – Used to identify high-return segments
    *   `ReturnStatus` / `IsReturn` – Indicates whether an order was returned (core variable)
    *   `UnitPrice` (Price) – Helps analyze price vs return behavior
    *   `Country` (Region) – Enables geographic return analysis
    *   `CustomerID` (Customer Segment Proxy) – Used for customer-level patterns

### Limitations
*   **Missing Values:** Some fields (e.g., CustomerID) may be incomplete
*   **Limited Customer Behavior Data:** No insights into intent, reviews, or satisfaction
*   **No Return Reason:** Cannot directly determine why products were returned
*   **Possible Sampling Bias:** Dataset may not represent all regions or categories equally

---

## 6. Data Cleaning & ETL Pipeline
Performed in Python:
*   Handled missing values using imputation/removal
*   Removed duplicates
*   Standardized categorical values
*   Converted data types
*   Created new features: Return Rate, Price Buckets

### Assumptions
*   Missing values treated as non-critical unless affecting key metrics

---

## 7. KPI & Metric Framework
*   **Return Rate** = Returned Orders / Total Orders
*   **Category Return Rate**
*   **Revenue Loss due to Returns**
*   **Region-wise Return Rate**

### Why KPIs matter
They directly map to profitability and operational efficiency.

---

## 8. Exploratory Data Analysis (EDA)
*   **Trend Analysis:** Returns vary across time periods
*   **Comparison Analysis:** Some categories have significantly higher returns
*   **Distribution Analysis:** Price distribution shows correlation with returns
*   **Correlation Insights:** Higher-priced items may have higher return probability
*   **Business Insight Example:** High return rates in a category indicate potential product quality or expectation mismatch.

---

## 9. Statistical Analysis
*   Segmentation of customers based on return behavior
*   Identification of high-risk product clusters
*   Root cause analysis for returns

---

## 10. Tableau Dashboard Design
*   **Objective:** Provide an interactive view of return patterns for decision-makers
*   **Features:**
    *   Filters by category, region, and time
    *   KPI summary dashboard
    *   Drill-down views

---

## 11. Insights Summary
*   Certain categories drive majority of returns
*   High-priced products show higher return likelihood
*   Specific regions have higher return rates
*   Customer segments behave differently
*   Seasonal spikes in returns observed
*   Logistics inefficiencies contribute to returns
*   Product mismatch is a key factor
*   Return-heavy SKUs can be identified

---

## 12. Recommendations
1.  **Category Optimization:** Improve quality control, better product descriptions. 
    *   **Impact:** Reduced return rate
2.  **Region-Specific Strategy:** Optimize delivery and packaging.
    *   **Impact:** Lower logistics costs
3.  **Predictive Analytics:** Build return prediction models.
    *   **Impact:** Proactive risk reduction

---

## 13. Impact Estimation
*   5–10% reduction in return rate → significant cost savings
*   Improved logistics efficiency → lower operational cost
*   Better product quality → increased customer satisfaction

---

## 14. Limitations
*   Limited dataset scope
*   No real-time data
*   Lack of detailed customer behavior

---

## 15. Future Scope
*   Build ML model for return prediction
*   Integrate real-time dashboards
*   Add customer review sentiment analysis

---

## 16. Conclusion
This project analyzed e-commerce return data to identify key drivers of returns. Using data cleaning, EDA, and visualization, actionable insights were generated. Implementing the recommendations can significantly reduce return rates and improve profitability.

---

## 17. Appendix

---

## 18. Contribution Matrix

| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Yash Pratap Singh Solanki** | ✅ | | ✅ | | | | ✅ |
| **Archisman Nath Choudhury** | ✅ | | | | ✅ | | ✅ | ✅ |
| **Ved Bhadani** | ✅ | | ✅ | | | | ✅ |
| **Akanksha Sharma** | ✅ | | | | | ✅ | ✅ | ✅ |
| **Krish Amit Modi** | ✅ | ✅ | | ✅ | | | ✅ | |
