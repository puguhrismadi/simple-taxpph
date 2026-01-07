from pydantic import BaseModel
class IncomeRequest(BaseModel):
    annual_income: float