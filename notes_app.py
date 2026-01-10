import tkinter as tk
from tkinter import ttk,messagebox
import json 

class NotesFrame(tk.Frame):
    def __init__(self, parent,show_calc_callback,root):
        super().__init__(parent)
        self.show_calc_callback = show_calc_callback
        root.geometry("500x500")

        notes={}
        try:
            with open("notes.json", "r") as f:
                notes = json.load(f)
        except FileNotFoundError:
            pass

        notebook = ttk.Notebook(self)
        notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        def add_note():
            note_frame = ttk.Frame(notebook, padding=10)
            notebook.add(note_frame, text="New Note")

            title_entry = ttk.Entry(note_frame, width=40)
            title_entry.grid(row=0, column=1)

            content_entry = tk.Text(note_frame, width=40, height=10)
            content_entry.grid(row=1, column=1)

            ttk.Label(note_frame, text="Title").grid(row=0,column=0)
            ttk.Label(note_frame, text="Content").grid(row=1,column=0)

            def save_note():
                title = title_entry.get().strip()
                content = content_entry.get("1.0", tk.END).strip()
                if not title:
                    messagebox.showerror("Error", "Title cannot be empty")
                    return

                notes[title] = content
                with open("notes.json","w") as f:
                    json.dump(notes,f)

                notebook.forget(notebook.select())

                frame = ttk.Frame(notebook)
                text = tk.Text(frame)
                text.insert("1.0", content)
                text.pack(expand=True, fill="both")
                notebook.add(frame, text=title)

            ttk.Button(note_frame, text="Save", command=save_note).grid(row=2,column=1)

        def load_notes():
            try:
                with open("notes.json","r") as f:
                    loaded = json.load(f)
                for title,content in loaded.items():
                    frame = ttk.Frame(notebook)
                    text = tk.Text(frame)
                    text.insert("1.0", content)
                    text.pack(expand=True, fill="both")
                    notebook.add(frame, text=title)
            except:
                pass

        def delete_note():
            tab = notebook.select()
            title = notebook.tab(tab,"text")
            if messagebox.askyesno("Delete", f"Delete {title}?"):
                notebook.forget(tab)
                notes.pop(title,None)
                with open("notes.json","w") as f:
                    json.dump(notes,f)

        load_notes()

        control = tk.Frame(self)
        control.pack()

        ttk.Button(control, text="New Note", command=add_note).pack(side=tk.LEFT)
        ttk.Button(control, text="Delete", command=delete_note).pack(side=tk.LEFT)
        ttk.Button(control, text="Back", command=self.show_calc_callback).pack(side=tk.LEFT)
