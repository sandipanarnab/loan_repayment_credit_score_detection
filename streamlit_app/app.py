import streamlit as st
import requests


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="XYZ Bank Ltd. - Credit Risk Portal",
    page_icon="🏦",
    layout="centered"
)


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🏦 XYZ Bank Ltd.")
st.subheader("Retail Credit Risk Assessment System")
st.caption("Thane Regional Office")


st.markdown("---")


# ---------------------------------------------------
# APPLICANT DETAILS
# ---------------------------------------------------

st.markdown("## Applicant Financial Details")


col1, col2 = st.columns(2)


with col1:

    dti = st.number_input(
        "Debt-to-Income Ratio (%)",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=0.1,
        help="Percentage of monthly debt obligations to monthly income."
    )

    grade = st.selectbox(
        "Credit Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

    term = st.selectbox(
        "Loan Term",
        ["36 months", "60 months"]
    )

    int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0,
        max_value=40.0,
        value=12.0,
        step=0.1
    )


with col2:

    purpose = st.selectbox(
        "Loan Purpose",
        [
            "debt_consolidation",
            "credit_card",
            "home_improvement",
            "major_purchase",
            "small_business"
        ]
    )

    revol_util = st.number_input(
        "Revolving Utilization (%)",
        min_value=0.0,
        max_value=150.0,
        value=35.0,
        step=0.1,
        help="Credit utilization across revolving accounts."
    )

    issue_d = st.text_input(
        "Issue Date",
        value="Jan-2015",
        help="Format: MMM-YYYY"
    )


st.markdown("---")


# ---------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------

if st.button("Evaluate Applicant Risk"):

    payload = {

        "dti": dti,
        "grade": grade,
        "term": term,
        "int_rate": int_rate,
        "purpose": purpose,
        "revol_util": revol_util,
        "issue_d": issue_d
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        probability = result["default_probability"]

        prediction = result["prediction"]


        # ---------------------------------------------------
        # RESULTS
        # ---------------------------------------------------

        st.markdown("## Risk Assessment Result")

        st.metric(
            label="Default Probability",
            value=f"{probability:.2%}"
        )

        if prediction == 1:

            st.error(
                "Application classified as HIGH RISK"
            )

        else:

            st.success(
                "Application classified as LOW RISK"
            )

    except Exception as e:

        st.error(
            f"Connection Error: {e}"
        )