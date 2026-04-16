import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title('Insurance Premium Category Predictor')
st.markdown('Enter your details below:')

# Input fields 
age = st.number_input('Age', min_value= 1, max_value= 118, value=35)
weight = st.number_input('Weight (kg)', min_value= 1, value=70)
height =st.number_input('Height (m)', min_value= 1.0, max_value= 2.5, value=1.25)
income_lpa = st.number_input('Annual income (LPA)', min_value= 0.1, value=25.0)
smoker = st.selectbox('Are you a smoker ?', options=[True, False])
city = st.text_input('City', value='Delhi')
occupation = st.selectbox('Occupation', ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium Category"):
    input_data = {"age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation}
    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "response" in result:
            prediction = result["response"]
            st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
            st.write("🔍 Confidence:", prediction["confidence"])
            st.write("📊 Class Probabilities:")
            st.json(prediction["class_probabilities"])

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")