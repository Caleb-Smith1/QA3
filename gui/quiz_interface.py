import tkinter as tk
import sqlite3

def open_quiz_interface(root):
    category_map = {
        "Database Admin": "database_admin",
        "Microeconomics": "microeconomics",
        "Business Mgmt": "business_mgmt",
        "Statistics": "statistics",
        "App Dev": "app_dev"
    }

    win = tk.Toplevel(root)
    win.title("Select a Quiz Category")
    win.geometry("300x300")

    label = tk.Label(win, text="Choose a Category", font=("Arial", 14))
    label.pack(pady=10)

    def start_quiz(table_name, category_label):
        win.destroy()  # Close category selection
        quiz_window = tk.Toplevel(root)
        quiz_window.title(f"{category_label} Quiz")
        quiz_window.geometry("500x300")

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {table_name} LIMIT 2")
        questions = cursor.fetchall()
        conn.close()

        current_q = [0]
        score = [0]
        user_answer = tk.StringVar()

        def show_question():
            q = questions[current_q[0]]
            question_label.config(text=f"Q{current_q[0]+1}: {q[0]}")
            user_answer.set(None)  # Clear selection

            # Clear previous options
            for widget in options_frame.winfo_children():
                widget.destroy()

            options = [q[1], q[2], q[3], q[4]]
            for opt in options:
                if opt:  # Only show non-None options
                    tk.Radiobutton(options_frame, text=opt, variable=user_answer, value=opt).pack(anchor="w")

        def submit_answer():
            selected = user_answer.get()
            if not selected:
                return

            correct = questions[current_q[0]][5]
            if selected.strip().lower() == correct.strip().lower():
                score[0] += 1

            current_q[0] += 1
            if current_q[0] < len(questions):
                show_question()
            else:
                question_label.config(text=f"Quiz Complete! You scored {score[0]} out of {len(questions)}.")
                for widget in options_frame.winfo_children():
                    widget.destroy()
                submit_btn.pack_forget()

        question_label = tk.Label(quiz_window, text="", font=("Arial", 12), wraplength=480)
        question_label.pack(pady=20)

        options_frame = tk.Frame(quiz_window)
        options_frame.pack()

        submit_btn = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
        submit_btn.pack(pady=10)

        show_question()

    for label_text, table_name in category_map.items():
        btn = tk.Button(win, text=label_text, width=25, command=lambda t=table_name, l=label_text: start_quiz(t, l))
        btn.pack(pady=5)
