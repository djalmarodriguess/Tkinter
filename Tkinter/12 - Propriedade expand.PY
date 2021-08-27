'''A propriedade "expand" que quando definida igual a 1 (true) faz com que os componentes tenham um mesmo tamanho proporcional. Assim, se tivermos 3 componentes dentro de um frame com a propriedade "expand" igual a 1, o gerenciador de leiaute Pack irá definir que o tamanho de cada widget seja igual aos demais, de forma a ocupar todo o vídeo.'''

from tkinter import *

janela = Tk()

lb1 = Label(janela, text = 'LINHA 1', bg = 'white')
lb2 = Label(janela, text = 'LINHA 2', bg = 'red')
lb3 = Label(janela, text = 'LINHA 3', bg = 'pink')
lb4 = Label(janela, text = 'LINHA 4', bg = 'yellow')

lb1.pack(side=TOP, fill = BOTH, expand = 1)
lb2.pack(side=TOP, fill = BOTH, expand = 1)
lb3.pack(side=TOP, fill = BOTH, expand = 1)
lb4.pack(side=TOP, fill = BOTH, expand = 1)

janela['bg'] = 'black'
janela.geometry('400x300+200+200')
janela.mainloop()