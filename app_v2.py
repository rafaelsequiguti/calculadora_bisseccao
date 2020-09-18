from tkinter import*
import tkinter.font as tkFont
import math
import bissecao as bissecao
import newton as newton

class app():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("400x700")
        self.frame = Frame(self.janela)
        self.frame.pack(side=LEFT)

        # Fontes
        fontStyle1 = tkFont.Font(family="Times", size=20)
        fontStyle2 = tkFont.Font(family="Lucida Grande", size=13)


        # Título
        self.title = Label(self.frame, text="CALCULADORA", font = fontStyle1)
        self.title.grid(row=0, column = 1)
        self.subtitle = Label(self.frame, text="Método da Bissecção", font = fontStyle2)
        self.subtitle.grid(row=1, column = 1)

        # Espaçamento
        self.emp = Label(self.frame, text="")
        self.emp.grid(row=2, column = 0)

        
        # Entrada de dados 1
        self.n_value = Label(self.frame, text = "a = ")
        self.n_value.grid(row=3, column = 0)

        self.e = Entry(self.frame, font=fontStyle1)
        self.e.grid(row=3, column = 1)

        # Espaçamento
        self.emp = Label(self.frame, text="")
        self.emp.grid(row=4, column = 0)

        # Entrada de dados 2
        self.x_value = Label(self.frame, text = "b = ")
        self.x_value.grid(row=5, column = 0)

        self.e1 = Entry(self.frame, font=fontStyle1)
        self.e1.grid(row=5, column = 1)

        # Espaçamento
        self.emp1 = Label(self.frame, text="")
        self.emp1.grid(row=6, column = 0)
        
        # Entrada de dados 3
        self.epslon = Label(self.frame, text = "Epslon = ")
        self.epslon.grid(row=7, column = 0)

        self.epslon_entry = Entry(self.frame, font=fontStyle1)
        self.epslon_entry.grid(row=7, column = 1)
        
        # Espaçamento
        self.emp2 = Label(self.frame, text="")
        self.emp2.grid(row=8, column = 0)

        # Button "igual"
        self.bt2 = Button(self.frame, text = "=", command = self.conta_bissecaao)
        self.bt2.grid(row=9, column = 1)
        self.bt2.config(height = 2, width = 5)

        # Resultado
        self.biss = Label(self.frame, text="", font = fontStyle1)
        self.biss.grid(row=10, column = 1)

        # Espaçamento
        self.emp2 = Label(self.frame, text="")
        self.emp2.grid(row=11, column = 0)

    ############################################################################################################
        # Título

        self.subtitle = Label(self.frame, text="Método de Newton", font = fontStyle2)
        self.subtitle.grid(row=12, column = 1)

        # Espaçamento
        self.emp = Label(self.frame, text="")
        self.emp.grid(row=13, column = 0)

        
        # Entrada de dados 1
        self.chute_value = Label(self.frame, text = "Chute = ")
        self.chute_value.grid(row=14, column = 0)

        self.chute = Entry(self.frame, font=fontStyle1)
        self.chute.grid(row=14, column = 1)

        # Espaçamento
        self.emp = Label(self.frame, text="")
        self.emp.grid(row=15, column = 0)

        # Entrada de dados 2
        self.epslon2 = Label(self.frame, text = "Epslon = ")
        self.epslon2.grid(row=16, column = 0)

        self.epslon2_entry = Entry(self.frame, font=fontStyle1)
        self.epslon2_entry.grid(row=16, column = 1)

        
        # Espaçamento
        self.emp1 = Label(self.frame, text="")
        self.emp1.grid(row=17, column = 0)

        # Button "igual"
        self.bt = Button(self.frame, text = "=", command = self.conta_newton)
        self.bt.grid(row=18, column = 1)
        self.bt.config(height = 2, width = 5)

        # Resultado
        self.newt = Label(self.frame, text="", font = fontStyle1)
        self.newt.grid(row=19, column = 1)

        self.janela.mainloop()        

    def conta_bissecaao(self): # CALCULO
        self.n = float(self.e.get())
        self.x = float(self.e1.get())
        self.eps = float(self.epslon_entry.get())
        self.result = float(bissecao.bisseccao(self.n,self.x,self.eps))
        self.biss["text"] = self.result

    def conta_newton(self):
        self.entry1 = float(self.chute.get())
        self.entry2 = float(self.epslon2_entry.get())
        self.result = float(newton.newton(self.entry1,self.entry2))
        self.newt["text"] = self.result
        
app()