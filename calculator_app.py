import tkinter as tk 
import json
import os 
import webbrowser


def open_easter_egg():
    raw_path = r"C:\Users\bhakt\OneDrive\Desktop\easter_egg\index.html"
    path = raw_path.strip('"')
    if os.path.exists(path):
        webbrowser.open(f"file:///{path}")
    else:
        print("not found:", path)


class CalculatorFrame(tk.Frame):
    def __init__(self, parent, show_notes_callback):
        super().__init__(parent)
        self.show_notes_callback = show_notes_callback
        self.configure(bg="black")

        self.grid_rowconfigure(0, weight=0)  
        self.grid_rowconfigure(1, weight=0)  
        self.grid_rowconfigure(2, weight=0)  
        self.grid_rowconfigure(2, weight=1) 

        for i in range(3, 8):
         self.grid_rowconfigure(i, weight=0)  


        for j in range(6):
            self.grid_columnconfigure(j, weight=1)

        self.history = []
        if os.path.exists("calc_history.json"):
            with open("calc_history.json","r") as f:
                self.history = json.load(f)

        global calculation
        calculation =""

        def add_to_calc(symbol):
            global calculation
            calculation += str(symbol)
            text_result.delete(1.0,"end")
            text_result.insert(1.0,calculation)
            
        def eval_calc():
            global calculation
            expr = calculation.strip()
            if expr == "2+2":
             open_easter_egg()
             clear_feild()
             return

            if expr == "69/67":
                clear_feild()
                self.show_notes_callback()
                return
            try:
                calculation = str(eval(calculation))
                text_result.delete(1.0,"end")
                text_result.insert(1.0,calculation)
            except:
                clear_feild()
                text_result.insert(1.0,"Why are u even trying?!")
                return
            entry = f"{expr} = {calculation}"
            self.history.append(entry)
            self.history_list.insert(tk.END, entry)
            with open("calc_history.json","w") as f:
             json.dump(self.history,f,indent=4)

        def clear_feild():
            global calculation
            calculation=""
            text_result.delete(1.0,"end")

        def backspace():
            global calculation
            calculation = calculation[:-1]
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)

        def on_key(event):
            key = event.keysym
            if key in ("0","1","2","3","4","5","6","7","8","9","KP_0","KP_1","KP_2","KP_3","KP_4","KP_5","KP_6","KP_7","KP_8","KP_9"):
                add_to_calc(key[-1])
            elif key in ("plus", "KP_Add"):
                add_to_calc("+")
            elif key in ("minus", "KP_Subtract"):
                add_to_calc("-")
            elif key in ("asterisk", "KP_Multiply"):
                add_to_calc("*")
            elif key in ("slash", "KP_Divide"):
                add_to_calc("/")
            elif key in ("Return", "KP_Enter"):
                eval_calc()
            elif key == "BackSpace":
                backspace()
            elif key == "Escape":
                clear_feild()
            elif key in ("period", "KP_Decimal"):
                add_to_calc(".")
            return "break"

       
        self.history_visible = False
        toggle_btn = tk.Button(self, text="⬇ History", bg="#111", fg="white")
        toggle_btn.grid(row=0, column=0, columnspan=7, sticky="nsew")

       
        history_frame = tk.Frame(self, bg="black")
        history_frame.grid(row=1, column=0, columnspan=7, sticky="nsew")
        history_frame.grid_remove()

        self.history_list = tk.Listbox(history_frame, bg="black", fg="white")
        self.history_list.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(history_frame, command=self.history_list.yview)
        scroll.pack(side="right", fill="y")
        self.history_list.config(yscrollcommand=scroll.set)

        for item in self.history:
            self.history_list.insert(tk.END, item)

        def toggle_history():
            if self.history_visible:
                history_frame.grid_remove()
                toggle_btn.config(text="⬇")
            else:
                history_frame.grid()
                toggle_btn.config(text="⬆")
            self.history_visible = not self.history_visible

        toggle_btn.config(command=toggle_history)

        text_result=tk.Text(self, height=2, font=("Ariel",24),
            bg="black", fg="white", insertbackground="white")
        text_result.grid(row=2, column=0, columnspan=7, sticky="nsew", padx=4, pady=4)

        btn_1=tk.Button(self,text="1",command=lambda:add_to_calc(1),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=4,column=1,sticky="nsew", padx=2, pady=2)

        btn_2=tk.Button(self,text="2",command=lambda:add_to_calc(2),font=("Ariel",14),bg="#222", fg="white")
        btn_2.grid(row=4,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="3",command=lambda:add_to_calc(3),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=4,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="4",command=lambda:add_to_calc(4),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=5,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="5",command=lambda:add_to_calc(5),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=5,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="6",command=lambda:add_to_calc(6),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=5,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="7",command=lambda:add_to_calc(7),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=6,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="8",command=lambda:add_to_calc(8),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=6,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="9",command=lambda:add_to_calc(9),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=6,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="+",command=lambda:add_to_calc("+"),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=6,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="-",command=lambda:add_to_calc("-"),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=5,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="x",command=lambda:add_to_calc("*"),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=4,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="÷",command=lambda:add_to_calc("/"),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=3,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="=",command=eval_calc,font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=7,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="0",command=lambda:add_to_calc(0),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=7,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text=".",command=lambda:add_to_calc("."),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=7,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="DEL",command=backspace,font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=7,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="(",command=lambda:add_to_calc("("),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=3,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text=")",command=lambda:add_to_calc(")"),font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=3,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="C",command=clear_feild,font=("Ariel",14),bg="#222", fg="white")
        btn_1.grid(row=3,column=3,sticky="nsew", padx=2, pady=2)

        self.winfo_toplevel().bind("<Key>", on_key)
