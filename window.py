import tkinter as tk
from tkinter import simpledialog, messagebox
from gui.admin_panel import open_admin_panel
from gui.quiz_interface import open_quiz_interface

ADMIN_PASSWORD = "3535"  # INCLUDE IN README

def main():
    root = tk.Tk()
    root.title("Quiz Bowl App")
    root.geometry("300x200")

    label = tk.Label(root, text="Welcome to the Quiz Bowl App!", font=("Arial", 14))
    label.pack(pady=20)

    def handle_admin():
        password = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")
        if password == ADMIN_PASSWORD:
            root.withdraw()
            open_admin_panel(root)
        else:
            messagebox.showerror("Error", "Incorrect password!")

    def handle_quiz():
        root.withdraw()
        open_quiz_interface(root)

    admin_btn = tk.Button(root, text="Admin", width=20, command=handle_admin)
    quiz_btn = tk.Button(root, text="Take Quiz", width=20, command=handle_quiz)

    admin_btn.pack(pady=10)
    quiz_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()