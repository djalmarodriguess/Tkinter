'''Função fill preenche todo espaço que foi definido'''

from tkinter import *

janela = Tk()

#Informar a função qual o sentido, X ou Y, 
#Sendo X = Horizontal e Y = Vertical
lb1 = Label(janela, text='Horizontal', bg = 'red')
lb1.pack(side=TOP, fill = X)
lb2 = Label(janela, text='', bg = 'red')
lb2.pack(side=RIGHT, fill = Y)
lb3 = Label(janela, text='', bg = 'red')
lb3.pack(side=LEFT, fill = Y)

janela.geometry('300x300+100+100')
janela,mainloop()