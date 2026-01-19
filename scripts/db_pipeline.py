# ============================================================
# db_pipeline.py
# Video Game Sales – SQL Create & Load Pipeline
# ============================================================

import pandas as pd
import pymysql
from sqlalchemy import create_engine

# ---------------- DATABASE CONFIG ----------------
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"   
DATABASE_NAME = "video_game_db"
TABLE_NAME = "video_game_sales"

# ---------------- CREATE DATABASE ----------------
def create_database():
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
    conn.close()

# ---------------- CREATE TABLE ----------------
def create_table():
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=DATABASE_NAME
    )
    cursor = conn.cursor()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        game_name VARCHAR(200),
        platform VARCHAR(50),
        year INT,
        genre VARCHAR(50),
        publisher VARCHAR(100),
        na_sales FLOAT,
        eu_sales FLOAT,
        jp_sales FLOAT,
        other_sales FLOAT,
        global_sales FLOAT,
        rating VARCHAR(20)
    )
    """
    cursor.execute(create_table_query)
    conn.close()

# ---------------- INSERT DATA ----------------
def insert_data():
    engine = create_engine(
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{DATABASE_NAME}"
    )

    df = pd.read_csv("data/cleaned_video_game_data.csv")

     # Rename 'name' to match DB column 'game_name'
    if "name" in df.columns:
        df = df.rename(columns={"name": "game_name"})

    df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=1000
    )

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("🚀 Starting SQL Load Pipeline")

    create_database()
    print("✅ Database ready")

    create_table()
    print("✅ Table created")

    insert_data()
    print("✅ Data inserted successfully")

    print("🎉 SQL pipeline completed")
