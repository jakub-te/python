import tkinter as tk

root = tk.Tk()
root.title("Calculator.exe")
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
text=tk.StringVar()
enterclear=False

label = tk.Label(root, textvariable=text,width=30,height=4).grid(row=0,column=0,columnspan=10)

def clicked(thing):
    global enterclear
    if enterclear:
        text.set("")
        enterclear=False
    text.set(text.get()+str(thing))

def clear():
    text.set("")

def enter():
    global enterclear
    try:
        text.set(eval(text.get()))
    except:
        text.set("Syntax ERROR")
    enterclear=True


button_procento = tk.Button(root, text="%",width=10,height=3).grid(row=1,column=0,sticky="W")
button_ce = tk.Button(root, text="CE",width=10,height=3).grid(row=1,column=1,sticky="W")
button_c = tk.Button(root, text="C",command=clear,width=10,height=3).grid(row=1,column=2,sticky="W")
button_backspace = tk.Button(root, text="⌫",width=10,height=3).grid(row=1,column=3,sticky="W")

button_1x = tk.Button(root, text="1/x",width=10,height=3).grid(row=2,column=0,sticky="W")
button_x2 = tk.Button(root, text="x2",width=10,height=3).grid(row=2,column=1,sticky="W")
button_2odmocnina = tk.Button(root, text="2√x",width=10,height=3).grid(row=2,column=2,sticky="W")
button_deleno = tk.Button(root, text="/",command=lambda: clicked("/"),width=10,height=3).grid(row=2,column=3,sticky="W")

button_7 = tk.Button(root, text="7", command=lambda: clicked(7),width=10,height=3).grid(row=3,column=0,sticky="W")
button_8 = tk.Button(root, text="8", command=lambda: clicked(8),width=10,height=3).grid(row=3,column=1,sticky="W")
button_9 = tk.Button(root, text="9", command=lambda: clicked(9),width=10,height=3).grid(row=3,column=2,sticky="W")
button_krat = tk.Button(root, text="*", command=lambda: clicked("*"),width=10,height=3).grid(row=3,column=3,sticky="W")

button_4 = tk.Button(root, text="4", command=lambda: clicked(4),width=10,height=3).grid(row=4,column=0,sticky="W")
button_5 = tk.Button(root, text="5", command=lambda: clicked(5),width=10,height=3).grid(row=4,column=1,sticky="W")
button_6 = tk.Button(root, text="6", command=lambda: clicked(6),width=10,height=3).grid(row=4,column=2,sticky="W")
button_minus = tk.Button(root, text="-", command=lambda: clicked("-"),width=10,height=3).grid(row=4,column=3,sticky="W")


button_1 = tk.Button(root, text="1", command=lambda: clicked(1),width=10,height=3).grid(row=5,column=0,sticky="W")
button_2 = tk.Button(root, text="2", command=lambda: clicked(2),width=10,height=3).grid(row=5,column=1,sticky="W")
button_3 = tk.Button(root, text="3", command=lambda: clicked(3),width=10,height=3).grid(row=5,column=2,sticky="W")
button_plus = tk.Button(root, text="+", command=lambda: clicked("+"),width=10,height=3).grid(row=5,column=3,sticky="W")

button_plusminus = tk.Button(root, text="+/-",width=10,height=3).grid(row=6,column=0,sticky="W")
button_0 = tk.Button(root, text="0", command=lambda: clicked(0),width=10,height=3).grid(row=6,column=1,sticky="W")
button_carka = tk.Button(root, text=",", command=lambda: clicked(","),width=10,height=3).grid(row=6,column=2,sticky="W")
button_rovnitko = tk.Button(root, text="=",width=10,height=3,command=enter).grid(row=6,column=3,sticky="W")



root.minsize(350,400)
root.maxsize(350,400)
root.mainloop()