import tkinter as tk
import time
import threading

# Liste fictive de mots de passe (wordlist)
wordlist = ["1234", "password", "admin", "letmein", "qwerty", "pass123", "toor", "root"]
real_password = "toor"

class BruteforceApp:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Simulation Bruteforce")
        self.window.geometry("400x300")
        self.window.config(bg="#1e1e1e")

        self.label = tk.Label(self.window, text="Attaque en cours...", fg="white", bg="#1e1e1e", font=("Courier", 14))
        self.label.pack(pady=20)

        self.progress = tk.Label(self.window, text="", fg="#00ff88", bg="#1e1e1e", font=("Courier", 12))
        self.progress.pack(pady=10)

        self.result = tk.Label(self.window, text="", fg="red", bg="#1e1e1e", font=("Courier", 12))
        self.result.pack(pady=10)

        self.button = tk.Button(self.window, text="Lancer l'attaque", command=self.start_attack, width=25)
        self.button.pack(pady=20)

    def start_attack(self):
        self.button.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.bruteforce)
        thread.start()

    def bruteforce(self):
        start_time = time.time()
        for i, password in enumerate(wordlist):
            self.progress.config(text=f"Tentative {i+1}: '{password}'")
            time.sleep(0.8)
            if password == real_password:
                elapsed = round(time.time() - start_time, 2)
                self.result.config(text=f"\nMot de passe trouvé: '{password}' en {elapsed} sec")
                return
        self.result.config(text="\nMot de passe non trouvé.")
