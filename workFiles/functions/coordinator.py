import pandas as pd
from feature_engine.transformation import ReciprocalTransformer
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

from workFiles.functions.helpers import rmse
from workFiles.functions.performanceDecorator import performance_decorator
from workFiles.functions.reciprocalFeatures import ReciprocalFeatures
from workFiles.types import Data_transformed, Data_splitted

predicted_properties = [
    "K_VRH",  # bulk modulus
    "G_VRH",  # shear modulus
    "elastic_anisotropy",
    "poisson_ratio",
]

excluded_columns = predicted_properties + [
    "formula",
    "material_id",
    "structure",
    "composition",
    "composition_oxid",
    "space_group",
]


def extract_data_to_fit(
        table: pd.DataFrame, properties_to_predict=None, properties_to_exclude=None
) -> Data_transformed:
    """
    Extracts and transforms data for model fitting.

    Parameters:
    table (pd.DataFrame): The input dataframe containing features and target properties.
    property_to_predict (str): The name of the property to predict, which will be used as the target variable.
    properties_to_exclude (list, optional): List of column names to exclude from the features. Defaults to a predefined list of excluded columns.

    Returns:
    DataToFit: A named tuple containing transformed feature matrix X and target variable y.

    The function applies a pipeline of transformations on the feature matrix, including PCA for dimensionality reduction,
    polynomial feature expansion, and standard scaling. It outputs the transformed features and the target variable.
    """

    if properties_to_predict is None:
        properties_to_predict = predicted_properties

    if properties_to_exclude is None:
        properties_to_exclude = excluded_columns

    y_true = table[properties_to_predict]
    X_original = table.drop(properties_to_exclude, axis=1)

    pipe = Pipeline(
        [
            ("reciprocalFeatures", ReciprocalFeatures()),
            ("polynomialFeatures", PolynomialFeatures(degree=2)),
            ("standardScaler2", StandardScaler()),
            ("pca", PCA(n_components=0.95)),
        ]
    )

    X_transformed = pipe.fit_transform(X_original)

    # variances = [f"{x:.3f}" for x in pipe.named_steps["pca"].explained_variance_ratio_]
    # print(f"pca variance explained: {variances}")
    print(f"df shape: {X_original.shape}")
    print(f"df transformed shape: {X_transformed.shape}", end="\n\n")

    return Data_transformed(X_transformed, y_true)


@performance_decorator
def fit_model(Model: type, data: Data_splitted, column_name: str, param_grid):
    """
    Perform hyperparameter optimization using GridSearchCV for a given model.

    Parameters:
    Model (type): The class of the model to be used for fitting/optimization.
    data (DataToFit): A named tuple containing the transformed feature matrix X and target variable y.
    columnName (str): The name of the column in y to predict.
    param_grid (dict): A dictionary with hyperparameters names (string) as keys and lists of parameter settings to try as values.

    Returns:
    GridSearchCV: The GridSearchCV object containing the best parameters and the corresponding performance metrics.

    The function prints the model name, target property, and training R-squared and RMSE values.
    """

    X_train, X_test, y_train, y_test = data

    model = Model()

    grid_search = GridSearchCV(
        model,
        param_grid,
        n_jobs=5,
        cv=10,
        scoring="neg_mean_squared_error",
        return_train_score=True,
    )

    grid_search.fit(X_train, y_train)

    r2_test = grid_search.best_estimator_.score(X_test, y_test)
    rmse_test = rmse(y_test, grid_search.best_estimator_.predict(X_test))

    print(f"Model: {model.__class__.__name__}")
    print(f"test R2 = {r2_test:.3f},", end="\t")
    print(f"RMSE = {rmse_test:.3f}")
    print("Best Parameters:", grid_search.best_params_)
    print(f"Best Score: {grid_search.best_score_:.3f}")

    return grid_search
