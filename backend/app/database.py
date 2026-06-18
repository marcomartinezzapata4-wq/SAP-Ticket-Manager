from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SERVER = "DESKTOP-7V6GCSR\\SQLEXPRESS"
DATABASE = "SAPTicketManager"
DRIVER = "ODBC Driver 17 for SQL Server"

DATABASE_URL = (
    f"mssql+pyodbc://{SERVER}/{DATABASE}"
    f"?driver={DRIVER}&trusted_connection=yes"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from . import models

Base.metadata.create_all(bind=engine)