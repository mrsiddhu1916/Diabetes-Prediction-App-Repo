from fastapi import FastAPI

from pydantic import BaseModel 

from predictor import predict

app=FastAPI(title="ML prediction app")

class predictionInput(BaseModel):
    Pregnancies:int
    Glucose:float
    BloodPressure:float
    SkinThickness:float
    Insulin:float
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int

@app.post("/predict")
def Diabetes_prediction(input_data:predictionInput):
    prediction = predict(input_data.model_dump())
    if prediction ==1:
        results="Diabetes"
    else:
        results="no diabetes"
    return{
        "prediction":int(prediction),
        results:results
    }