# 🏥 Insurance Premium Category Prediction App

An end-to-end machine learning application that predicts an **insurance premium category** from user-provided information.

The project covers the complete machine learning workflow, including data ingestion, exploratory data analysis, preprocessing, model training, model evaluation, API development, database integration, and interactive prediction through a web interface.

Two machine learning models were trained and compared:

- Support Vector Machine
- Random Forest Classifier

The prediction service is implemented with **FastAPI**, while **Streamlit** provides the interactive frontend. **PostgreSQL** is used for structured data storage, and **uv** is used for dependency and environment management.

> **Important:** If the project uses `sklearn.svm.SVC`, describe the model as a **Support Vector Classifier**. If it uses `sklearn.svm.SVR`, SVR is a regression model rather than a classifier. Update the model description in this README to match the implementation.

---

## 🚀 Features

- End-to-end machine learning workflow
- Insurance premium category prediction
- Support Vector Machine model
- Random Forest Classifier model
- Model training and performance comparison
- Interactive Streamlit user interface
- FastAPI REST API for model inference
- Pydantic request validation
- PostgreSQL database integration
- CSV-based dataset ingestion
- Serialized model loading for inference
- Automatic Swagger API documentation
- Dependency and environment management with uv
- Organized source package under `src/`

---

## 🎯 Problem Statement

Insurance premiums can vary according to demographic, lifestyle, health, and location-related factors. The purpose of this project is to use supervised machine learning to predict the appropriate insurance premium category for a new observation.

Because the target is a category rather than an exact monetary amount, the problem is treated as a **classification task**.

---

## 🔄 Project Workflow

1. Load the insurance dataset from a CSV file.
2. Explore the dataset and inspect feature distributions.
3. Identify missing values and duplicate observations.
4. Preprocess numerical and categorical features.
5. Split the data into training and test sets.
6. Train and compare two machine learning models.
7. Evaluate the models using classification metrics.
8. Save the selected model and preprocessing objects.
9. Expose the selected model through a FastAPI endpoint.
10. Send user input from Streamlit to the FastAPI backend.
11. Display the predicted premium category in the Streamlit app.
12. Store relevant structured data in PostgreSQL.

---

## 🧠 Machine Learning Models

### 1. Support Vector Machine

A Support Vector Machine model was trained to learn the decision boundaries between the insurance premium categories.

If the implementation uses classification labels, the appropriate scikit-learn estimator is:

```python
from sklearn.svm import SVC
```

If the implementation currently uses `SVR`, review the problem formulation because `SVR` predicts continuous numerical values rather than categorical classes.

### 2. Random Forest Classifier

A Random Forest Classifier was trained as an ensemble-based alternative. Random Forest combines multiple decision trees and uses their aggregated predictions to classify each observation.

```python
from sklearn.ensemble import RandomForestClassifier
```

The final model is selected based on test-set and cross-validation performance, rather than training accuracy alone.

---

## 📊 Model Evaluation

The models can be compared using the following classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Cross-validation score

Add the actual results obtained from the notebook below:

```text
Support Vector Machine
Accuracy: [add value]
Precision: [add value]
Recall: [add value]
F1-score: [add value]
Cross-validation score: [add mean ± standard deviation]

Random Forest Classifier
Accuracy: [add value]
Precision: [add value]
Recall: [add value]
F1-score: [add value]
Cross-validation score: [add mean ± standard deviation]

Selected model: [add selected model]
```

---

## 🛠️ Tech Stack

### Programming and data analysis

- Python
- Pandas
- NumPy
- Jupyter Notebook

### Machine learning

- scikit-learn
- Support Vector Machine
- Random Forest Classifier

### Backend and API

- FastAPI
- Uvicorn
- Pydantic

### Frontend

- Streamlit
- Requests

### Database

- PostgreSQL

### Development tools

- Git
- GitHub
- uv

---

## 📁 Repository Structure

```text
Insurance-premium-prediction-app/
|
├── src/
│   └── insurance_premium_prediction_app/
│       └── [source package files]
|
├── .gitignore
├── .python-version
├── README.md
├── Streamlit app screenshot.png
├── fastApi screenshot.png
├── insurance.csv
├── insurance_api.py
├── insurance_code.ipynb
├── pyproject.toml
├── stream_lit.py
└── uv.lock
```

### Main files

- `insurance_code.ipynb`: Exploratory data analysis, preprocessing, model training, and model evaluation
- `insurance_api.py`: FastAPI application and prediction endpoint
- `stream_lit.py`: Streamlit frontend application
- `insurance.csv`: Dataset used for model development
- `pyproject.toml`: Project metadata and dependency configuration
- `uv.lock`: Locked dependency versions for reproducible installation
- `src/insurance_premium_prediction_app/`: Python source package
- `Streamlit app screenshot.png`: Screenshot of the Streamlit application
- `fastApi screenshot.png`: Screenshot of the FastAPI Swagger interface

---

## ⚙️ Installation

### Prerequisites

Install the following software before running the application:

- Python
- Git
- uv
- PostgreSQL

### 1. Clone the repository

```bash
git clone https://github.com/avneeshDS/Insurance-premium-prediction-app.git
cd Insurance-premium-prediction-app
```

### 2. Install the dependencies

The repository contains `pyproject.toml` and `uv.lock`. Install the locked dependencies with:

```bash
uv sync
```

This command creates a virtual environment and installs the required packages.

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

#### Linux or macOS

```bash
source .venv/bin/activate
```

You can also run project commands with `uv run` without manually activating the environment.

---

## 🗄️ PostgreSQL Configuration

Create a PostgreSQL database for the application and configure the connection values used by the project.

A local `.env` file can be used to store the database configuration:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=insurance_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Alternatively, use a database connection URL:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/insurance_db
```

Do not commit passwords or other secrets to GitHub. Ensure that `.env` is included in `.gitignore`:

```text
.env
```

The environment-variable names must match the names used in the Python application.

---

## ▶️ Running the Application

### 1. Start the FastAPI backend

Run the following command from the repository root:

```bash
uv run uvicorn insurance_api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI will be available at:

```text
http://127.0.0.1:8000/docs
```

ReDoc will be available at:

```text
http://127.0.0.1:8000/redoc
```

### 2. Start the Streamlit frontend

Open another terminal in the repository root and run:

```bash
uv run streamlit run stream_lit.py
```

The Streamlit application will normally open at:

```text
http://localhost:8501
```

The FastAPI backend must be running before predictions are submitted from Streamlit.

---

## 🔌 API Endpoint

### Predict an insurance premium category

```http
POST /predict
```

### Example request

The following request is an example. Update the field names and values so that they exactly match the Pydantic schema in `insurance_api.py`.

```json
{
  "age": 38,
  "height": 1.72,
  "weight": 70,
  "smoker": 1,
  "city": "Prague"
}
```

### Example response

```json
{
  "predicted_premium_category": "Medium"
}
```

The actual category names depend on the target labels used during model training.

---

## 🔁 Prediction Flow

1. A user enters information in the Streamlit interface.
2. Streamlit converts the input into a JSON request.
3. Streamlit sends a POST request to the FastAPI `/predict` endpoint.
4. Pydantic validates the submitted fields and data types.
5. FastAPI applies the preprocessing steps used during model training.
6. The selected classifier predicts the insurance premium category.
7. FastAPI returns the prediction as a JSON response.
8. Streamlit displays the predicted category.
9. Relevant structured information can be stored in PostgreSQL.

---

## 🖥️ Application Screenshots

### Streamlit application

![Streamlit application](Streamlit%20app%20screenshot.png)

### FastAPI Swagger interface

![FastAPI Swagger interface](fastApi%20screenshot.png)

---

## 📓 Model Development

The model-development notebook contains the following stages.

### Data loading

The insurance dataset is loaded from `insurance.csv` using Pandas.

### Exploratory data analysis

The analysis includes:

- Dataset dimensions
- Feature data types
- Missing-value inspection
- Duplicate-observation inspection
- Numerical-feature distributions
- Categorical-feature distributions
- Relationships between the predictors and target category

### Data preprocessing

The preprocessing process may include:

- Missing-value handling
- Categorical-feature encoding
- Numerical-feature scaling
- Feature selection
- Training and test splitting

### Model training

The prepared training data is used to train and compare the Support Vector Machine and Random Forest Classifier.

### Model evaluation

The models are evaluated on unseen data using appropriate classification metrics. Cross-validation can also be used to estimate model stability.

### Model persistence

The selected model and all required preprocessing components are serialized and loaded by the FastAPI application during inference.

For reliable predictions, preprocessing during inference must be identical to preprocessing during training. A scikit-learn `Pipeline` is recommended for combining preprocessing and model inference.

---

## 📝 Key Learnings

This project demonstrates experience in:

- Framing a business problem as a machine learning classification task
- Preparing numerical and categorical data
- Training and comparing classification models
- Evaluating models with suitable classification metrics
- Avoiding preprocessing inconsistencies between training and inference
- Serving a trained model through a REST API
- Validating API requests with Pydantic
- Connecting a Streamlit frontend to a FastAPI backend
- Integrating a Python application with PostgreSQL
- Managing dependencies and environments with uv
- Organizing an end-to-end machine learning repository
- Handling model serialization and dependency compatibility

---

## 🔮 Future Improvements

- Add automated unit tests
- Add FastAPI endpoint tests
- Add input-validation tests
- Combine preprocessing and classification in a scikit-learn pipeline
- Add stratified cross-validation
- Investigate class imbalance
- Perform hyperparameter optimization
- Add feature-importance visualization
- Add SHAP-based model explanations
- Add structured application logging
- Add data-drift and model-performance monitoring
- Add Docker and Docker Compose
- Add GitHub Actions for continuous integration
- Add authentication and authorization
- Deploy the application to a cloud platform
- Manage secrets through environment variables
- Add model version tracking
- Add FastAPI health-check endpoints

---

## ⚠️ Disclaimer

This repository is an educational and portfolio machine learning project.

The predicted insurance premium categories must not be used for real insurance pricing, underwriting, medical assessment, financial decisions, or eligibility determination without appropriate validation, regulatory review, security controls, and qualified domain-expert oversight.

---

## 👤 Author

**Avneesh Kumar**

- GitHub: [avneeshDS](https://github.com/avneeshDS)


If you find this project useful, consider starring the repository.
