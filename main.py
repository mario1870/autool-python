
import tkinter as tk
from tkinter import messagebox
import autool

def project_ent():
    entry = proj_entry.get()
    if entry in action_list:
        tk.messagebox.showwarning('Warnung', 'Es existiert bereits ein Projekt mit diesem Namen')
    else:
        autor_entry = e2.get()
        if len(entry) and len(autor_entry) >= 4:
            action_list.append(entry)
            project_list.set(action_list)
            autool.new_autool()
        else: tk.messagebox.showwarning('Warnung', 'Der Projektname und der Autorenname muss mindestens 4 Zeichen haben!')

window = tk.Tk()
window.title("Autool")
window.geometry('500x500')

#----------------------------------------------------------

# Variable lengs definieren
action_list = []

# Variable project_list als TK-Variable definieren
project_list = tk.StringVar(value=action_list)

#-------------------------------------------------------------

# Überschrift "Autool"
tk.Label(window, text="Autool", font=("Tunga", 20)).place(x=200, y=0)

# Aufzählungsbox
lbox = tk.Listbox(window, listvariable=project_list)
lbox.place(x=10, y=50, height=400, width=150)

# Projektname + Projektinputfeld
lbl_proj = tk.Label(window, text="Projektname", font=("Tunga", 20))
lbl_proj.place(x=200, y=100, width=200)
proj_entry = tk.Entry(window, width=30)
proj_entry.place(x=200, y=150, width=200)

# Autorname + Autorinputfeld
lbl_autor = tk.Label(window, text="Autor", font=("Tunga", 20))
lbl_autor.place(x=200, y=200, width=200)
e2 = tk.Entry(window, width=30)
e2.place(x=200, y=250, width=200)

#Button "erstellen"
tk.Button(window, text="Projekt erstellen", bg="gray", fg="black", command=project_ent, font=("Arial", 20)).place(x=200, y=300, width=200)

if __name__ == "__main__":
    window.mainloop()


