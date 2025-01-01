from collections import namedtuple

import pandas as pd

from sklearn.decomposition import PCA

from workFiles.functions.helpers import rmse
from workFiles.functions.performanceDecorator import performance_decorator

properties_to_predict = [
    "K_VRH", # bulk modulus
    "G_VRH", # shear modulus
    "elastic_anisotropy",
    "poisson_ratio"
]

excluded_columns = (
    properties_to_predict +
    [
        "formula",
        "material_id",
        "structure",
        "composition",
        "composition_oxid"
    ]
)
# n_estimators=50, random_state=1
DataToFit = namedtuple("Data", ["name","X", "y"])

def extract_data_to_fit(
        table: pd.DataFrame,
        property_to_predict: str ,
        properties_to_exclude=None
) -> DataToFit:
    """
    Extracts features and target variable from a DataFrame for model fitting.

    Parameters:
    table (pd.DataFrame): The input data containing features and the target property.
    property_to_predict (str): The name of the column in the DataFrame to be used as the target variable.

    Returns:
    DataToFit: A named tuple containing rest of the features X and the target y.
    """
    if properties_to_exclude is None:
        properties_to_exclude = excluded_columns

    y_true = table[property_to_predict].values
    X = table.drop(properties_to_exclude, axis=1)
    return DataToFit(property_to_predict, X, y_true)


@performance_decorator
def fit_model(Model: type, data: DataToFit, options=None):
    """
    Fits a model using the provided data and model class.

    Parameters:
    Model (type): The class of the model to be used for fitting.
    data (DataToFit): A named tuple containing the features X and target y.
    options (dict, optional): Optional parameters to be passed to the model's constructor.

    Returns:
    model: The fitted model.

    The function prints the model name, target property, and training R-squared and RMSE values.
    """

    model = None
    if options is not None:
        model = Model(**options)
    else:
        model = Model()

    X, y = data.X, data.y

    # X_decomposed = PCA(n_components=0.95).fit_transform(X)
    X_decomposed = X

    model.fit(X_decomposed, y)

    r2_training = model.score(X_decomposed, y)
    rmse_training = rmse(y, model.predict(X_decomposed))

    print(f"Model: {model.__class__.__name__}")
    print(f"Property: {data.name}")
    print(f'training R2 = {r2_training:.3f},', end='\t')
    print(f'RMSE = {rmse_training:.3f}', end='\n\n')

    return model

    # from sklearn.linear_model import HuberRegressor
    # HuberRegressor