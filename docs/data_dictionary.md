# Data Dictionary — Online Sales Dataset

**Source:** [Online Sales Dataset — Kaggle](https://www.kaggle.com/datasets/yusufdelikkaya/online-sales-dataset)

## Raw Columns (`data/raw/online_sales_dataset.csv`)

| # | Column | Type | Description |
|---|--------|------|-------------|
| 1 | `InvoiceNo` | String | Unique invoice/transaction identifier |
| 2 | `StockCode` | String | Product code (SKU) |
| 3 | `Description` | String | Product name/description |
| 4 | `Quantity` | Integer | Number of units purchased (negative = cancellation) |
| 5 | `InvoiceDate` | Datetime | Date and time of the transaction |
| 6 | `UnitPrice` | Float | Price per unit in currency |
| 7 | `CustomerID` | Float/Int | Unique customer identifier (may have missing values) |
| 8 | `Country` | String | Customer's country |
| 9 | `Discount` | Float | Discount applied (0–1 scale; >1 = data error) |
| 10 | `PaymentMethod` | String | Payment method (Credit Card, Bank Transfer, PayPal) |
| 11 | `ShippingCost` | Float | Shipping cost for the order |
| 12 | `Category` | String | Product category (Electronics, Apparel, Furniture, etc.) |
| 13 | `SalesChannel` | String | Online or In-store |
| 14 | `ReturnStatus` | String | `Returned` or `Not Returned` — **target variable** |
| 15 | `ShipmentProvider` | String | Shipping carrier (UPS, FedEx, DHL, Royal Mail) |
| 16 | `WarehouseLocation` | String | Warehouse city (London, Paris, Berlin, etc.) |
| 17 | `OrderPriority` | String | Order priority level (Low, Medium, High) |

## Engineered Columns (added in `02_cleaning.ipynb`)

| Column | Type | Description |
|--------|------|-------------|
| `Revenue` | Float | `Quantity × UnitPrice × (1 - Discount)` |
| `IsReturn` | Integer | 1 if `ReturnStatus == Returned`, else 0 |
| `OrderMonth` | Integer | Month extracted from `InvoiceDate` (1–12) |
| `OrderYear` | Integer | Year extracted from `InvoiceDate` |
| `OrderDayOfWeek` | String | Day name (Monday–Sunday) |
| `OrderHour` | Integer | Hour extracted from `InvoiceDate` (0–23) |

## Data Quality Notes

- **Missing values:** `CustomerID`, `ShippingCost`, `WarehouseLocation` have nulls in raw data
- **Negative quantities:** Represent cancellations/adjustments — removed during cleaning
- **PaymentMethod typo:** `paypall` corrected to `PayPal`
- **Discount outliers:** Values >1 clipped to 1.0 during cleaning
