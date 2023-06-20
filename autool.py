import tkinter as tk
from tkinter.filedialog import askopenfile
import pyautogui
import customtkinter

# Button Funktionen
def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg'), ('Image Files', '*png')], title="Bild auswählen", initialdir="/")
    global file_name
    file_name = file_path.name
    if file_name is not None:
        update_list("Bild: " + file_name)

def add_break():
    entry_break = entry_pause.get()

    #Wert aus entry zu Liste "langs" hinzufügen
    if len(entry_break) > 0:
        entry_break_as_int = int(entry_break)
        update_list(entry_break_as_int)

def get_position():
    pyautogui.sleep(2)
    global position
    position = pyautogui.position()
    posi_koordinaten.set(position)

def test_position(position):
    pyautogui.moveTo(position)

def add_position():
    entry = position
    update_list(entry)

def add_key(key):
    if key is not None:
        update_list("Down-Taste: " + key)

def add_key_up(key):
    if key is not None:
        update_list("Up-Taste: " + key)

def press_key(key):
    if key is not None:
        update_list("Press-Taste: " + key)

def read_entry_typewrite():
    entry_typewrite = tr.get()
    if len(entry_typewrite) > 0:
        entry_typewrite_as_str = str(entry_typewrite)
        update_list("Eingabe: " + entry_typewrite_as_str)

def delete_last_one():
    if len(action_list) != 0:
        action_list.pop()
        project_list.set(action_list)

def delete_all():
    action_list.clear()
    project_list.set(action_list)


def update_list(var):
    #Wert aus entry zu Liste "langs" hinzufügen
    action_list.append(var)
    #TK-Varible aktualisieren
    project_list.set(action_list)

#Ablauf Funktionen
def start():
    for i in action_list:
        check_typ(i)

def check_typ(i):
    checked_datatyp = type(i)
    if checked_datatyp == pyautogui.Point:
        pyautogui.click(i)

#für Bilder
    if checked_datatyp == int:
        pyautogui.sleep(i)

#für Pause
    if checked_datatyp == str:
        if "Bild" in i:
            located_pic = pyautogui.locateCenterOnScreen(i, grayscale=True, confidence=0.8)
            while located_pic == None:
                pyautogui.sleep(1)
                located_pic = pyautogui.locateCenterOnScreen(i, grayscale=True, confidence=0.8)
            else:
                pyautogui.click(located_pic)

        if "Down-Taste" in i:
            splitted = i.split(" ")
            pyautogui.keyDown(splitted[1])
        if "Up-Taste" in i:
            splitted = i.split(" ")
            pyautogui.keyUp(splitted[1])
        if "Press-Taste" in i:
            splitted = i.split(" ")
            pyautogui.press(splitted[1])
        if "Eingabe" in i:
            splitted = i.split(" ")
            pyautogui.typewrite(splitted[1])

# TK Funktionen

def tk_create_new_button(tk_window, text, cmd, x, y_pos, width=100, height=25):
    tk.Button(tk_window, text=text, command=cmd).place(x=x, y=y_pos, width=width, height=height)

def new_autool():
    window = tk.Tk()
    window.title("Autool")
    window.geometry('500x500')
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#------------------------------------------------------------

    #Variable für Liste definieren
    global action_list
    action_list = []

    # Variable action_list als TK-Variable definieren
    global project_list
    project_list = tk.StringVar(value=action_list)

#--------------------------------------------------------------

    p = ""
    global posi_koordinaten
    posi_koordinaten = tk.StringVar(value=p)

#--------------------------------------------------------------

    # Überschrift "Autool"
    tk.Label(window, text="Autool", font=("Tunga", 20)).place(x=200, y=0)

    # Aufzählungsbox
    lbox = tk.Listbox(window, listvariable=project_list)
    lbox.place(x=10, y=50, height=400, width=150)

    OPTIONS = [
        "enter",
        "left",
        "right",
        'ctrl',
        'alt',
        'shift',
        'win',
        'del',
        'delete',
        'down',
        "tab"
    ]
    global tr
    tr = tk.Entry(window)
    tr.place(x=320, y=35, width=100, height=25)
    tk_create_new_button(window, "Text hinzufügen", read_entry_typewrite, 320, 60, 100)

    variable = tk.StringVar(window)
    variable.set("Press")
    w = tk.OptionMenu(window, variable, *OPTIONS, command=press_key)
    w.place(x=200, y=60, width=100, height=25)

    variable = tk.StringVar(window)
    variable.set("Down")
    w = tk.OptionMenu(window, variable, *OPTIONS, command=add_key)
    w.place(x=200, y=100, width=100, height=25)

    variable = tk.StringVar(window)
    variable.set("Up")
    w = tk.OptionMenu(window, variable, *OPTIONS, command=add_key_up)
    w.place(x=320, y=100, width=100, height=25)

    # Projektname + Projektinputfeld
    tk.Label(window, text="Bild hinzufügen", font=("Tunga", 15)).place(x=200, y=160, width=200)
    #Bild input
    tk_create_new_button(window, "Bild auswählen", open_file, 200, 200, 220)

    # Pause hinzufügen
    tk.Label(window, text="Pause hinzufügen (in Sek.)", font=("Tunga", 12)).place(x=200, y=260, width=200)
    global entry_pause
    entry_pause = tk.Entry(window, width=30)
    entry_pause.place(x=200, y=300, width=100, height=25)

    #Button Pause hinzufügen
    tk_create_new_button(window, "Hinzufügen", add_break, 320, 300)

    # Position hinzufügen
    tk.Label(window, text="Position hinzufügen", font=("Tunga", 15)).place(x=200, y=360, width=200)
    tk.Label(window, width=30, bg="#9AC0CD", textvariable=posi_koordinaten).place(x=200, y=400, width=100, height=25)
    tk_create_new_button(window, "Messen", get_position, 320, 400)
    tk_create_new_button(window, "Hinzufügen", add_position, 200, 450)
    tk_create_new_button(window, "Testen", test_position, 320, 450)


    #button start
    tk_create_new_button(window, "Start", start, 320, 450)

    tk_create_new_button(window, "del. last", delete_last_one, 10, 460, 70)

    tk_create_new_button(window, "del. all", delete_all, 90, 460, 70)

    window.mainloop()

if __name__ == "__main__":
    new_autool()


