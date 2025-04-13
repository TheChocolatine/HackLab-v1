import tkinter as tk
from scenarios.bruteforce import BruteforceApp
from scenarios.sql_injection import SQLInjectionApp

def run_bruteforce():
    BruteforceApp()

def main_menu():
    root = tk.Tk()
    root.title("HackLab - Simulateur de Hacking")
    root.geometry("500x400")
    root.configure(bg="#101010")

    title = tk.Label(root, text="HackLab", font=("Courier", 24), fg="#00ff88", bg="#101010")
    title.pack(pady=20)

    desc = tk.Label(root, text="Choisissez une simulation", font=("Courier", 12), fg="#00ff88", bg="#101010")
    desc.pack(pady=10)

    btn_brute = tk.Button(root, text="Bruteforce", command=run_bruteforce, width=30)
    btn_brute.pack(pady=10)
    btn_sql = tk.Button(root, text="SQL Injection", command=SQLInjectionApp, width=30)
    btn_sql.pack(pady=10)

    # Ajouts futurs : btn_sql, btn_xss, etc.

    root.mainloop()

if __name__ == "__main__":
    main_menu()
