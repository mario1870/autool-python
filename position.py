import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

def add_project():
    project_list.append("Didi")
    print(project_list)

window = tk.Tk()
window.title("Autool")
window.geometry('500x500')

project_list = ["Troll", "LOL"]
# Create a String Object and set the default value
var = tk.Variable(value=project_list)

# Überschrift
tk.Label(window, text="Autool", font=("Tunga", 20)).place(x=200, y=0)

# Aufzählungsbox
lbox = tk.Listbox(window, listvariable=var)
lbox.place(x=10, y=50, height=400, width=150)

#Label Zeit
tk.Label(window, text="Klicke auf den Button und navigiere innerhalb der nächsten 5 Sekunden auf die zu klickende Position",bg="lightgray", font=("Tunga", 15)).place(x=200, y=300, width=200, height=100)

#Button "-"
tk.Button(window, text="Los", bg="gray", fg="black", font=("Arial", 15)).place(x=200, y=360, width=200, height=40)

window.mainloop()

