🏥 Insurance Premium Prediction App
An end‑to‑end machine learning application that predicts insurance premiums using am ML model, with a Streamlit frontend, FastAPI backend, and PostgreSQL database.
The project demonstrates a full ML workflow from data ingestion to model deployment and interactive inference.

🚀 Features

✅ Trains a Random Forest Classifier on insurance data
✅ Interactive Streamlit UI for user input
✅ FastAPI REST API for model inference
✅ PostgreSQL integration for structured data storage
✅ CSV‑based dataset ingestion
✅ Model serialization using pickle
✅ Request validation using Pydantic
✅ Swagger documentation (/docs)


🧠 Tech Stack
Language: Python
Machine Learning: scikit‑learn
Backend: FastAPI, Uvicorn
Frontend: Streamlit
Database: PostgreSQL
Data Handling: pandas, NumPy
Model Persistence: pickle
API Client: requests

🏗️ System Architecture
┌──────────────┐
│  Streamlit   │  ← User Interface
│   Frontend   │
└──────┬───────┘
       │ POST /predict
       ▼
┌──────────────┐
│   FastAPI    │  ← Model Inference API
│   Backend    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│      ML      │  ← Trained ML Model
│   Classifier │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ PostgreSQL   │  ← Data Storage
└──────────────┘


📂 Project Structure
insurance-premium-prediction-app/
│
├── data/
│   └── insurance.csv
│
├── model/
│   └── model.pkl
│
├── backend/
│   └── insurance_api.py
│
├── frontend/
│   └── stream_lit.py
│
├── requirements.txt
├── README.md
└── .gitignore


▶️ Running the Application
✅ Start FastAPI Backend
Shelluvicorn insurance_api:app --reload``Show more lines
Backend will start at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs


✅ Start Streamlit Frontend (new terminal)
Shellstreamlit run stream_lit.pyShow more lines
Streamlit app will open at:
http://localhost:8501


🔌 API Endpoint
POST /predict
Request Body (JSON):
JSON{  "age": 38,  "height": 1.2,  "weight": 70,  "smoker": 1,  "city": "Prague"}Show more lines
Response:
JSON{  "predicted_premium": 12456}``Show more lines

✅ Example Prediction Flow
1️⃣ User enters details in Streamlit UI
2️⃣ Streamlit sends POST request to FastAPI
3️⃣ FastAPI validates input and loads model
4️⃣ Model predicts insurance premium
5️⃣ Result is displayed in the UI

📝 Key Learnings

Deploying ML models using REST APIs
Frontend–backend communication using HTTP
Handling schema validation with Pydantic
Avoiding common deployment pitfalls (pickle, environment mismatches)
Building production‑style ML applications


🔮 Future Improvements

Dockerization
Cloud deployment (AWS / Azure)
Model monitoring & logging
Authentication & authorization
CI/CD pipeline
Feature importance visualization


📌 Author
Avneesh Kumar
Machine Learning & Data Science Enthusiast
