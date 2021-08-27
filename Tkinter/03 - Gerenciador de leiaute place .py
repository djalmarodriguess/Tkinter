# Um gerenciador de leiaute define a organização do widgets dentro de um container

from tkinter import *

janela = Tk()

#Criar Label
lb = Label(janela, text = 'Hello World!')

#Informa o lugar aonde será mostrado a Label
lb.place(x =110, y = 120)

janela.geometry('300x300+200+200')

janela.mainloop()