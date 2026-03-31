import os
from joblib import load
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import logging

#load content .env into environmment variables
load_dotenv()
PROJECT_ROOT=Path(os.getenv("PROJECT_ROOT"))
MODEL_PATH=PROJECT_ROOT/os.getenv("MODEL_DIR")/os.getenv("MODEL_NAME")
LOG_PATH=PROJECT_ROOT/os.getenv("LOG_DIR")/os.getenv("LOG_NAME")

MODEL_PATH.parent.mkdir(parents=True,exist_ok=True)
LOG_PATH.parent.mkdir(parents=True,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_PATH)
    ]
)

# model loading 
model=load(MODEL_PATH)
logging.info("model loaded successfully")

def predict(input_data):
    df=pd.DataFrame([input_data])
    prediction=model.predict(df)[0]
    logging.info("Model provided a prediction")
    return prediction



# example usage
# input_data = {
#     "Pregnancies": 2,
#     "Glucose": 120,
#     "BloodPressure": 150,
#     "SkinThickness": 25,
#     "Insulin": 50,
#     "BMI": 28.5,
#     "DiabetesPedigreeFunction": 0.583,
#     "Age": 30
# }

# model_prediction = predict(input_data=input_data)
# print(model_prediction)