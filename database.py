import sqlite3

def connect_db():
    return sqlite3.connect("quiz.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    table_names = {
        "database_admin": "Database Administration",
        "microeconomics": "Microeconomics",
        "business_mgmt": "Business Management",
        "statistics": "Business Statistics",
        "app_dev": "Business App Development"
    }

    for table in table_names:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT,
            option_b TEXT,
            option_c TEXT,
            option_d TEXT,
            correct_answer TEXT NOT NULL
        );
        """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")