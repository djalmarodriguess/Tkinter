'''Gerenciador que empacota todas path em uma determinada ordem'''

from tkinter import *

janela = Tk()

lb1 = Label(janela, text = 'TOP', bg = 'white')
lb2 = Label(janela, text = 'RIGHT', bg = 'white')
lb3 = Label(janela, text = 'BOTTOM', bg = 'white')
lb4 = Label(janela, text = 'LEFT', bg = 'white')


#Adicionar ao gerenciador de leiaute pack
lb1.pack(side=TOP)
lb2.pack(side=RIGHT)
lb3.pack(side=BOTTOM)
lb4.pack(side=LEFT)

janela['bg'] = 'black'
janela.geometry('400x300+200+200')
janela.mainloop()