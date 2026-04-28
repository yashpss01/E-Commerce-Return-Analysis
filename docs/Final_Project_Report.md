# 📊 E-Commerce Return Analysis — Final Project Report

## 1. Cover Page
**Project Title:** E-Commerce Return Analysis & Revenue Leakage Detection  
**Sector:** E-Commerce / Retail Analytics  
**Institute:** Newton School of Technology  
**Submission Date:** 28/04/2026  

**Team Members & Roles:**
*   **Yash Pratap Singh Solanki**: Project Lead & Data Extraction
*   **Archisman Nath Choudhury**: ETL Pipeline & Data Cleaning
*   **Krish Amit Modi**: Statistical Analysis & Modeling
*   **Ved Bhadani**: Tableau Dashboard Design & Visualization
*   **Akanksha Sharma**: Business Insights & Documentation

**Project Resources:**
*   **GitHub Repository**: [https://github.com/yashpss01/E-Commerce-Return-Analysis](https://github.com/yashpss01/E-Commerce-Return-Analysis)
*   **Tableau Dashboard**: [Tableau Public Link](https://public.tableau.com/app/profile/ved.bhadani/viz/DASHBOARD_17773999460820/Dashboard?publish=yes)

---

## 2. Executive Summary (1 Page)

### Problem
E-commerce businesses are currently grappling with high return rates, which directly impact the bottom line through lost revenue, increased reverse logistics costs, and inventory ties. For many retailers, returns are a "silent killer" of profitability. This project addresses the challenge of quantifying this revenue leakage and identifying the root causes—be it product categories, regional factors, or customer behavior.

### Approach
Our team built a robust data analytics pipeline using **Python (Pandas, NumPy, Scipy)** and **Tableau**. We processed a transactional dataset of 44,804 records, implementing a multi-stage ETL (Extract, Transform, Load) process. This included data cleaning, missing value imputation, and feature engineering to derive metrics like `Revenue` and `IsReturn`. Exploratory Data Analysis (EDA) and Statistical Significance testing were performed to validate hypotheses.

### Key Insights
1.  **Revenue Leakage**: The overall return rate stands at **9.79%**, representing approximately **$3.98 Million** in revenue at risk.
2.  **Category Risk**: **Furniture** and **Stationery** are the highest-risk categories, both exceeding a 10% return rate, while **Electronics** shows the lowest risk.
3.  **Price Sensitivity**: Statistical testing revealed that lower-priced items are significantly more likely to be returned, suggesting potential quality control issues in the budget segment.
4.  **Warehouse Efficiency**: Returns are relatively consistent across warehouses, suggesting that the primary drivers of returns are product-specific rather than logistical.

### Key Recommendations
1.  **Quality Control for High-Risk Categories**: Implement stricter quality checks for Furniture and Stationery items prior to shipping.
2.  **Dynamic Return Policies**: Adjust return windows or restocking fees for low-margin, high-return items to mitigate logistics losses.
3.  **Improved Product Visuals**: High returns in Furniture often stem from "size/fit" issues; integrating AR tools or better dimension guides can reduce these errors.

---

## 3. Sector & Business Context

### Sector Overview
The global E-Commerce sector has seen exponential growth, but with it comes the "Return Epidemic." Unlike brick-and-mortar stores where return rates hover around 8-10%, online retail often sees rates as high as 20-30% in specific segments like fashion.

### The Decision-Maker
This project serves **Operations Managers** and **Inventory Strategists**. They need to decide which products to keep in stock, which suppliers to prioritize, and where to tighten return policies without hurting customer loyalty.

### Business Value
Reducing the return rate by even **1-2%** can save millions in operational costs. This project provides the data-driven foundation to transition from "guessing" why returns happen to "knowing" where the leakage occurs.

---

## 4. Problem Statement & Objectives

### Problem Statement
How can we identify and quantify the primary drivers of product returns to minimize revenue leakage in an e-commerce ecosystem?

### Objectives
*   **Quantify Revenue Loss**: Calculate exactly how much money is lost due to "Cancelled" and "Returned" orders.
*   **Segment Risk**: Identify high-return categories, regions, and customer segments.
*   **Establish an ETL Pipeline**: Create a repeatable process for cleaning messy transactional data.
*   **Interactive Visualization**: Provide stakeholders with a real-time view of business health via Tableau.

---

## 5. Data Description

### Dataset Overview
*   **Source**: Transactional Sales Dataset (CSV format).
*   **Size**: 44,804 rows and 23 initial columns.
*   **Key Features**: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `UnitPrice`, `CustomerID`, `Country`, `Category`.

### Limitations & Bias
*   **Missing Data**: Significant missing values in `CustomerID` (filled with "Guest") and `ShippingCost` (imputed using median).
*   **Temporal Scope**: The data spans specific months; seasonal bias (e.g., holiday returns) may be present.
*   **Data Entry Errors**: Negative quantities and extreme discounts were present, requiring clipping and filtering.

---

## 6. Data Cleaning & ETL Pipeline

### Phase 1: Extraction
Data is loaded from raw CSV files into a Pandas DataFrame.

### Phase 2: Cleaning
1.  **Duplicate Removal**: Removed identical transaction entries.
2.  **Imputation**: 
    *   `ShippingCost`: Imputed with median ($14.96).
    *   `WarehouseAddress`: Filled with "Unknown".
3.  **Filtering**: Removed records with negative `Quantity` or `UnitPrice` to ensure logical consistency.
4.  **Standardization**: Corrected typos in `PaymentMethod` (e.g., merging variations of "Credit Card").

### Phase 3: Feature Engineering
*   **Revenue**: Calculated as `(Quantity * UnitPrice) * (1 - Discount)`.
*   **IsReturn**: A binary flag (1 for "Returned"/"Cancelled", 0 otherwise).
*   **Time Features**: Extracted `OrderMonth`, `DayOfWeek`, and `Hour` from `InvoiceDate`.

---

## 7. KPI & Metric Framework

| Metric | Definition | Current Value |
| :--- | :--- | :--- |
| **Return Rate** | (Total Returns / Total Orders) * 100 | **9.79%** |
| **Gross Revenue** | Sum of all transaction values | **$40.63M** |
| **Revenue at Risk** | Sum of revenue from returned/cancelled orders | **$3.98M** |
| **Average Order Value** | Total Revenue / Total Invoices | **~$907** |

---

## 8. Exploratory Data Analysis (EDA)

### Key Visual Findings
1.  **Category Performance**: Furniture and Stationery have the highest return rates. This suggests these items are either prone to damage during transit or do not meet customer expectations based on online descriptions.
2.  **Monthly Trends**: Revenue shows significant fluctuations, but the return rate remains relatively stable, indicating that returns are a systemic issue rather than a seasonal one.
3.  **Payment Method Impact**: There is no significant difference in return behavior between Credit Card and E-wallet users, suggesting the payment interface is not a friction point for returns.

---

## 9. Statistical Analysis & Insights

### Correlation Analysis
*   **Unit Price**: We found a small but statistically significant negative correlation between Unit Price and Returns. **Lower-priced items have higher return rates.** This suggests that "budget" items may be failing to meet basic quality expectations.
*   **Quantity**: Large bulk orders do not show a higher propensity for returns compared to single-item orders.

### Hypothesis Testing
Using **Chi-Squared tests**, we validated that the `Category` of a product has a significant relationship with its likelihood of being returned (p < 0.05). This confirms that returns are not random but tied to the product type.

---

## 10. Tableau Dashboard Design

The dashboard is designed for executive monitoring.
*   **Top Row**: Summary KPIs (Total Revenue, Return Rate, Revenue at Risk).
*   **Middle Row**: Return Rate by Category (Bar Chart) and Monthly Trend (Line Chart).
*   **Bottom Row**: Regional breakdown and Warehouse performance.
*   **Interactivity**: Users can filter by `Country` and `OrderPriority` to see localized leakage.

---

## 11. Recommendations & Business Impact

1.  **Supplier Audit**: Categories with >10% returns should undergo a supplier audit to check for consistent manufacturing defects.
2.  **Threshold-Based Shipping**: Since shipping costs impact margins, e-commerce managers should consider higher free-shipping thresholds for high-return categories to cover the risk.
3.  **Review Sentiment Analysis**: Integrate customer reviews to identify *why* Stationery/Furniture is being returned (e.g., "Color mismatch").

---

## 12. Contribution Matrix

| Team Member | Sourcing | ETL/Cleaning | EDA | Stats | Tableau | Documentation |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Yash Pratap | P | S | - | - | - | S |
| Archisman | S | P | S | - | - | S |
| Krish | - | - | S | P | - | - |
| Ved | - | - | S | - | P | S |
| Akanksha | - | - | - | - | S | P |

*P = Primary, S = Secondary*

---
