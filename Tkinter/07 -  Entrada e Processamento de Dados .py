from tkinter import *


def soma():
    #Verificar se os valores são númericos, se forem, desem ser passados para inteiros e efetur a soma
    if str(valor1.get()).isnumeric() and str(valor2.get()).isnumeric():
        lb['text'] = int(valor1.get()) + int(valor2.get())
    
    #Caso algum valor inserido não seja numerico, a mensagem de erro aparece
    else:
        lb['text'] = 'Valor informado inválido'


janela = Tk()

#Entra com um valores para somar 
valor1 = Entry(janela)
valor1.place(x= 90, y = 100)
valor2 = Entry(janela)
valor2.place(x= 90, y = 130)

#Criar botão 
botao = Button(janela, width=20, text= 'SOMAR', command=soma)
botao.place(x = 80, y = 150)

#Criar Label, aonde será mostrado o resultado digitado após apertar o botão.
lb = Label(janela, text='Label')
lb.place(x = 100, y = 180)

janela.geometry('300x300+300+300')
janela.mainloop()