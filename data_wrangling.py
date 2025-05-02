# data_wrangling.py
# Author: Aldo Poci
# Description: This script loads and cleans the Electric Vehicle dataset for use in visualizations and modeling.

import pandas as pd

# Load the original dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

print("============================")
print(" Preview of Raw Dataset ")
print("============================")
print(df.head())
print(f"\nDataset contains {df.shape[0]:,} rows and {df.shape[1]} columns.")

# Clean up the column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

print("\n============================")
print(" Dataset Info Before Cleaning ")
print("============================")
df.info()

print("\n============================")
print(" Missing Values Per Column ")
print("============================")
print(df.isnull().sum())

# Drop any unnecessary columns
df = df.drop(columns=['VIN_1_10'], errors='ignore')

# Drop rows missing critical values
df = df.dropna(subset=['Model_Year', 'Make', 'Electric_Vehicle_Type'])

# Convert columns to numeric types
df['Model_Year'] = pd.to_numeric(df['Model_Year'], errors='coerce')
df['Electric_Range'] = pd.to_numeric(df['Electric_Range'], errors='coerce')

# Filter out rows with 0 or missing Electric Range (if applicable)
if 'Electric_Range' in df.columns:
    df = df[df['Electric_Range'] > 0]

# Save the cleaned dataset
output_file = "clean_ev_data.csv"
df.to_csv(output_file, index=False)

print("\n============================")
print(" Cleaned data saved ✅")
print(f" File: {output_file}")
print("============================")
