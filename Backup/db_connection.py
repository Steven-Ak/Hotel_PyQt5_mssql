# database_manager.py
import pyodbc

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=LAPTOP-MEABQQJG;'
            'DATABASE=hotel;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Database connection error: {str(e)}")
        return None

# Usage
connection = get_db_connection()
if connection:
    print("Connected to the database successfully!")
else:
    print("Failed to connect to the database.")
