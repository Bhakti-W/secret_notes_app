import tkinter as tk 

class CalculatorFrame(tk.Frame):
    def __init__(self, parent, show_notes_callback):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=0)  
        for i in range(1,6):
         self.grid_rowconfigure(i, weight=1)  


        for j in range(5):
         self.grid_columnconfigure(j, weight=1)
         self.show_notes_callback = show_notes_callback


        global calculation
        calculation =""

        def add_to_calc(symbol):
            global calculation
            calculation += str(symbol)
            text_result.delete(1.0,"end")
            text_result.insert(1.0,calculation)

        def eval_calc():
            global calculation
            if calculation == "69/67":
                calculation = ""
                text_result.delete(1.0,"end")
                self.show_notes_callback()
                return
            try:
                calculation=str(eval(calculation))
                text_result.delete(1.0,"end")
                text_result.insert(1.0,calculation)
            except:
                clear_feild()
                text_result.insert(1.0,"Why are u even trying?!")

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

           if key in "0123456789":
            add_to_calc(key)
           elif key in ("plus", "KP_Add"):
            add_to_calc("+")
           elif key in ("minus", "KP_Subtract"):
            add_to_calc("-")
           elif key in ("asterisk", "KP_Multiply"):
             add_to_calc("*")
           elif key in ("slash", "KP_Divide"):
            add_to_calc("/")
           elif key == "Return":
            eval_calc()
           elif key == "BackSpace":
            backspace()
           elif key == "Escape":
            clear_feild()
           elif key == "period":
            add_to_calc(".")

           self.bind("<Key>", on_key)
           self.focus_set()

        text_result=tk.Text(self, height=2, font=("Ariel",24))
        text_result.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=4, pady=4)

        btn_1=tk.Button(self,text="1",command=lambda:add_to_calc(1),font=("Ariel",14))
        btn_1.grid(row=2,column=1,sticky="nsew", padx=2, pady=2)

        btn_2=tk.Button(self,text="2",command=lambda:add_to_calc(2),font=("Ariel",14))
        btn_2.grid(row=2,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="3",command=lambda:add_to_calc(3),font=("Ariel",14))
        btn_1.grid(row=2,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="4",command=lambda:add_to_calc(4),font=("Ariel",14))
        btn_1.grid(row=3,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="5",command=lambda:add_to_calc(5),font=("Ariel",14))
        btn_1.grid(row=3,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="6",command=lambda:add_to_calc(6),font=("Ariel",14))
        btn_1.grid(row=3,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="7",command=lambda:add_to_calc(7),font=("Ariel",14))
        btn_1.grid(row=4,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="8",command=lambda:add_to_calc(8),font=("Ariel",14))
        btn_1.grid(row=4,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="9",command=lambda:add_to_calc(9),font=("Ariel",14))
        btn_1.grid(row=4,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="+",command=lambda:add_to_calc("+"),font=("Ariel",14))
        btn_1.grid(row=4,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="-",command=lambda:add_to_calc("-"),font=("Ariel",14))
        btn_1.grid(row=3,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="x",command=lambda:add_to_calc("*"),font=("Ariel",14))
        btn_1.grid(row=2,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="÷",command=lambda:add_to_calc("/"),font=("Ariel",14))
        btn_1.grid(row=1,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="=",command=eval_calc,font=("Ariel",14))
        btn_1.grid(row=5,column=4,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="0",command=lambda:add_to_calc(0),font=("Ariel",14))
        btn_1.grid(row=5,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text=".",command=lambda:add_to_calc("."),font=("Ariel",14))
        btn_1.grid(row=5,column=3,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="⌫",command=backspace,font=("Ariel",14))
        btn_1.grid(row=5,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="(",command=lambda:add_to_calc("("),font=("Ariel",14))
        btn_1.grid(row=1,column=1,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text=")",command=lambda:add_to_calc(")"),font=("Ariel",14))
        btn_1.grid(row=1,column=2,sticky="nsew", padx=2, pady=2)

        btn_1=tk.Button(self,text="C",command=clear_feild,font=("Ariel",14))
        btn_1.grid(row=1,column=3,sticky="nsew", padx=2, pady=2)

        self.bind("<Key>", on_key)
        self.focus_set()

