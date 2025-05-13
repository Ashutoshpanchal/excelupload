# excelupload

# excelupload

## Excel/CSV Upload API with FastAPI

This project provides a FastAPI-based API to upload Excel (`.xlsx`) or CSV (`.csv`) files, process the data, and insert it into a SQLite database. The database consists of two tables: `Company` and `Employee`, with a one-to-many relationship between them.

---

## Features

- Upload `.xlsx` or `.csv` files containing employee and company data.
- Automatically creates the database and tables if they do not exist.
- Inserts unique company data into the `Company` table.
- Maps employees to their respective companies using a foreign key (`company_id`).
- Handles duplicate entries gracefully using SQLite's `ON CONFLICT` clause.

---

## Requirements

- Python 3.9 or higher
- FastAPI
- Uvicorn
- Pandas
- SQLAlchemy

---

## Installation

1. Clone the repository:
   
- git clone <repository-url>
- cd <repository-folder>
- pip install -r requirements.txt


2. Run
- python app.py


3.Visit
-Open your browser and navigate to http://127.0.0.1:4545/docs to access the interactive Swagger UI.








