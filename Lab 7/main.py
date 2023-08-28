from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
from io import StringIO
import requests
app = FastAPI()
class ChurnClass (BaseModel):
    CreditScore: float
    Age:         float
    Tenure:   float   
    Balance: float
    NumOfProducts: float
    IsActiveMember: float
    EstimatedSalary: float
    Geography_France: float
    Geography_Germany: float
    Geography_Spain: float
    Gender_Female: float
    Gender_Male: float



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/predict')
async def predict_churn (churn: ChurnClass):
    data = churn.dict()
    data_in = [[
        data['CreditScore'], 
        data['Age'], 
        data['Tenure'], 
        data['Balance'],
        data['NumOfProducts'],
        data['IsActiveMember'],
        data['EstimatedSalary'],
        data['Geography_France'],
        data['Geography_Germany'],
        data['Geography_Spain'],
        data['Gender_Female'],
        data['Gender_Male']
        ]]
    print (data_in)
    endpoint = "http://localhost:1234/invocations"
    inference_request = {
    "dataframe_records": data_in
    }
    print (inference_request)



@app.post("/files/")
#async def create_file(file: bytes = File(...), fileb: Upload File = File(...), token: str = Form(...)):
async def batch_prediction (file: bytes = File(...)):
    s=str(file, 'utf-8')
    data = StringIO(s)
    df=pd.read_csv (data)
    lst = df.values.tolist ()
    inference_request = {
        "dataframe_records": lst
    }
    endpoint = "http://localhost:1234/invocations"
    response = requests.post(endpoint, json=inference_request)
    print (response.text)
    return response.text

# uvicorn main:app --reload
# run the above line in terminal