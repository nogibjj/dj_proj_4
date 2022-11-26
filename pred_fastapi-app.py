from fastapi import FastAPI
import uvicorn
from classifier_check import predict_attrition


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Duke"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/pred")
async def pred():
    """predict whether a certain person quits"""

    payload = predict_attrition()
    return payload


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')