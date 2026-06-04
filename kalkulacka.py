import customtkinter as ctk
import cmath

class Main(ctk.CTk):
    enterclear=False
    def __init__(self):

        super().__init__()

        self.title("kalkulacka")
        self.geometry("350x550")
        self.minsize(350,550)
        self.maxsize(500,550)

        self.generate_layout()
        self.generate_rows()
        self.generate_buttons()

    def generate_layout(self):
        self.obrazovka = ctk.CTkFrame(self, fg_color="#08081B", corner_radius=0, width=300, height=50)
        self.obrazovka.pack(fill=ctk.X, ipady=7)

        self.klavenice = ctk.CTkFrame(self, fg_color="#161630", corner_radius=0, width=300, height=400)
        self.klavenice.pack(fill=ctk.BOTH, expand=True)

    def generate_rows(self):
        self.radek = ctk.CTkLabel(self.obrazovka, text="", font=("Roboto", 28))
        self.radek.pack(side=ctk.RIGHT, padx=12, expand=True, fill=ctk.BOTH)


    def generate_buttons(self):
        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.BOTH)

        btnSize = 50
        # prvni radek
        self.radek_open = ctk.CTkButton(self.klavenice_radek,text="(",width=btnSize,height=btnSize,command=lambda: self.addToScreen("("))
        self.radek_open.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_close = ctk.CTkButton(self.klavenice_radek,text=")",width=btnSize,height=btnSize,command=lambda: self.addToScreen(")"))
        self.radek_close.pack(side=ctk.LEFT, padx=10,expand=True, fill=ctk.BOTH)

        self.radek_c = ctk.CTkButton(self.klavenice_radek,text="C",width=btnSize,height=btnSize,command=lambda: self.clearScreen())
        self.radek_c.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_del = ctk.CTkButton(self.klavenice_radek,text="⌫",width=btnSize,height=btnSize,command=lambda: self.deleteScreen())
        self.radek_del.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.X)


        self.radek_1lomenox = ctk.CTkButton(self.klavenice_radek,text="1/x",width=btnSize,height=btnSize,command=lambda: self.addToScreen("1/("))
        self.radek_1lomenox.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

        self.radek_x2 = ctk.CTkButton(self.klavenice_radek,text="^x",width=btnSize,height=btnSize,command=lambda: self.addToScreen("^"))
        self.radek_x2.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

        self.radek_odmocnina = ctk.CTkButton(self.klavenice_radek,text="2√x",width=btnSize,height=btnSize,command=lambda: self.addToScreen("√(("))
        self.radek_odmocnina.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

        self.radek_lomeno = ctk.CTkButton(self.klavenice_radek,text="/",width=btnSize,height=btnSize,command=lambda: self.addToScreen("/"))
        self.radek_lomeno.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)


        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.BOTH)


        self.radek7 = ctk.CTkButton(self.klavenice_radek,text="7",width=btnSize,height=btnSize,command=lambda: self.addToScreen("7"))
        self.radek7.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek8 = ctk.CTkButton(self.klavenice_radek,text="8",width=btnSize,height=btnSize,command=lambda: self.addToScreen("8"))
        self.radek8.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek9 = ctk.CTkButton(self.klavenice_radek,text="9",width=btnSize,height=btnSize,command=lambda: self.addToScreen("9"))
        self.radek9.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_x = ctk.CTkButton(self.klavenice_radek,text="*",width=btnSize,height=btnSize,command=lambda: self.addToScreen("*"))
        self.radek_x.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)
        
        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.BOTH)


        self.radek4 = ctk.CTkButton(self.klavenice_radek,text="4",width=btnSize,height=btnSize,command=lambda: self.addToScreen("4"))
        self.radek4.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek5 = ctk.CTkButton(self.klavenice_radek,text="5",width=btnSize,height=btnSize,command=lambda: self.addToScreen("5"))
        self.radek5.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek6 = ctk.CTkButton(self.klavenice_radek,text="6",width=btnSize,height=btnSize,command=lambda: self.addToScreen("6"))
        self.radek6.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_minus = ctk.CTkButton(self.klavenice_radek,text="-",width=btnSize,height=btnSize,command=lambda: self.addToScreen("-"))
        self.radek_minus.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)       

        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.BOTH)


        self.radek1 = ctk.CTkButton(self.klavenice_radek,text="1",width=btnSize,height=btnSize,command=lambda: self.addToScreen("1"))
        self.radek1.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek2 = ctk.CTkButton(self.klavenice_radek,text="2",width=btnSize,height=btnSize,command=lambda: self.addToScreen("2"))
        self.radek2.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek3 = ctk.CTkButton(self.klavenice_radek,text="3",width=btnSize,height=btnSize,command=lambda: self.addToScreen("3"))        
        self.radek3.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_plus = ctk.CTkButton(self.klavenice_radek,text="+",width=btnSize,height=btnSize,command=lambda: self.addToScreen("+"))        
        self.radek_plus.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.BOTH)


        

        self.radek0 = ctk.CTkButton(self.klavenice_radek,text="0",width=btnSize,height=btnSize,command=lambda: self.addToScreen("0"))
        self.radek0.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_carka = ctk.CTkButton(self.klavenice_radek,text=".",width=btnSize,height=btnSize,command=lambda: self.addToScreen("."))
        self.radek_carka.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_neg  = ctk.CTkButton(self.klavenice_radek,text="+/-",width=btnSize,height=btnSize,command=lambda: self.negation())
        self.radek_neg.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)

        self.radek_konec = ctk.CTkButton(self.klavenice_radek,text="=",width=btnSize,height=btnSize,command=lambda: self.enter())
        self.radek_konec.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.BOTH)


        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12, expand=True, fill=ctk.BOTH)

    
    def addToScreen(self, message):
        
        current = self.radek.cget("text")
        if self.enterclear:
            current=""
            self.enterclear=False
        self.radek.configure(text=current + message)
    
    def clearScreen(self):
        self.radek.configure(text="")

    def deleteScreen(self):
        current = self.radek.cget("text")
        self.radek.configure(text=current[:-1])

    def enter(self):
        
        print("get it")
        try:
            res=eval(self.radek.cget("text").replace("^","**").replace("√(", "abs(cmath.sqrt"))
            if res==int(res):
                res=int(res)
            self.radek.configure(text=str(res))
        except:
            self.radek.configure(text="SYNTAX Error")
            self.enterclear=True
    
    def negation(self):
        texts=self.radek.cget("text")
        print(texts[0])
        texts=list(texts)
        if texts[0]=="-":
            texts.pop(0)
        else:
            texts.insert(0,"-")
        ress="".join(texts)
        self.radek.configure(text=ress)
        
            
        




if __name__ == "__main__":
    app = Main()
    app.mainloop()