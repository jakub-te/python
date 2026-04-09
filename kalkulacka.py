import customtkinter as ctk

class Main(ctk.CTk):
    def __init__(self):

        super().__init__()

        self.title("kalkulacka")
        self.geometry("300x500")

        self.generate_layout()
        self.generate_rows()
        self.generate_buttons()

    def generate_layout(self):
        self.obrazovka = ctk.CTkFrame(self, fg_color="#08081B", corner_radius=0, width=300, height=100)
        self.obrazovka.pack(fill=ctk.X, ipady=5)

        self.klavenice = ctk.CTkFrame(self, fg_color="#161630", corner_radius=0, width=300, height=400)
        self.klavenice.pack(fill=ctk.BOTH, expand=True)

    def generate_rows(self):
        self.radek = ctk.CTkLabel(self.obrazovka, text="", font=("Roboto", 24))
        self.radek.pack(side=ctk.RIGHT, padx=12)

    def generate_buttons(self):
        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)

        btnSize = 50

        self.radek_open = ctk.CTkButton(self.klavenice_radek,text="(",width=btnSize,height=btnSize,command=lambda: self.addToScreen("("))
        self.radek_open.pack(side=ctk.LEFT, padx=10)

        self.radek_close = ctk.CTkButton(self.klavenice_radek,text=")",width=btnSize,height=btnSize,command=lambda: self.addToScreen(")"))
        self.radek_close.pack(side=ctk.LEFT, padx=10)

        self.radek_c = ctk.CTkButton(self.klavenice_radek,text="C",width=btnSize,height=btnSize,command=lambda: self.clearScreen())
        self.radek_c.pack(side=ctk.LEFT, padx=10)

        self.radek_del = ctk.CTkButton(self.klavenice_radek,text="⌫",width=btnSize,height=btnSize,command=lambda: self.deleteScreen())
        self.radek_del.pack(side=ctk.LEFT, padx=10)

        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)


        self.radek_1lomenox = ctk.CTkButton(self.klavenice_radek,text="1/x",width=btnSize,height=btnSize,command=lambda: self.addToScreen(""))
        self.radek_1lomenox.pack(side=ctk.LEFT, padx=10)

        self.radek_x2 = ctk.CTkButton(self.klavenice_radek,text="x2",width=btnSize,height=btnSize,command=lambda: self.addToScreen(""))
        self.radek_x2.pack(side=ctk.LEFT, padx=10)

        self.radek_odmocnina = ctk.CTkButton(self.klavenice_radek,text="2√x",width=btnSize,height=btnSize,command=lambda: self.addToScreen(""))
        self.radek_odmocnina.pack(side=ctk.LEFT, padx=10)

        self.radek_lomeno = ctk.CTkButton(self.klavenice_radek,text="/",width=btnSize,height=btnSize,command=lambda: self.addToScreen("/"))
        self.radek_lomeno.pack(side=ctk.LEFT, padx=10)


        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)


        self.radek7 = ctk.CTkButton(self.klavenice_radek,text="7",width=btnSize,height=btnSize,command=lambda: self.addToScreen("7"))
        self.radek7.pack(side=ctk.LEFT, padx=10)

        self.radek8 = ctk.CTkButton(self.klavenice_radek,text="8",width=btnSize,height=btnSize,command=lambda: self.addToScreen("8"))
        self.radek8.pack(side=ctk.LEFT, padx=10)

        self.radek9 = ctk.CTkButton(self.klavenice_radek,text="9",width=btnSize,height=btnSize,command=lambda: self.addToScreen("9"))
        self.radek9.pack(side=ctk.LEFT, padx=10)

        self.radek_x = ctk.CTkButton(self.klavenice_radek,text="*",width=btnSize,height=btnSize,command=lambda: self.addToScreen("*"))
        self.radek_x.pack(side=ctk.LEFT, padx=10)
        
        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)


        self.radek4 = ctk.CTkButton(self.klavenice_radek,text="4",width=btnSize,height=btnSize,command=lambda: self.addToScreen("4"))
        self.radek4.pack(side=ctk.LEFT, padx=10)

        self.radek5 = ctk.CTkButton(self.klavenice_radek,text="5",width=btnSize,height=btnSize,command=lambda: self.addToScreen("5"))
        self.radek5.pack(side=ctk.LEFT, padx=10)

        self.radek6 = ctk.CTkButton(self.klavenice_radek,text="6",width=btnSize,height=btnSize,command=lambda: self.addToScreen("6"))
        self.radek6.pack(side=ctk.LEFT, padx=10)

        self.radek_minus = ctk.CTkButton(self.klavenice_radek,text="-",width=btnSize,height=btnSize,command=lambda: self.addToScreen("-"))
        self.radek_minus.pack(side=ctk.LEFT, padx=10)       

        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)


        self.radek1 = ctk.CTkButton(self.klavenice_radek,text="1",width=btnSize,height=btnSize,command=lambda: self.addToScreen("1"))
        self.radek1.pack(side=ctk.LEFT, padx=10)

        self.radek2 = ctk.CTkButton(self.klavenice_radek,text="2",width=btnSize,height=btnSize,command=lambda: self.addToScreen("2"))
        self.radek2.pack(side=ctk.LEFT, padx=10)

        self.radek3 = ctk.CTkButton(self.klavenice_radek,text="3",width=btnSize,height=btnSize,command=lambda: self.addToScreen("3"))        
        self.radek3.pack(side=ctk.LEFT, padx=10)

        self.radek_plus = ctk.CTkButton(self.klavenice_radek,text="+",width=btnSize,height=btnSize,command=lambda: self.addToScreen("+"))        
        self.radek_plus.pack(side=ctk.LEFT, padx=10)

        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)


        self.radek7 = ctk.CTkButton(
            self.klavenice_radek,
            text="7",
            width=btnSize,
            height=btnSize,
            command=lambda: self.addToScreen("7")
        )
        self.radek7.pack(side=ctk.LEFT, padx=10)

        self.radek8 = ctk.CTkButton(
            self.klavenice_radek,
            text="8",
            width=btnSize,
            height=btnSize,
            command=lambda: self.addToScreen("8")
        )
        self.radek8.pack(side=ctk.LEFT, padx=10)

        self.radek9 = ctk.CTkButton(
            self.klavenice_radek,
            text="9",
            width=btnSize,
            height=btnSize,
            command=lambda: self.addToScreen("9")
        )
        self.radek9.pack(side=ctk.LEFT, padx=10)
        self.klavenice_radek = ctk.CTkFrame(self.klavenice, fg_color="transparent", corner_radius=0)
        self.klavenice_radek.pack(side=ctk.TOP, pady=12)

    

    def addToScreen(self, message):
        current = self.radek.cget("text")
        self.radek.configure(text=current + message)
    
    def clearScreen(self):
        self.radek.configure(text="")

    def deleteScreen(self):
        current = self.radek.cget("text")
        self.radek.configure(text=current[:-1])




if __name__ == "__main__":
    app = Main()
    app.mainloop()
