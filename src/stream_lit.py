import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=118, value=35)
weight = st.number_input("Weight (kg)", min_value=1, value=70)
height = st.number_input(
    "Height (m)",
    min_value=1.0,
    max_value=2.5,
    value=1.75,
)
income_lpa = st.number_input(
    "Annual income (LPA)",
    min_value=0.1,
    value=25.0,
)
smoker = st.selectbox(
    "Are you a smoker?",
    options=[True, False],
)
city = st.selectbox("City", ["urban", "semi-urban", "rural"])
occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job",
    ],
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post(
            API_URL,
            json=input_data,
            timeout=30,
        )

        # Show useful information if the API returns an error
        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
            st.code(response.text or "The API returned an empty response.")
            st.stop()

        # Confirm that the successful response is JSON
        content_type = response.headers.get("content-type", "")

        if "application/json" not in content_type.lower():
            st.error("The API did not return JSON.")
            st.code(response.text or "The API returned an empty response.")
            st.stop()

        result = response.json()

        if "predicted_category" not in result:
            st.error("The API response does not contain the 'predicted_category.")
            st.json(result)
            st.stop()

        prediction = result["predicted_category"]

        st.success(f"Predicted Insurance Premium Category: **{prediction}**")

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the FastAPI server. Start FastAPI on port 8000 first."
        )

    except requests.exceptions.Timeout:
        st.error("The FastAPI request timed out.")

    except requests.exceptions.JSONDecodeError:
        st.error("The API response could not be decoded as JSON.")
        st.code(response.text or "The API returned an empty response.")

    except KeyError as error:
        st.error(f"Expected response field is missing: {error}")

    except requests.exceptions.RequestException as error:
        st.error(f"API request failed: {error}")
