from tkinter import *

def click():
    print(ed.get())
    #Label recebe o valor de "ed" chamando a função "get()"
    lb['text'] = ed.get()

janela = Tk()

#Entra com um valor 
ed = Entry(janela)
ed.place(x= 90, y = 100)

#Criar botão 
botao = Button(janela, width=20, text= 'Mostrar', command=click)
botao.place(x = 80, y = 130)

#Criar Label, aonde será mostrado o valor digitado após apertar o botão.
lb = Label(janela, text='Label')
lb.place(x = 100, y = 160)

janela.geometry('300x300+300+300')
janela.mainloop()