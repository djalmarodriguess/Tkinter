from tkinter import *

janela = Tk()

#Criar função para mostrar mensagem no TERMINAL após o botão ser clicado
def bt_click():
    #print('Logado')

#Modificar a Label para mostrar a mensagem na JANELA após clicar o botão
    lb['text'] = 'Logado'

#Criar Botão, entrar com parametro "command" e informa a função.
#OBS: Ao chamar a função no command não colocar as parênteses.
bt = Button(janela, width = 20, text ="Entrar", command=bt_click)

#Informa o lugar aonde será mostrado o botão
bt.place(x =75, y = 120)

lb = Label(janela, text ="Hello World")

lb.place(x =120, y = 150)

janela.geometry('300x300+200+200')

janela.mainloop()