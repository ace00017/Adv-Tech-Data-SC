# modeling.py
# Author: Aldo Poci
# Description: Linear regression model to predict electric vehicle range

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def main():
    # Load the cleaned electric vehicle dataset
    data = pd.read_csv("clean_ev_data.csv")

    # Choose features and the target variable
    X = data[["Model_Year", "Base_MSRP"]]
    y = data["Electric_Range"]

    # Split the dataset into training and testing sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42)

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the electric range using the test set
    y_pred = model.predict(X_test)

    # Evaluate model performance using common metrics
    print("========================")
    print(" Model Performance Metrics")
    print("========================")
    print("Mean Absolute Error (MAE):", round(mean_absolute_error(y_test, y_pred), 2))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error (RMSE):", round(rmse, 2))
    print("R-squared (Coefficient of Determination):", round(r2_score(y_test, y_pred), 4))

    # Save the actual and predicted values to a CSV file
    results = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
    results.to_csv("ev_predictions.csv", index=False)
    # Confirm that predictions were saved
    print("\nPredictions saved to 'ev_predictions.csv'")


if __name__ == "__main__":
    main()
