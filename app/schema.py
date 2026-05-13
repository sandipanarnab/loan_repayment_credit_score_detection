from pydantic import BaseModel

class LoanInput(BaseModel):

    dti: float
    grade: str
    term: str
    int_rate: float
    purpose: str
    revol_util: float