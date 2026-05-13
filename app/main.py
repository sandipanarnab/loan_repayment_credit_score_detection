from fastapi import FastAPI

from app.schema import LoanInput
from app.predictor import predict_loan

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Loan API Running"
    }


@app.post("/predict")
def predict(input_data: LoanInput):

    result = predict_loan(
        input_data.dict()
    )

    return result