import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

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


#Button "-"
tk.Button(window, text="Upload", bg="gray", fg="black", font=("Arial", 15), command=UploadAction).place(x=200, y=100, width=200, height=40)





#Label Zeit
tk.Label(window, text="00:00",bg="lightgray", font=("Tunga", 15)).place(x=250, y=360, width=100, height=40)

#Zeit zwischen Bild-Suche-Label
tk.Label(window, text="Zeit zwischen jeder Bildsuche",bg="lightgray", font=("Tunga", 10)).place(x=200, y=320, width=200, height=40)

#Button "-"
tk.Button(window, text="-", bg="gray", fg="black", font=("Arial", 15)).place(x=200, y=360, width=50, height=40)

#Button "+"
tk.Button(window, text="+", bg="gray", fg="black", font=("Arial", 15)).place(x=350, y=360, width=50, height=40)

#Button "hinzufügen"
tk.Button(window, text="Save", bg="gray", fg="black", font=("Arial", 15)).place(x=200, y=400, width=200, height=40)


window.mainloop()

