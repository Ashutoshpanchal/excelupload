# schemas.py

from pydantic import BaseModel
from typing import Optional,List




class EmployeeSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    salary: Optional[float] = None
    manager_id: Optional[int] = None
    department_id: Optional[int] = None
    company_id: int

    class Config:
        orm_mode = True




class CompanySchema(BaseModel):
    id: int
    name: str
    employees: Optional[List[EmployeeSchema]] = []

    class Config:
        orm_mode = True