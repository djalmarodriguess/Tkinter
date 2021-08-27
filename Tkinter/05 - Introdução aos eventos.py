'''Exemplo de como definir uma função generica, criando dois botões definindo apenas uma função.  '''


from tkinter import *
from functools import partial
'''Fução partial é uma forma que temos de escrever outra função, no qual 
passamos o nome da função e na seguencia o parâmetro que devem está contidos na função chamada'''

def bt_click(botao):
    print(botao['text'])

janela = Tk()

botao1 = Button(janela, width=20, text= 'Botão 1')
botao1.place(x = 80, y = 80)
botao1['command'] = partial(bt_click, botao1)

botao2 = Button(janela, width=20, text= 'Botão 2')
botao2.place(x = 80, y = 120)
botao2['command'] = partial(bt_click, botao2)

janela.geometry('300x300+100+100')
janela.mainloop()