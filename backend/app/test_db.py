import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=SAPTicketManager;"
    
    "Trusted_Connection=yes;"
)

print("Conectado correctamente")