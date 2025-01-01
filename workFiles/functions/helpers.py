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