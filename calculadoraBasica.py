from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Calculadora Básica")
menu_inicial.iconbitmap("imagens/icon.ico")

#dimensões da janela
largura = 500
altura = 500

#resolução do sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

#posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#definir a geometry
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label1 = Label(menu_inicial, text = "label1", font = "Arial 20", bg = "red")
label2 = Label(menu_inicial, text = "label2", font = "Arial 20", bg = "green")
label3 = Label(menu_inicial, text = "label3", font = "Arial 20", bg = "blue")
#label1.pack()
#label2.pack()

btn1 = Button(menu_inicial, text = "Click1")
btn2 = Button(menu_inicial, text = "Click2")
btn3 = Button(menu_inicial, text = "Click3")

label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
label3.grid(row = 0, column = 2)

btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)

menu_inicial.mainloop()