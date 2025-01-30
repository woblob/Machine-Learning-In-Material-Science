import os
from dotenv import load_dotenv
from mp_api.client import MPRester
from emmet.core.summary import HasProps
import pandas as pd
import joblib

from workFiles.functions.field_names import (
    fields_for_request,
    fields_to_drop,
    all_fields,
)

load_dotenv()
API_KEY = os.getenv("API_KEY")
modulus_limit = 1000


def _mp_data_unpack(ser: pd.Series) -> pd.Series:
    return ser.map(lambda x: x[1])


def _mp_data_modulus_cleaning(dictionary: dict) -> float | None:
    vrh_value = dictionary.get("vrh")

    if (vrh_value is not None) and 0 < vrh_value < modulus_limit:
        return vrh_value

    return None


def _mp_data_anisotropy_cleaning(value: float | None) -> float | None:
    if value is None or not (0 < value < 3):
        return None
    return value


def download_data_from_mp(filename: str = None) -> pd.DataFrame:
    if filename is not None:
        try:
            df = joblib.load(filename)
            print(f"Loaded {len(df)} records from {filename}")
            return df
        except FileNotFoundError as e:
            print(e)

    with MPRester(API_KEY) as mpr:
        docs = mpr.materials.summary.search(
            theoretical=False,
            is_stable=True,
            has_props=[HasProps.elasticity],
            fields=fields_for_request,
        )

    print(f"Got {len(docs)} records")

    df = pd.DataFrame(docs, columns=all_fields)
    df.drop(fields_to_drop, axis=1, inplace=True)
    df = df.transform(_mp_data_unpack, axis=0)
    df.set_index("material_id", inplace=True)
    df.dropna(axis=0, how="any", inplace=True)
    df["bulk_modulus"] = df["bulk_modulus"].transform(_mp_data_modulus_cleaning)
    df["shear_modulus"] = df["shear_modulus"].transform(_mp_data_modulus_cleaning)
    df["universal_anisotropy"] = df["universal_anisotropy"].transform(
        _mp_data_anisotropy_cleaning
    )
    df.dropna(axis=0, how="any", inplace=True)

    joblib.dump(df, filename)

    print(f"Dropped {len(docs) - len(df)} records")

    return df
