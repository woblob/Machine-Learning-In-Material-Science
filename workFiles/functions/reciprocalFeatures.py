import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class ReciprocalFeatures(BaseEstimator, TransformerMixin):
    """Transformer to create new features as reciprocal of given columns.

    Parameters
    ----------
    columns_to_drop : list, optional
        List of column names which should be excluded from the transformation.
        If a column name is included in this list, it will be ignored and not
        transformed. This can be useful if you want to keep the original column
        but also include a reciprocal transformation of the same column in the
        output.

        The default is None.

    Attributes
    ----------
    _columns_to_transform : list
        List of column names which will be transformed.

    Examples
    --------
    >>> df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    >>> ReciprocalFeatures().fit_transform(df)
       a  b  a_inv  b_inv
    0  1  4    1.0   0.25
    1  2  5    0.5   0.20
    2  3  6    0.3   0.17

    >>> df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    >>> ReciprocalFeatures(columns_to_drop=["a"]).fit_transform(df)
       a  b  b_inv
    0  1  4    0.25
    1  2  5    0.20
    2  3  6    0.17
    """

    def __init__(self, columns_to_drop: list = None, *args, **kwargs):
        self.columns_to_drop = columns_to_drop
        self._columns_to_transform = []

    def fit(self, X: pd.DataFrame, y=None):
        # mask = X != 0
        # nonZeroTable = X[mask]
        # wholeColumnsMask = nonZeroTable.all(axis=1)
        # droppedZeroTable = nonZeroTable[wholeColumnsMask]
        # onlyNumbers = droppedZeroTable.select_dtypes(include=[np.number])
        # invertible_data = onlyNumbers
        invertible_data = X[X != 0].dropna(axis=1).select_dtypes(include=[np.number])

        if self.columns_to_drop is not None and len(self.columns_to_drop) > 0:
            invertible_data = invertible_data.drop(self.columns_to_drop, axis=1)

        self._columns_to_transform = invertible_data.columns.tolist()

        return self

    def transform(self, X: pd.DataFrame):
        X_copy = X.copy()

        for col in self._columns_to_transform:
            X_copy[f"{col}_inv"] = 1 / X_copy[col]

        return X_copy


if __name__ == "__main__":
    df = pd.DataFrame({"a": [0], "b": ["a"], "c": [1], "d": [2]})

    print(df)
    print(ReciprocalFeatures().fit_transform(df))
    print(ReciprocalFeatures([]).fit_transform(df))
    print(ReciprocalFeatures(["d"]).fit_transform(df))
