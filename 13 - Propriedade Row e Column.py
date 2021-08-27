''' Propriedades Row e Column nos permitem definir a linha e a coluna respectivamente.'''
from tkinter import *

janela = Tk()

#Definir a linha e coluna aonde será inserido a Label.
lb1 = Label(janela, text='Label 1')
lb1.grid(row=1, column=1)

janela.geometry('300x400+100+100')
janela.mainloop()