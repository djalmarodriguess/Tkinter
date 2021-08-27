from tkinter import *

janela = Tk()

#Modificar título
janela.title('Janela Principal')

#Alterar cor de fundo da janela com 'background' ou 'bg'
janela['bg'] = 'red'

#Definir tamanho 
#L(largura)xA(Altura)+E(Distância da borda esquesda)+T(Distância com relação ao topo)
#300x300+100+100
janela.geometry('700x300+100+100')






janela.mainloop()