from enum import Enum
from pydantic import BaseModel
from typing import Optional
from typing_extensions import TypedDict

class CategoryEnum(str, Enum):
    food = "food"
    transport = "transport"
    health = "health"
    education = "education"
    housing = "housing"
    entertainment = "entertainment"
    shopping = "shopping"
    services = "services"
    travel = "travel"
    taxes = "taxes"
    other = "other"

class ExpenseRecord(BaseModel):
    description: Optional[str] = None
    category: Optional[CategoryEnum] = None
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    vendor: Optional[str] = None
    notes: Optional[str] = None 
    
class Graph(TypedDict):
    entry: dict
    user_input: str
    image_path: str
    extracted_text: Optional[str]
    expense_record: Optional[ExpenseRecord]