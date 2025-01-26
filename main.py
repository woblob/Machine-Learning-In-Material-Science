import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge, HuberRegressor, TheilSenRegressor, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR, SVR
from sklearn.tree import DecisionTreeRegressor

from workFiles.functions.coordinator import fit_model, extract_data_to_fit, predicted_properties
from workFiles.functions.getDF import get_df
from workFiles.functions.helpers import calculate_total_time_left, rmse, count_combinations
from workFiles.types import Data_splitted
import joblib


df = get_df()
data = extract_data_to_fit(df, predicted_properties)
models = [
    (LinearRegression, {
        "fit_intercept": [True, False],
        "positive": [True, False]
    }),
    (Lasso, {
        'alpha': [0.001, 0.01, 0.1, 1.0, 10],
        'tol': [0.0001, 0.001, 0.01, 0.1],
        'copy_X': [True]
    }),
    (Ridge, {
        'alpha': [0.001, 0.01, 0.1, 1.0, 10.0, 100],
        'solver': ['svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga'],
        'copy_X': [True],
        'max_iter': [100_000_000],
        'fit_intercept': [True],
    }),
    (ElasticNet, {
        'alpha': [0.001, 0.01, 0.1, 1.0, 10],
        'tol': [0.00001, 0.0001, 0.001, 0.01, 0.1],
        'l1_ratio': [0.1, 0.2, 0.4, 0.6, 0.8, 0.9],
        "fit_intercept": [True],
        'copy_X': [True],
        "selection": ['cyclic', 'random']
    }),
    (HuberRegressor, {
        'max_iter': [10_000],
        'epsilon': [1.0, 1.5, 2.0, 2.5, 3.0],
        'alpha': [0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0],
        'fit_intercept': [True],
    }),
    (LinearSVR, {
        'max_iter': [100_000],
        'loss': ['epsilon_insensitive', 'squared_epsilon_insensitive'],
        'epsilon': [0.0, 0.1, 0.3, 0.6, 1.0, 3.0, 10.0],
        'tol': [1e-04, 1e-03, 1e-02, 1e-01, 1e+00],
    }),
    (TheilSenRegressor, {
        'max_iter': [100],
        'max_subpopulation': [500, 700, 900, 1100],
        'fit_intercept': [True],
        'tol': [1e-05, 1e-04, 1e-03, 1e-02],
    }),
    (DecisionTreeRegressor, {
        'max_depth': [3, 7, 10, 30, 60, 100, 150, 200],
        'min_samples_split': [2, 4, 8, 16, 32],
        'min_samples_leaf': [1, 2, 4, 8],
        'splitter': ['best', 'random'],
    }),
    (RandomForestRegressor, {
        'n_estimators': [50, 75, 100, 150, 200],
        'max_leaf_nodes': [32, 64, 128, 256],
        'max_depth': [3, 9, 27, 81],
        'bootstrap': [True],
    }),
]

model_combinations = {model_name: count for model_name, count in map(count_combinations, models)}
try:
    Results = joblib.load('Results.joblib')
except FileNotFoundError as e:
    print(e)

    Results = {
        column_name: {
            model.__name__: {
                "instance": None,
                "time_taken": None,
                'time_taken_per_run': None,
                'r2': None,
                'rmse': None
            } for (model, _) in models
        }
        for column_name in data.y
    }

for i, column_name in enumerate(data.y):
    X_train, X_test, y_train, y_test = train_test_split(
        data.X, data.y[column_name], test_size=0.1, random_state=1234
    )
    data_split = Data_splitted(X_train, X_test, y_train, y_test)

    print(f"Property {i}: {column_name}")
    for j, (model, options) in enumerate(models):
        if Results[column_name][model.__name__]["instance"] is not None:
            continue
        print(model.__name__, i, j)

        model_instance, time_taken = fit_model(model, data_split, options)

        Results[column_name][model.__name__]["instance"] = model_instance.instance
        Results[column_name][model.__name__]["r2"] = model_instance.r2_test
        Results[column_name][model.__name__]["rmse"] = model_instance.rmse_test

        time_taken_per_run = time_taken / model_combinations[model.__name__]
        Results[column_name][model.__name__]["time_taken_per_run"] = time_taken_per_run
        Results[column_name][model.__name__]["time_taken"] = time_taken

        print(f"Time taken: {time_taken:.2f}[min]")
        print(f"Time per run: {time_taken_per_run:.2f}[min]", end="\n\n")
        print(f"Estimated Time Left: {calculate_total_time_left(Results):.2f}[min]")

        joblib.dump(Results, 'Results.joblib')


total_time = 0
for el in Results:
    for model in Results[el]:
        time_taken = Results[el][model]['time_taken']
        total_time += time_taken or 0

print(f'{round(total_time, 1)}[min]')
print(f'{round(total_time / 60, 1)}[h]')
for feature in Results:
    X_train, X_test, y_train, y_test = train_test_split(
        data.X, data.y[feature], test_size=0.1, random_state=1234
    )
    print()
    print(feature)
    print()
    for model in Results[feature]:
        fitted_model = Results[feature][model]['instance']

        if fitted_model is None:
            break

        r2_test = round(fitted_model.best_estimator_.score(X_test, y_test), 3)
        rmse_test = round(rmse(y_test, fitted_model.best_estimator_.predict(X_test)), 3)

        print(f'{model=}')
        print(f'R2: {r2_test}', end=", ")
        print(f"Time: {Results[feature][model]['time_taken']:.2f}[min]", rmse_test, sep=",\t")
        print(f"Best params: {fitted_model.best_params_}", end="\n\n")

