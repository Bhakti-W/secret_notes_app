import tkinter as tk
from calculator_app import CalculatorFrame
from notes_app import NotesFrame

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

def show_calc():
    notes.pack_forget()
    calc.pack(fill="both", expand=True)

def show_notes():
    calc.pack_forget()
    notes.pack(fill="both", expand=True)

calc = CalculatorFrame(root, show_notes)
notes = NotesFrame(root, show_calc,root)

calc.pack(fill="both", expand=True)

root.mainloop()
