import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from reportlab.pdfgen import canvas

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Interactif")

        self.student_name = tk.StringVar()
        self.student_class = tk.StringVar()

        tk.Label(root, text="Nom :", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(root, textvariable=self.student_name, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Classe :", font=("Arial", 12)).pack(pady=5)
        self.class_entry = tk.Entry(root, textvariable=self.student_class, font=("Arial", 12))
        self.class_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Commencer le Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        if not self.student_name.get() or not self.student_class.get():
            messagebox.showwarning("Erreur", "Veuillez entrer votre nom et classe.")
            return

        self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0

        self.show_question()

    def load_questions(self):
        conn = sqlite3.connect("C:/Users/hp/PycharmProjects/Projet_TIC_Education/database/quiz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT question, option1, option2, option3, correct_option FROM questions")
        questions = cursor.fetchall()
        conn.close()
        return questions

    def show_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.q_label = tk.Label(self.root, text=q[0], font=("Arial", 14))
            self.q_label.pack(pady=10)

            self.options_buttons = []
            for i in range(3):
                btn = tk.Button(self.root, text=q[i+1], command=lambda i=i: self.check_answer(i))
                btn.pack(pady=5)
                self.options_buttons.append(btn)
        else:
            self.show_result()

    def check_answer(self, i):
        correct = int(self.questions[self.current_question][4]) - 1
        if i == correct:
            self.score += 1
        self.current_question += 1
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Résultat", f"{self.student_name.get()}, Score : {self.score}")

        conn = sqlite3.connect("database/quiz.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO resultats (nom, classe, score, date) VALUES (?, ?, ?, ?)",
                       (self.student_name.get(), self.student_class.get(), self.score, datetime.now().strftime("%Y-%m-%d")))
        conn.commit()
        conn.close()

        self.generate_pdf()

    def generate_pdf(self):
        file = f"reports/{self.student_name.get()}_{self.student_class.get()}.pdf"
        c = canvas.Canvas(file)
        c.drawString(100, 700, f"Nom : {self.student_name.get()}")
        c.drawString(100, 670, f"Classe : {self.student_class.get()}")
        c.drawString(100, 640, f"Score : {self.score}")
        c.save()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
