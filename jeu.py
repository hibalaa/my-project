import tkinter as tk
import random


def play(choice):
    options = ["Pierre", "Papier", "Ciseaux"]
    computer_choice = random.choice(options)
    result = ""
    
    if choice == computer_choice:
        result = "Égalité !"
    elif (choice == "Pierre" and computer_choice == "Ciseaux") or \
         (choice == "Papier" and computer_choice == "Pierre") or \
         (choice == "Ciseaux" and computer_choice == "Papier"):
        result = "Tu as gagné !"
    else:
        result = "L'ordinateur a gagné !"
    
    label_result.config(text=f"Ordinateur : {computer_choice}\n{result}")


root = tk.Tk()
root.title("Pierre Papier Ciseaux")
root.geometry("300x250")


label = tk.Label(root, text="Choisis : Pierre, Papier ou Ciseaux", font=("Arial", 12))
label.pack(pady=10)


frame = tk.Frame(root)
frame.pack()

for choix in ["Pierre", "Papier", "Ciseaux"]:
    tk.Button(frame, text=choix, command=lambda c=choix: play(c)).pack(side=tk.LEFT, padx=5)


label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=20)


tk.mainloop()
