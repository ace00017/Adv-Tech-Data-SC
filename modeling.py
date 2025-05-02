# data_wrangling.py
# Author: Aldo Poci
# Description: Cleans the Electric Vehicle dataset

import pandas as pd
import numpy as np

def main():
    # Load raw data
    df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

    # Rename columns for consistency
    df.columns = df.columns.str.replace(" ", "_").str.replace("(", "", regex=False).str.replace(")", "", regex=False)

    # Print first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Drop rows with missing essential data
    df = df.dropna(subset=["Model_Year", "Make", "Electric_Vehicle_Type", "Electric_Range", "Base_MSRP"])

    # Fill less critical missing values with placeholder or forward fill
    df = df.fillna(method="ffill")

    # Save cleaned data
    df.to_csv("clean_ev_data.csv", index=False)
    print("\nCleaned data saved to 'clean_ev_data.csv'")


if __name__ == "__main__":
    main()
