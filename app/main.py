import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load


app = FastAPI(title='Churn Prediction')

model = load('../model/churn.joblib')
transformer = load('../model/transformer.joblib')


class InputData(BaseModel):
    credit_score: int
    country: str
    gender: str
    age: int
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float


class OutputData(BaseModel):
    score: float


@app.post('/score', response_model=OutputData)
def score(data: InputData):
    model_input = {k: [v] for (k, v) in data.dict().items()}
    data = pd.DataFrame.from_dict(model_input)
    data = data.astype({"gender": "category", "country": "category", "products_number": "category",
                        "credit_card": bool, "active_member": bool})
    result = model.predict(transformer.transform(data))[0]
    return {'score': result}
