from fastapi import FastAPI
from app.tax import calculate_pph21
from app.schemas import IncomeRequest

app = FastAPI()

@app.post("/pph21")
def calculate_pph(data: IncomeRequest):
    annual_income = data.annual_income
    pph = calculate_pph21(annual_income)
    return {"pph21": pph}
@app.get("/")
def index():
    return {
        "message": "Hello World",
        "status": "FastAPI is running"
    }