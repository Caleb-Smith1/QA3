import tkinter as tk

def open_quiz_interface(root):
    win = tk.Toplevel(root)
    win.title("Select a Quiz Category")
    win.geometry("300x300")

    label = tk.Label(win, text="Choose a Category", font=("Arial", 14))
    label.pack(pady=10)

    categories = {
        "Database Admin": "database_admin",
        "Microeconomics": "microeconomics",
        "Business Mgmt": "business_mgmt",
        "Statistics": "statistics",
        "App Dev": "app_dev"
    }

    def start_quiz(table_name):
        # Placeholder: real quiz will load from the table
        quiz_window = tk.Toplevel(win)
        quiz_window.title(f"{table_name} Quiz")
        msg = tk.Label(quiz_window, text=f"Loading quiz from '{table_name}'...", font=("Arial", 12))
        msg.pack(padx=20, pady=20)

    for label_text, table_name in categories.items():
        btn = tk.Button(win, text=label_text, width=25, command=lambda t=table_name: start_quiz(t))
        btn.pack(pady=5)