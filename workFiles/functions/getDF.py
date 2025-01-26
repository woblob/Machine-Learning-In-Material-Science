import pandas as pd
import joblib

from matminer.featurizers.conversions import (
    StrToComposition,
    CompositionToOxidComposition,
)
from matminer.featurizers.composition import ElementProperty, OxidationStates
from matminer.featurizers.structure import DensityFeatures

from workFiles.functions.download_data import download_data_from_mp
from workFiles.functions.performanceDecorator import performance_decorator


def get_full_dataframe(docs: pd.DataFrame) -> pd.DataFrame:
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
    print("Extracting data...")

    df = StrToComposition().featurize_dataframe(docs, "formula_pretty")
    df = ElementProperty.from_preset(
        preset_name="magpie", impute_nan=True
    ).featurize_dataframe(df, col_id="composition")
    df = CompositionToOxidComposition().featurize_dataframe(df, "composition")
    df = OxidationStates().featurize_dataframe(df, "composition_oxid")
    df = DensityFeatures().featurize_dataframe(df, "structure", ignore_errors=True)

    df.dropna(axis=0, how="any", inplace=True)

    print("Data extracted")
    print(f"Removed {len(docs) - len(df)} records")

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
        filename = "outputs/df.joblib"

    df = None
    try:
        df = joblib.load(filename)
        print(f"Loaded full dataframe with {len(df)} records from {filename}")
    except FileNotFoundError as e:
        print(e)

        data = download_data_from_mp("outputs/mp_docs.joblib")
        df = get_full_dataframe(data)

        joblib.dump(df, filename)

    if df is None:
        raise Exception("df is still None")

    return df
