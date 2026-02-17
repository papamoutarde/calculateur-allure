import tkinter as tk
from tkinter import messagebox

def calculer():
    try:
        VMA = float(entry_vma.get())
        Pourcentage = float(entry_pourcentage.get())
        distance = float(entry_distance.get())

        vitesse = VMA * (Pourcentage / 100)
        temps = (distance * 3.6) / vitesse

        minutes = int(temps // 60)
        secondes = round(temps % 60)

        resultat_label.config(
            text=f"Temps à réaliser : {minutes} min {secondes} sec"
        )

    except ValueError:
        messagebox.showerror("Erreur", "Merci d'entrer uniquement des nombres.")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Calculateur allure")
fenetre.geometry("350x250")

# Labels + champs
tk.Label(fenetre, text="VMA (km/h)").pack()
entry_vma = tk.Entry(fenetre)
entry_vma.pack()

tk.Label(fenetre, text="Pourcentage (%)").pack()
entry_pourcentage = tk.Entry(fenetre)
entry_pourcentage.pack()

tk.Label(fenetre, text="Distance (m)").pack()
entry_distance = tk.Entry(fenetre)
entry_distance.pack()

# Bouton
tk.Button(fenetre, text="Calculer", command=calculer).pack(pady=10)

# Résultat
resultat_label = tk.Label(fenetre, text="")
resultat_label.pack()

# Lancement
fenetre.mainloop()
