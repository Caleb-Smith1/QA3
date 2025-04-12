import tkinter as tk
from tkinter import ttk
import sqlite3

def open_admin_panel(root):
    win = tk.Toplevel(root)
    win.title("Admin Panel")
    win.geometry("700x400")

    label = tk.Label(win, text="All Questions in the Database", font=("Arial", 14))
    label.pack(pady=10)

    tree = ttk.Treeview(win, columns=("Category", "Question", "Correct Answer"), show="headings")
    tree.heading("Category", text="Category")
    tree.heading("Question", text="Question")
    tree.heading("Correct Answer", text="Correct Answer")
    tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def load_questions():
        tree.delete(*tree.get_children())  # Clear existing rows
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()

        tables = {
            "database_admin": "Database Admin",
            "microeconomics": "Microeconomics",
            "business_mgmt": "Business Mgmt",
            "statistics": "Statistics",
            "app_dev": "App Dev"
        }

        for table, label in tables.items():
            cursor.execute(f"SELECT question, correct_answer FROM {table}")
            for row in cursor.fetchall():
                tree.insert("", "end", values=(label, row[0], row[1]))

        conn.close()

    load_btn = tk.Button(win, text="Refresh Questions", command=load_questions)
    load_btn.pack(pady=10)

    load_questions()  # Load when window opens