# Adv-Tech-Data-SC
# Electric Vehicle Data Analysis Project

File Size was bigger than 25Mb so I could't upload it here
Please access it from the link below
https://catalog.data.gov/dataset/electric-vehicle-population-data

This project uses a public dataset containing electric vehicle registrations across the state of Washington. The original file, `Electric_Vehicle_Population_Data.csv`, includes detailed information about each EV, such as make, model, year, range, MSRP, and more. The goal of this project was to clean the data, explore it visually, and build a simple model to predict the electric driving range of a vehicle based on selected features.

## What I Did

### 1. Data Wrangling (`data_wrangling.py`)

The original CSV had messy column names and missing values in some columns. I cleaned the column headers by removing spaces and special characters and then dropped rows missing critical values like electric range or MSRP. For other missing values, I used forward fill as a basic way to complete the dataset without losing too much information. The cleaned version was saved as `clean_ev_data.csv`.

### 2. Visualization (`plots.ipynb`)

In the notebook, I created several plots to get a better sense of the data. This includes:

* The distribution of electric vehicle types (e.g., BEV vs PHEV)
* Top 10 EV makes (brands) by count
* EV registrations by model year
* Average electric range by vehicle type
* Top 10 cities with the most EVs

These visuals helped reveal interesting trends, like how certain brands dominate the market or how newer model years tend to have greater electric range.

### 3. Modeling (`modeling.py`)

For the model, I used linear regression to predict the electric driving range of a vehicle using just its model year and base MSRP. These two were chosen because they’re simple numeric features that make sense logically — newer cars and more expensive models are expected to go farther. I trained and tested the model using an 80/20 split and evaluated its performance using mean absolute error, root mean squared error, and R-squared score. The final results showed decent accuracy.

The model’s predictions were saved to a file called `ev_predictions.csv`.

---

Overall, this project was a great hands-on way to practice data cleaning, visualization, and simple regression modeling in Python.
