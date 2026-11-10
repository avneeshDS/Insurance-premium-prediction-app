# 🏥 Insurance Premium Category Prediction App

An end-to-end machine-learning application that predicts an **insurance premium category** from demographic, physical, lifestyle, location, income, and occupation-related information.

The application includes:

- A trained scikit-learn classification pipeline
- A FastAPI prediction backend
- A Streamlit web frontend
- Automated CI/CD deployment through GitHub Actions
- Separate frontend and backend deployments on Azure App Service
- Reproducible dependency management using `uv`

---

## 🌐 Live Azure Applications

### Streamlit Web Application

Use the interactive frontend to enter customer information and obtain an insurance premium category prediction:

[Open the Streamlit application](https://streamlitapp-hsf5eug5g0b0emf9.indonesiacentral-01.azurewebsites.net/)

### FastAPI Swagger Documentation

Use the Swagger interface to inspect and test the prediction API:

[Open the FastAPI Swagger interface](https://fastapiinsurance-dkb9f7a2ehbzdxgr.uaenorth-01.azurewebsites.net/docs#/default/predict_premium_predict_post)

### Direct Prediction Endpoint

Applications should send POST requests directly to:

```text
https://fastapiinsurance-dkb9f7a2ehbzdxgr.uaenorth-01.azurewebsites.net/predict
```

> **Note:** The Swagger URL is intended for browser-based API testing. The Streamlit application communicates with the direct `/predict` endpoint.

> **Free-tier notice:** The applications are hosted on Azure App Service Free F1 plans. An application may require a short startup period after inactivity and may become temporarily unavailable if the free daily quota is exhausted.

---

## 🚀 Features

- Insurance premium category prediction
- Interactive Streamlit web interface
- FastAPI REST prediction endpoint
- Automatic Swagger/OpenAPI documentation
- Pydantic request validation
- Derived-feature calculation during inference
- Serialized scikit-learn model pipeline
- Git and GitHub version control
- Automated Azure deployment using GitHub Actions
- OpenID Connect authentication between GitHub and Azure
- Python dependency and environment management with `uv`
- Python 3.13 development and deployment environment
- Cross-platform model loading with `pathlib`
- Separate frontend and backend Azure Web Apps

---

## 🎯 Problem Statement

Insurance premium categories may depend on demographic, physical, lifestyle, occupational, income, and location-related factors.

This project uses supervised machine learning to predict an insurance premium category for a new customer profile.

Because the output is a category rather than an exact monetary amount, the problem is formulated as a **classification task**.

---

## 🏗️ Application Architecture

```text
User
  │
  ▼
Streamlit Web App
  │
  │ HTTPS POST request
  ▼
FastAPI /predict endpoint
  │
  ▼
Pydantic input validation
  │
  ▼
Feature engineering
  ├── BMI
  ├── Age group
  ├── Lifestyle risk
  └── City class
  │
  ▼
Serialized scikit-learn pipeline
  │
  ▼
Predicted premium category
  │
  ▼
JSON response displayed in Streamlit
```

The Streamlit frontend and FastAPI backend are deployed as two separate Azure App Service Web Apps.

---

## 🔄 Project Workflow

1. Load the insurance dataset.
2. Inspect the dataset for missing values and duplicate observations.
3. Explore numerical and categorical feature distributions.
4. Engineer relevant insurance-risk features.
5. Prepare numerical and categorical predictors.
6. Split the dataset into training and testing subsets.
7. Train and compare machine-learning classifiers.
8. Evaluate the models using classification metrics.
9. Save the selected preprocessing and classification pipeline as `model.pkl`.
10. Load the saved pipeline in the FastAPI application.
11. Validate incoming requests using Pydantic.
12. Generate the required derived features inside the API.
13. Send prediction requests from Streamlit to FastAPI.
14. Return and display the predicted premium category.
15. Deploy the frontend and backend separately to Azure App Service.
16. Automate future deployments using GitHub Actions.

---

## 🧠 Machine-Learning Models

The project explores classification algorithms for predicting insurance premium categories.

### Support Vector Classifier

A Support Vector Classifier can learn nonlinear decision boundaries between premium categories.

```python
from sklearn.svm import SVC
```

### Random Forest Classifier

A Random Forest Classifier combines predictions from multiple decision trees and can capture nonlinear relationships and interactions between insurance-risk variables.

```python
from sklearn.ensemble import RandomForestClassifier
```

The selected model is stored as part of a serialized scikit-learn pipeline:

```text
src/model.pkl
```

The pipeline should contain both preprocessing and classification steps to ensure that training and inference use the same transformations.

---

## 🧮 Input and Derived Features

### User-provided inputs

The application accepts:

- Age
- Weight in kilograms
- Height in metres
- Annual income in lakhs per annum
- Smoking status
- City
- Occupation

### Features calculated by FastAPI

The API derives the following features before prediction.

#### Body mass index

```text
BMI = weight / height²
```

#### Age group

| Age range | Group |
|---|---|
| Below 28 | Young |
| 28 to below 45 | Adult |
| 45 to below 65 | Middle_aged |
| 65 and above | Senior |

#### Lifestyle risk

| Condition | Risk category |
|---|---|
| Smoker and BMI above 30 | High |
| Smoker or BMI above 25 | Medium |
| Non-smoker and BMI of 25 or below | Low |

#### City class

| City grouping | Class |
|---|---:|
| Selected major cities | 1 |
| Selected regional cities | 2 |
| Other cities | 3 |

These derived features must remain consistent with the feature engineering used during model training.

---

## 📊 Model Evaluation

Classification models should be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Cross-validation score
- Class-wise performance

Training accuracy alone should not be used for selecting the final model. Model selection should be based on performance on unseen data and cross-validation stability.

---

## 🛠️ Technology Stack

### Programming and data analysis

- Python 3.13
- Pandas
- NumPy
- Jupyter Notebook

### Machine learning

- scikit-learn
- Support Vector Classification
- Random Forest Classification
- Pickle model persistence

### Backend

- FastAPI
- Pydantic
- Uvicorn
- Gunicorn

### Frontend

- Streamlit
- Requests

### Cloud deployment

- Microsoft Azure App Service
- Linux Web Apps
- Azure App Service Free F1 plans
- Azure Deployment Center
- Azure managed identities
- OpenID Connect

### CI/CD and version control

- Git
- GitHub
- GitHub Actions

### Dependency management

- `uv`
- `pyproject.toml`
- `uv.lock`
- `requirements.txt`

---

## 📁 Repository Structure

```text
Insurance-premium-prediction-app/
│
├── .github/
│   └── workflows/
│       ├── main_fastapiinsurance.yml
│       └── main_streamlitapp.yml
│
├── data/
│   └── [insurance dataset]
│
├── src/
│   ├── insurance_api.py
│   ├── stream_lit.py
│   └── model.pkl
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── README.md
├── Streamlit app screenshot.png
└── fastApi screenshot.png
```

### Important files

- `src/insurance_api.py`: FastAPI application, input validation, feature engineering, model loading, and prediction endpoint
- `src/stream_lit.py`: Streamlit user interface and FastAPI request handling
- `src/model.pkl`: Serialized preprocessing and classification pipeline
- `pyproject.toml`: Project metadata and direct dependencies
- `uv.lock`: Reproducible dependency lockfile
- `requirements.txt`: Azure and GitHub Actions deployment dependencies
- `.python-version`: Python version used by `uv`
- `.github/workflows/`: GitHub Actions deployment workflows

---

## ⚙️ Local Installation

### Prerequisites

Install:

- Python 3.13
- Git
- `uv`

### 1. Clone the repository

```bash
git clone https://github.com/avneeshDS/Insurance-premium-prediction-app.git
cd Insurance-premium-prediction-app
```

### 2. Install dependencies

```bash
uv sync
```

This creates a project virtual environment and installs the dependencies recorded in `uv.lock`.

### 3. Verify the Python version

```bash
uv run python --version
```

Expected output:

```text
Python 3.13.x
```

### 4. Verify the main dependencies

```bash
uv run python -c "import fastapi, streamlit, sklearn, pandas, numpy; print('Dependencies OK')"
```

---

## ▶️ Running the Applications Locally

FastAPI and Streamlit must run in separate terminals.

### Terminal 1: Start FastAPI

From the repository root:

```bash
uv run uvicorn src.insurance_api:app --host 127.0.0.1 --port 8000 --reload
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

FastAPI ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

Local prediction endpoint:

```text
http://127.0.0.1:8000/predict
```

### Terminal 2: Start Streamlit

```bash
uv run streamlit run src/stream_lit.py --server.port 8501
```

The Streamlit application will normally be available at:

```text
http://localhost:8501
```

The FastAPI backend must be running before a prediction is submitted from Streamlit.

---

## 🔌 API Endpoint

### Predict an insurance premium category

```http
POST /predict
```

### Azure endpoint

```text
https://fastapiinsurance-dkb9f7a2ehbzdxgr.uaenorth-01.azurewebsites.net/predict
```

### Example request

```json
{
  "age": 38,
  "weight": 70,
  "height": 1.72,
  "income_lpa": 15,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}
```

### Example response

```json
{
  "predicted_category": "Medium"
}
```

### Supported occupation values

```text
retired
freelancer
student
government_job
business_owner
unemployed
private_job
```

### Example Python request

```python
import requests

api_url = (
    "https://fastapiinsurance-dkb9f7a2ehbzdxgr."
    "uaenorth-01.azurewebsites.net/predict"
)

payload = {
    "age": 38,
    "weight": 70,
    "height": 1.72,
    "income_lpa": 15,
    "smoker": False,
    "city": "Delhi",
    "occupation": "private_job",
}

response = requests.post(
    api_url,
    json=payload,
    timeout=30,
)

response.raise_for_status()
print(response.json())
```

---

## 🔁 Prediction Flow

1. A user enters information in the Streamlit interface.
2. Streamlit converts the inputs into a JSON payload.
3. Streamlit sends an HTTPS POST request to the FastAPI `/predict` endpoint.
4. Pydantic validates the submitted fields and data types.
5. FastAPI calculates BMI, age group, lifestyle risk, and city class.
6. FastAPI creates a Pandas DataFrame using the features expected by the trained pipeline.
7. The scikit-learn pipeline predicts the insurance premium category.
8. FastAPI returns the result as JSON.
9. Streamlit displays the predicted category.

---

## 🔗 Configuring the API URL

For local execution, `src/stream_lit.py` should use:

```python
API_URL = "http://127.0.0.1:8000/predict"
```

For Azure deployment, use:

```python
API_URL = (
    "https://fastapiinsurance-dkb9f7a2ehbzdxgr."
    "uaenorth-01.azurewebsites.net/predict"
)
```

Do not use the Swagger URL as the API endpoint:

```text
/docs#/default/predict_premium_predict_post
```

The Swagger fragment is only for interactive browser documentation.

---

## ☁️ Azure Deployment

The frontend and backend are deployed as separate Linux Web Apps.

### FastAPI Web App

The FastAPI service is deployed at:

[FastAPI Swagger documentation](https://fastapiinsurance-dkb9f7a2ehbzdxgr.uaenorth-01.azurewebsites.net/docs#/default/predict_premium_predict_post)

#### Startup command

```bash
gunicorn -w 1 -k uvicorn.workers.UvicornWorker src.insurance_api:app --bind 0.0.0.0:8000 --timeout 600
```

### Streamlit Web App

The Streamlit interface is deployed at:

[Streamlit application](https://streamlitapp-hsf5eug5g0b0emf9.indonesiacentral-01.azurewebsites.net/)

#### Startup command

```bash
python -m streamlit run src/stream_lit.py --server.port 8000 --server.address 0.0.0.0 --server.headless true
```

### Required Azure application setting

```text
SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

This instructs Azure App Service to install dependencies from `requirements.txt` during deployment.

### Runtime alignment

The following environments should use the same Python version:

```text
Local uv environment: Python 3.13
GitHub Actions:        Python 3.13
Azure App Service:     Python 3.13
```

---

## 🔁 CI/CD with GitHub Actions

A push to the `main` branch triggers the configured GitHub Actions deployment workflows.

The workflows perform the following steps:

1. Check out the repository.
2. Configure Python 3.13.
3. Create a temporary virtual environment.
4. Install packages from `requirements.txt`.
5. Package the application.
6. Authenticate to Azure using OpenID Connect.
7. Deploy the package to the corresponding Azure Web App.

Separate workflows deploy:

- The FastAPI backend
- The Streamlit frontend


---


## 🧪 Testing

Run code-quality checks with Ruff:

```bash
uv run ruff check .
```

Format the code:

```bash
uv run ruff format .
```

Run the test suite:

```bash
uv run pytest
```

## 🧩 Troubleshooting

### Streamlit cannot connect to FastAPI

Confirm that:

- FastAPI is running
- The `/predict` URL is correct
- Streamlit is using the direct API URL
- The request uses `requests.post()`
- The FastAPI Web App has not exhausted its Free F1 quota

### HTTP 405: Method Not Allowed

A 405 response generally means Streamlit is calling the wrong path or HTTP method.

### HTTP 422: Unprocessable Entity

The submitted JSON fields or data types do not match the Pydantic schema.


### HTTP 500: Internal Server Error

Inspect the FastAPI logs. Common causes include:


### HTTP 403: Site Disabled

The Azure Web App may be stopped or the Free F1 quota may be exhausted.

### HTTP 503: Service Unavailable

The application process may have failed to start. 


---

## 💰 Azure Free-Tier Considerations

The project uses separate Azure Web Apps for FastAPI and Streamlit.

## 👤 Author

**Avneesh Kumar**

- GitHub: [avneeshDS](https://github.com/avneeshDS)
- Repository: [Insurance-premium-prediction-app](https://github.com/avneeshDS/Insurance-premium-prediction-app)
- Streamlit: [Live web application](https://streamlitapp-hsf5eug5g0b0emf9.indonesiacentral-01.azurewebsites.net/)
- FastAPI: [Swagger documentation](https://fastapiinsurance-dkb9f7a2ehbzdxgr.uaenorth-01.azurewebsites.net/docs#/default/predict_premium_predict_post)

If this project is useful, consider starring the repository.
