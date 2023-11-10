import sqlite3 as sql

def sert_info(height: float, weight: float, result: float):
    with sql.connect("testbd.db") as database:
        cursor = database.cursor()
        cursor.execute(f"INSERT INTO result (height, weight, result) VALUES {height, weight, result}")
