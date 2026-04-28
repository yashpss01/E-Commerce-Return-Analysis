"""
ETL Pipeline — E-Commerce Return Analysis
==========================================
Standalone script version of the cleaning pipeline (02_cleaning.ipynb).

Usage:
    python scripts/etl_pipeline.py

Input:  data/raw/online_sales_dataset.csv
Output: data/processed/cleaned_online_sales.csv
"""

import pandas as pd
import numpy as np
import os

# ── Paths ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'online_sales_dataset.csv')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
PROCESSED_PATH = os.path.join(PROCESSED_DIR, 'cleaned_online_sales.csv')


def load_data(path: str) -> pd.DataFrame:
    """Load raw CSV."""
    df = pd.read_csv(path)
    print(f'[LOAD] {df.shape[0]:,} rows, {df.shape[1]} columns')
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    print(f'[DEDUP] Removed {before - len(df):,} duplicates  ({before:,} -> {len(df):,})')
    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values."""
    # Drop rows without CustomerID
    before = len(df)
    df = df.dropna(subset=['CustomerID'])
    print(f'[MISSING] Dropped {before - len(df):,} rows with missing CustomerID')

    # Fill ShippingCost with median
    median_ship = df['ShippingCost'].median()
    filled = df['ShippingCost'].isnull().sum()
    df['ShippingCost'] = df['ShippingCost'].fillna(median_ship)
    print(f'[MISSING] Filled {filled:,} ShippingCost with median ({median_ship:.2f})')

    # Fill WarehouseLocation with 'Unknown'
    filled = df['WarehouseLocation'].isnull().sum()
    df['WarehouseLocation'] = df['WarehouseLocation'].fillna('Unknown')
    print(f'[MISSING] Filled {filled:,} WarehouseLocation with "Unknown"')

    return df


def remove_negative_qty(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with negative or zero quantity."""
    before = len(df)
    df = df[df['Quantity'] > 0].copy()
    print(f'[FILTER] Removed {before - len(df):,} negative/zero quantity rows')
    return df


def fix_inconsistencies(df: pd.DataFrame) -> pd.DataFrame:
    """Fix typos, standardise text, clip values."""
    df['PaymentMethod'] = df['PaymentMethod'].replace({'paypall': 'PayPal'})
    df['ReturnStatus'] = df['ReturnStatus'].str.strip().str.title()
    df['Discount'] = df['Discount'].clip(0, 1)
    print('[FIX] PaymentMethod typo fixed, ReturnStatus standardised, Discount clipped')
    return df


def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert data types."""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int)
    print('[TYPES] InvoiceDate -> datetime, CustomerID -> int')
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add derived columns."""
    df['Revenue'] = (df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])).round(2)
    df['IsReturn'] = (df['ReturnStatus'] == 'Returned').astype(int)
    df['OrderMonth'] = df['InvoiceDate'].dt.month
    df['OrderYear'] = df['InvoiceDate'].dt.year
    df['OrderDayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['OrderHour'] = df['InvoiceDate'].dt.hour
    print('[FEATURES] Added Revenue, IsReturn, OrderMonth, OrderYear, OrderDayOfWeek, OrderHour')
    return df


def save_data(df: pd.DataFrame, path: str) -> None:
    """Save cleaned DataFrame to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f'[SAVE] {path}  ({os.path.getsize(path) / 1e6:.2f} MB)')


def run_pipeline():
    """Execute the full ETL pipeline."""
    print('=' * 60)
    print('E-Commerce Return Analysis — ETL Pipeline')
    print('=' * 60)

    df = load_data(RAW_PATH)
    df = remove_duplicates(df)
    df = handle_missing(df)
    df = remove_negative_qty(df)
    df = fix_inconsistencies(df)
    df = convert_types(df)
    df = engineer_features(df)

    print(f'\n[FINAL] {df.shape[0]:,} rows, {df.shape[1]} columns')
    print(f'[FINAL] Return rate: {df["IsReturn"].mean()*100:.2f}%')

    save_data(df, PROCESSED_PATH)
    print('\nPipeline complete.')


if __name__ == '__main__':
    run_pipeline()
