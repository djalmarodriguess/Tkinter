'''Gerenciador que empacota todas path em uma determinada ordem'''

from tkinter import *

janela = Tk()

lb1 = Label(janela, text = 'Label 1', bg = 'red')
lb2 = Label(janela, text = 'Label 2', bg = 'green')
lb3 = Label(janela, text = 'Label 3', bg = 'blue')
lb4 = Label(janela, text = 'Label 4', bg = 'yellow')


#Adicionar ao gerenciador de leiaute pack
lb1.pack()
lb2.pack(side=RIGHT)
lb3.pack()
lb4.pack(side=BOTTOM)


janela.geometry('300x300+200+200')
janela.mainloop()