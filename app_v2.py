from tkinter import*
import tkinter.font as tkFont
import math
import Exp_10 as exp10

class app():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("400x350")
        self.frame = Frame(self.janela)
        self.frame.pack(side=LEFT)

        # Fontes
        fontStyle1 = tkFont.Font(family="Times", size=20)
        fontStyle2 = tkFont.Font(family="Lucida Grande", size=13)


        # Título
        self.title = Label(self.frame, text="CALCULADORA", font = fontStyle1)
        self.title.grid(row=0, column = 1)
        self.subtitle = Label(self.frame, text="Somatório em PF", font = fontStyle2)
        self.subtitle.grid(row=1, column = 1)

        # Espaçamento
        self.emp = Label(self.frame, text="")
        self.emp.grid(row=2, column = 0)

        
        # Entrada de dados 1
        self.n_value = Label(self.frame, text = "N value = ")
        self.n_value.grid(row=3, column = 0)

        self.e = Entry(self.frame, font=fontStyle1)
        self.e.grid(row=3, column = 1)

        # Espaçamento
        self.emp = Label(self.frame, text="")
        self.emp.grid(row=4, column = 0)

        # Entrada de dados 2
        self.x_value = Label(self.frame, text = "X value = ")
        self.x_value.grid(row=5, column = 0)

        self.e1 = Entry(self.frame, font=fontStyle1)
        self.e1.grid(row=5, column = 1)

        # Espaçamento
        self.emp1 = Label(self.frame, text="")
        self.emp1.grid(row=6, column = 0)

        # Button "igual"
        self.bt = Button(self.frame, text = "=", command = self.conta)
        self.bt.grid(row=7, column = 1)
        self.bt.config(height = 2, width = 5)

        # Resultado
        self.la = Label(self.frame, text="", font = fontStyle1)
        self.la.grid(row=8, column = 1)

        self.janela.mainloop()        

    def conta(self): # CALCULO
        self.n = float(self.e.get())
        self.x = float(self.e1.get())
        self.result = 
        self.la["text"] = self.result
    
            
app()