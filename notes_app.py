import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class NotesFrame(tk.Frame):
    def __init__(self, parent, show_calc_callback, root):
        super().__init__(parent)
        self.show_calc_callback = show_calc_callback
        root.geometry("500x500")

        self.notes = {}
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                self.notes = json.load(f)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.build_tabs()

        control = tk.Frame(self)
        control.pack(pady=5)

        ttk.Button(control, text="New Note", command=self.new_note).pack(side="left", padx=5)
        ttk.Button(control, text="Delete", command=self.delete_note).pack(side="left", padx=5)
        ttk.Button(control, text="Back", command=self.show_calc_callback).pack(side="left", padx=5)

    def save_file(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f, indent=4)

    def clear_tabs(self):
        for tab in self.notebook.tabs():
            self.notebook.forget(tab)

    def build_tabs(self):
        self.clear_tabs()
        for title, data in self.notes.items():
            content = data["content"] if isinstance(data, dict) else data
            color = data.get("color","white") if isinstance(data, dict) else "white"
            self.create_tab(title, content, color)

    def create_tab(self, title, content, color):
        frame = tk.Frame(self.notebook)
        frame.pack(fill="both", expand=True)

        frame.text = tk.Text(frame, bg=color)
        frame.text.insert("1.0", content)
        frame.text.config(state="disabled")
        frame.text.pack(fill="both", expand=True, padx=10, pady=10)

        frame.color_var = tk.StringVar(value=color)
        color_menu = ttk.Combobox(frame, textvariable=frame.color_var,values=["white","lightblue","lightpink","lightyellow","lightgreen"],state="readonly", width=12)
        color_menu.pack(side="left", padx=5)

        def enable_edit():
            frame.text.config(state="normal")

        def save_edit():
            new_content = frame.text.get("1.0", tk.END).strip()
            new_color = frame.color_var.get()
            self.notes[title] = {"content": new_content, "color": new_color}
            self.save_file()
            frame.text.config(state="disabled", bg=new_color)

        ttk.Button(frame, text="Edit", command=enable_edit).pack(side="left", padx=5)
        ttk.Button(frame, text="Save Edit", command=save_edit).pack(side="left", padx=5)

        self.notebook.add(frame, text=title)

    def new_note(self):
        frame = tk.Frame(self.notebook)
        frame.pack(fill="both", expand=True)

        title_entry = ttk.Entry(frame)
        title_entry.pack(pady=5)

        color_var = tk.StringVar(value="white")
        color_menu = ttk.Combobox(frame, textvariable=color_var,values=["white","lightblue","lightpink","lightyellow","lightgreen"],state="readonly")
        color_menu.pack(pady=5)

        text = tk.Text(frame)
        text.pack(fill="both", expand=True, padx=10, pady=10)

        def save():
            title = title_entry.get().strip()
            if not title:
                messagebox.showerror("Error", "Title cannot be empty")
                return
            self.notes[title] = {"content": text.get("1.0", tk.END).strip(),"color": color_var.get()}
            self.save_file()
            self.build_tabs()

        ttk.Button(frame, text="Save", command=save).pack(pady=5)

        self.notebook.add(frame, text="New Note")
        self.notebook.select(frame)

    def delete_note(self):
        tab = self.notebook.select()
        if not tab:
            return
        title = self.notebook.tab(tab, "text")
        if title == "New Note":
            self.notebook.forget(tab)
            return
        if messagebox.askyesno("Delete", f"Delete {title}?"):
            self.notes.pop(title, None)
            self.save_file()
            self.build_tabs()
