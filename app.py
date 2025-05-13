from fastapi import FastAPI, UploadFile,Depends,Request
import pandas as pd
import io
import uvicorn
from config import settings
import os
from sqlalchemy.orm import Session
from db import get_db
from company import Company
from employee import Employee
from utility import insert_into_company,get_companies_by_names,insert_into_emp


app = FastAPI(
    title=settings.PROJECT_NAME,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)


@app.middleware("http")
async def check_db_exists(request: Request, call_next):
    if not os.path.exists(settings.DATABASE_URL):
        from sqlalchemy import create_engine
        from db import Base
        engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
        Base.metadata.create_all(bind=engine)
        try:
            Company.__table__.create(bind=engine)
            Employee.__table__.create(bind=engine)
        except:
            pass
        
        print("Database created!")
    response = await call_next(request)
    return response



@app.post("/upload/")
async def upload_file(file: UploadFile,db:Session = Depends(get_db)):
    content = await file.read()
    if file.filename.endswith(".xlsx"):
        df = pd.read_excel(io.BytesIO(content)) 
    elif file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(content)) 
    else:
        return {"message": "File format not supported. Please upload a .xlsx or .csv file."}
    companies = df["COMPANY_NAME"].drop_duplicates().to_frame("name")
    companies_dict  = companies.to_dict("records")
    await insert_into_company(db, companies_dict)
    ids_name = await get_companies_by_names(db, companies["name"].tolist())
    company_ids = {name: id for id, name in ids_name}
    df["company_id"] = df["COMPANY_NAME"].map(company_ids)
    df.drop(columns=["COMPANY_NAME"], inplace=True)
    df.columns = df.columns.str.lower()
    employees = df
    await insert_into_emp(db, employees.to_dict("records"))
    return {"message": "Data successfully inserted into the database."}

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=4545,reload=True) 

