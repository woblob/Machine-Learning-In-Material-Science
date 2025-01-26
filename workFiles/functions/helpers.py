from sklearn.metrics import mean_squared_error
import numpy as np


def rmse(y_true, y_pred):
    """
    Calculate the root mean squared error (RMSE) between true and predicted values.

    Parameters:
    y_true (array-like): Ground truth (correct) target values.
    y_pred (array-like): Estimated target values.

    Returns:
    float: The RMSE value.
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


def calculate_total_time_left(Results):
    """
    Calculate the total time left in minutes for the remaining models to finish training.

    This is calculated by summing the average time taken for each model to complete
    training on each feature. This average is then multiplied by the number of features
    that the model has yet to train on.

    Parameters:
    Results (dict): A dictionary where the keys are the feature names, the values
        are dictionaries where the keys are the model names, and the values are dictionaries
        with the keys "accuracy" and "time_taken".

    Returns:
    float: The total time left in minutes for the remaining models to finish training.
    """
    first_column = list(Results.keys())[0]
    total_time_per_model = {model: [] for model in Results[first_column]}

    for feature in Results:
        for model_name in Results[feature]:
            time_to_add = Results[feature][model_name]["time_taken"]
            if time_to_add is None:
                continue
            total_time_per_model[model_name].append(time_to_add)

    total_time_left = sum(
        (
            np.mean(fit_time) * (len(Results.keys()) - len(fit_time))
            if len(fit_time) > 0
            else 0
        )
        for fit_time in total_time_per_model.values()
    )
    return round(total_time_left, 2)


def count_combinations(element: tuple[type, dict]):
    """
    Count the number of combinations of the given hyperparameters.

    Parameters:
    element (tuple[type, dict]): A tuple containing the model class and a dictionary of its hyperparameters.

    Returns:
    tuple[str, int]: A tuple containing the model name and the number of hyperparameter combinations.
    """
    model, options = element
    model_name = model.__name__
    options_combination = np.prod([len(v) for v in options.values()])
    return model_name, int(options_combination)
