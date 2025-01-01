import pandas as pd
import joblib

from matminer.datasets.convenience_loaders import load_elastic_tensor
from matminer.featurizers.conversions import StrToComposition, CompositionToOxidComposition
from matminer.featurizers.composition import ElementProperty, OxidationStates
from matminer.featurizers.structure import DensityFeatures

from workFiles.functions.performanceDecorator import performance_decorator


@performance_decorator
def get_full_dataframe() -> pd.DataFrame:
    """
    Get a pandas DataFrame containing the elastic tensor data from
    "Charting the complete elastic properties of inorganic crystalline compounds",
    M. de Jong *et al.*, Sci. Data. 2 (2015) 150009, with additional features
    computed by the following featurizers:
        - StrToComposition: convert formula to composition
        - ElementProperty.from_preset("magpie"): compute elemental properties
        - CompositionToOxidComposition: convert composition to oxidation state composition
        - OxidationStates: compute oxidation states
        - DensityFeatures: compute density features

    :return: pandas DataFrame
    """
    df = load_elastic_tensor()

    unwanted_columns = ["volume", "nsites", "compliance_tensor", "elastic_tensor",
                        "elastic_tensor_original", "K_Voigt", "G_Voigt", "K_Reuss", "G_Reuss"]
    df.drop(unwanted_columns, axis=1, inplace=True)
    df = StrToComposition().featurize_dataframe(df, "formula")
    df = ElementProperty.from_preset(preset_name="magpie", impute_nan=True).featurize_dataframe(df, col_id="composition")
    df = CompositionToOxidComposition().featurize_dataframe(df, "composition")
    df = OxidationStates().featurize_dataframe(df, "composition_oxid")
    df = DensityFeatures().featurize_dataframe(df, "structure")

    return df


def get_df(filename=None) -> pd.DataFrame:
    """
    Load a pandas DataFrame containing the elastic tensor data

    If a filename is given, this function will attempt to load the DataFrame
    from the file. If the file does not exist, this function will compute the
    DataFrame from scratch, save it to the given filename, and then return it.

    :param filename: (optional) the filename to load the DataFrame from, or to
        save it to if it is not already present
    :return: pandas DataFrame
    """
    if filename is None:
        filename = 'df.joblib'

    df = None
    try:
        df = joblib.load(filename)
    except FileNotFoundError as e:
        print(e)

        df = get_full_dataframe()

        joblib.dump(df, filename)

    if df is None:
        raise Exception("df is still None")

    return df