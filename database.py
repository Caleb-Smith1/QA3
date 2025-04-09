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

def insert_sample_questions():
    conn = connect_db()
    cursor = conn.cursor()

    questions = [
        # DATABASE ADMINISTRATION
        ("database_admin", "True or false - In a database Primary keys must be unique.", "True", "False", None, None, "True"),
        ("database_admin", "True or false - NOSQL means 'not only sql'", "True", "False", None, None, "True"),

        # MICROECONOMICS
        ("microeconomics", "True or false - The definition of economics states that it is the study of: agents choose to allocate scarce resources and the impact of those choices on society.", "True", "False", None, None, "True"),
        ("microeconomics", "Yes or No - Does causation imply correlation?", "Yes", "No", None, None, "No"),

        # BUSINESS MANAGEMENT
        ("business_mgmt", "Which of these is NOT true", 
         "Employees will rarely encounter ethical challenges in their career", 
         "Ethics help us decide between what is 'right' and what is 'wrong'.",
         "The legal system cannot always be relied on to determine what is ethical",
         "Unethical behavior can damage relationships & the business as a whole.",
         "Employees will rarely encounter ethical challenges in their career"),

        ("business_mgmt", "What is one of the three components of attitude?", 
         "Affective", "Openness to change", "Conservation", "Job Satisfaction", 
         "Affective"),

        # BUSINESS STATISTICS
        ("statistics", "Fill in the blank - The _____ is the most frequently occurring value", 
         "Mean", "Median", "Mode", "Range", "Mode"),
        ("statistics", "Yes or No - range is a good measure of dispersion?", 
         "Yes", "No", None, None, "No"),

        # BUSINESS APP DEV
        ("app_dev", 'print("5+5") would return what?', 
         "10", "5+5", "Error", None, "5+5"),
        ("app_dev", "print(8*10) would return what?", 
         "80", "810", "8*10", "Error", "80")
    ]

    for q in questions:
        cursor.execute(f"""
        INSERT INTO {q[0]} (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
        """, q[1:])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_sample_questions()
    print("Database, tables, and sample questions created successfully.")
