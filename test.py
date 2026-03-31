

import requests

API_URL="http://127.0.0.1:8000/predict"

payload={
    "Pregnancies": 2,
    "Glucose": 140,
    "BloodPressure": 100,
    "SkinThickness": 30,
    "Insulin": 80,
    "BMI": 25,
    "DiabetesPedigreeFunction": 0.355,
    "Age": 28
}

#send post request

response=requests.post(API_URL , json=payload)

print("status code", response.status_code)
print("responde_json", response.json())