from fastapi import FastAPI
import pickle



with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    

app = FastAPI()

class1_cities = ["Mumbai", "Delhi", "Jaipur", "Bangalore", "Chandigarh", "Chennai", "Kolkata", "Hyderabad", "Pune"]
class2_cities = [
    "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# Pydantic model to validate incoming data 
import pydantic
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=100, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
    smoker: Annotated[bool, Field(..., description='Is user a smoker')]
    city: Annotated[str, Field(..., description='The city that the user belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')] 

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2) 
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 28:
            return 'Young'
        elif self.age < 45:
            return 'Adult'
        elif self.age < 65:
            return 'Middle_aged'
        return "Senior"
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'High'
        elif self.smoker or self.bmi > 25:
            return 'Medium'
        else:
            return 'Low'
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in class1_cities:
            return 1
        elif self.city in class2_cities:
            return 2
        else:
            return 3

import pandas as pd   
from fastapi.responses import JSONResponse   
@app.post('/predict')
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{'bmi': data.bmi, 'age_group': data.age_group, 'lifestyle_risk': data.lifestyle_risk, 'city_tier': data.city_tier, 'income_lpa': data.income_lpa, 'occupation': data.occupation}])

    prediction = model.predict(input_df)[0]
    
    return JSONResponse(status_code=200, content={'predicted_category': prediction})