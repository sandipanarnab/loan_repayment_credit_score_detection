import joblib
import pandas as pd
import json


# ------------------------------------------------
# LOAD ARTEFACTS
# ------------------------------------------------

model = joblib.load(
    "artefacts/logistic_model.pkl"
)

scaler = joblib.load(
    "artefacts/scaler.pkl"
)

woe_table = pd.read_csv(
    "artefacts/woe_table.csv"
)

with open(
    "artefacts/model_metadata.json",
    "r"
) as f:

    metadata = json.load(f)


model_features = metadata["model_features"]


# ------------------------------------------------
# BUILD WOE TABLES
# ------------------------------------------------

def build_woe_maps(df):

    woe_maps = {}

    for variable in df["VAR_NAME"].unique():

        temp = df[
            df["VAR_NAME"] == variable
        ]

        woe_maps[variable] = temp

    return woe_maps


woe_maps = build_woe_maps(
    woe_table
)


# ------------------------------------------------
# GET WOE VALUE
# ------------------------------------------------

def get_woe_value(value, variable_df):

    value = str(value)

    # --------------------------------------------
    # CATEGORICAL VARIABLES
    # --------------------------------------------

    for _, row in variable_df.iterrows():

        min_val = str(row["MIN_VALUE"])
        max_val = str(row["MAX_VALUE"])

        # category match
        if min_val == max_val:

            if value == min_val:
                return row["WOE"]

    # --------------------------------------------
    # NUMERICAL VARIABLES
    # --------------------------------------------

    try:

        numeric_value = float(value)

        for _, row in variable_df.iterrows():

            try:

                min_val = float(row["MIN_VALUE"])
                max_val = float(row["MAX_VALUE"])

                if min_val <= numeric_value <= max_val:
                    return row["WOE"]

            except:
                continue

    except:
        pass

    return 0


# ------------------------------------------------
# APPLY WOE TRANSFORMATION
# ------------------------------------------------

def apply_woe(df):

    transformed = pd.DataFrame()

    for variable in woe_maps:

        if variable in df.columns:

            variable_df = woe_maps[variable]

            woe_value = get_woe_value(
                df[variable].iloc[0],
                variable_df
            )

            transformed[
                f"new_{variable}"
            ] = [woe_value]

    return transformed


# ------------------------------------------------
# MAIN PREDICTION FUNCTION
# ------------------------------------------------

def predict_loan(data):

    # raw dictionary → dataframe
    df = pd.DataFrame([data])

    # apply WOE
    transformed_df = apply_woe(df)

    # ensure exact feature order
    transformed_df = transformed_df.reindex(
        columns=model_features,
        fill_value=0
    )

    print("\nTRANSFORMED DATAFRAME:")
    print(transformed_df)

    # scaling
    scaled = scaler.transform(
        transformed_df
    )

    # prediction
    prediction = model.predict(
        scaled
    )[0]

    # probability
    probability = model.predict_proba(
        scaled
    )[0][1]

    return {

        "prediction": int(prediction),

        "default_probability": float(
            probability
        )
    }