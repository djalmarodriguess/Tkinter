from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Login: ')
lb2 = Label(janela, text='Senha: ')

lb1.grid(row=1, column=1)
lb2.grid(row=2, column=1)

entrar_login = Entry(janela)
entrar_senha = Entry(janela)

entrar_login.grid(row=1, column=2)
entrar_senha.grid(row=2, column=2)

botao = Button(janela, text='Entrar')
botao.grid(row=3, column=2)

janela.geometry('200x100+100+100')
janela.mainloop()