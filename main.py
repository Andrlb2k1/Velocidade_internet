# Importando o Tkinter
from tkinter import *

# Importando o Pillow
from PIL import Image, ImageTk

# Cores
co0 = "#f0f3f5"  # Branca 1
co1 = "#feffff"  # Branca 2
co2 = "#3fb5a3"  # Verde
co3 = "#fc766d"  # Vermelha
co4 = "#403d3d"  # Preta/Letra
co5 = "#4a88e8"  # Azul

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('350x200')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela em dois frames
frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando o frame_logo
imagem = Image.open('speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=20, y=0)

l_logo_nome = Label(frame_logo, text='Internet speed test', padx=10, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
l_logo_nome.place(x=75, y=10)

l_logo_linha = Label(frame_logo, width=350, anchor=NW, font=('Ivy 1'), bg=co2)
l_logo_linha.place(x=0, y=57)

janela.mainloop()