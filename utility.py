from company import Company
from employee import Employee
from sqlalchemy import select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

async def insert_into_company(db:Session, companies:dict):
    query = insert(Company).values(companies)
    query = query.on_conflict_do_nothing(
        index_elements=["name"], 
    )
    db.execute(query)
    db.commit()



async def get_companies_by_names(session: Session, company_names: list):
    query = select(Company.id, Company.name).where(Company.name.in_(company_names))
    result = session.execute(query).all()
    return result



async def insert_into_emp(db: Session, emp: dict):
    query = insert(Employee).values(emp)
    query = query.on_conflict_do_nothing(index_elements=["employee_id"]) 
    db.execute(query)
    db.commit()