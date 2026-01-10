import tkinter as tk 
calculation =""
def add_to_calc(symbol):
   global calculation
   calculation += str(symbol)
   text_result.delete(1.0,"end")
   text_result.insert(1.0,calculation)

def eval_calc():
    global calculation
    try:
         calculation=str(eval(calculation))
       
         text_result.delete(1.0,"end")
         text_result.insert(1.0,calculation)
    except:
     clear_feild()
     text_result.insert(1.0,"Why are u even trying?!")
     pass
def clear_feild():
     global calculation
     calculation=""
     text_result.delete(1.0,"end")
     pass 
root = tk.Tk()
root.geometry("300x275")

text_result=tk.Text(root,height=2,width=16,font=("Ariel",24))
text_result.grid(columnspan=5)
btn_1=tk.Button(root,text="1",command=lambda:add_to_calc(1),width=5,font=("Ariel",14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda:add_to_calc(2),width=5,font=("Ariel",14))
btn_2.grid(row=2,column=2)

btn_1=tk.Button(root,text="3",command=lambda:add_to_calc(3),width=5,font=("Ariel",14))
btn_1.grid(row=2,column=3)

btn_1=tk.Button(root,text="4",command=lambda:add_to_calc(4),width=5,font=("Ariel",14))
btn_1.grid(row=3,column=1)

btn_1=tk.Button(root,text="5",command=lambda:add_to_calc(5),width=5,font=("Ariel",14))
btn_1.grid(row=3,column=2)

btn_1=tk.Button(root,text="6",command=lambda:add_to_calc(6),width=5,font=("Ariel",14))
btn_1.grid(row=3,column=3)

btn_1=tk.Button(root,text="7",command=lambda:add_to_calc(7),width=5,font=("Ariel",14))
btn_1.grid(row=4,column=1)

btn_1=tk.Button(root,text="8",command=lambda:add_to_calc(8),width=5,font=("Ariel",14))
btn_1.grid(row=4,column=2)

btn_1=tk.Button(root,text="9",command=lambda:add_to_calc(9),width=5,font=("Ariel",14))
btn_1.grid(row=4,column=3)

btn_1=tk.Button(root,text="+",command=lambda:add_to_calc("+"),width=5,font=("Ariel",14))
btn_1.grid(row=4,column=4)

btn_1=tk.Button(root,text="-",command=lambda:add_to_calc("-"),width=5,font=("Ariel",14))
btn_1.grid(row=3,column=4)

btn_1=tk.Button(root,text="x",command=lambda:add_to_calc("*"),width=5,font=("Ariel",14))
btn_1.grid(row=2,column=4)

btn_1=tk.Button(root,text="÷",command=lambda:add_to_calc("/"),width=5,font=("Ariel",14))
btn_1.grid(row=1,column=4)

btn_1=tk.Button(root,text="=",command=eval_calc,width=5,font=("Ariel",14))
btn_1.grid(row=5,column=4)

btn_1=tk.Button(root,text="0",command=lambda:add_to_calc(0),width=5,font=("Ariel",14))
btn_1.grid(row=5,column=2)

btn_1=tk.Button(root,text=".",command=lambda:add_to_calc("."),width=5,font=("Ariel",14))
btn_1.grid(row=5,column=3)

btn_1=tk.Button(root,text="x²",command=lambda:add_to_calc("^2"),width=5,font=("Ariel",14))
btn_1.grid(row=5,column=1)

btn_1=tk.Button(root,text="(",command=lambda:add_to_calc("("),width=5,font=("Ariel",14))
btn_1.grid(row=1,column=1)

btn_1=tk.Button(root,text=")",command=lambda:add_to_calc(")"),width=5,font=("Ariel",14))
btn_1.grid(row=1,column=2)

btn_1=tk.Button(root,text="C",command=clear_feild,width=5,font=("Ariel",14))
btn_1.grid(row=1,column=3)

root.mainloop()
