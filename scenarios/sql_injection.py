import tkinter as tk
from tkinter import messagebox
from core.score import score

class SQLInjectionApp:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("SQL Injection")
        self.window.geometry("450x250")
        self.window.config(bg="#1e1e1e")

        tk.Label(self.window, text="Nom d'utilisateur:", fg="#00ff88", bg="#1e1e1e").pack(pady=5)
        self.entry_user = tk.Entry(self.window, width=30)
        self.entry_user.pack()

        tk.Label(self.window, text="Mot de passe:", fg="#00ff88", bg="#1e1e1e").pack(pady=5)
        self.entry_pass = tk.Entry(self.window, show="*", width=30)
        self.entry_pass.pack()

        self.button = tk.Button(self.window, text="Connexion", command=self.check_login)
        self.button.pack(pady=15)

        self.status = tk.Label(self.window, text="", fg="#00ff88", bg="#1e1e1e")
        self.status.pack()

    def check_login(self):
        user = self.entry_user.get()
        pw = self.entry_pass.get()
        # Simulation d'une faille : un SQLi classique fonctionne
        if "' OR '1'='1" in user or "' OR '1'='1" in pw:
            self.status.config(text="Accès Admin accordé (SQLi réussi)")
            score.add_points(100)
        else:
            self.status.config(text="Échec de la connexion.")
            score.fail()
