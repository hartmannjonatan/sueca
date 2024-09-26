from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

from tela_secundaria import TelaSecundaria

class TelaPontuacao(TelaSecundaria):

    def __init__(self):
        super().__init__()

    def configurar_tela(self):
        self.tela.title("Pontuação")
        self.tela.resizable(False, False)

        self.canvas.config(width=600, height=400)

        x = (self.tela.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (400 // 2) - 10
        self.tela.geometry(f"600x400+{x}+{y}")

        imagem_fundo = Image.open("images/tela_pontuacao/imagem_pontuacao2.png")
        imagem_fundo = imagem_fundo.resize((600, 400))

        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)


        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)

        self.nome_jogador1 = Label(self.tela, text="Rodrigo e", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        self.nome_jogador2 = Label(self.tela, text="Henrique", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        self.nome_jogador3 = Label(self.tela, text="Jonathan", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        self.nome_jogador4 = Label(self.tela, text="Ricardo", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        
        self.pontuacao_dupla1 = Label(self.tela, text="52", font=("Arial", 22), bg="#D9D9D9", fg="#0E400D")
        self.pontuacao_dupla2 = Label(self.tela, text="20", font=("Arial", 22), bg="#D9D9D9", fg="#0E400D")

        self.nome_jogador1.place(anchor="center", x=270, y=115)
        self.nome_jogador2.place(anchor="center", x=270, y=145)
        self.nome_jogador3.place(anchor="center", x=480, y=115)
        self.nome_jogador4.place(anchor="center", x=480, y=145)

        self.pontuacao_dupla1.place(anchor="center", x=270, y=200)
        self.pontuacao_dupla2.place(anchor="center", x=480, y=200)

        imagem_galho_dupla1 = Image.open("images/tela_pontuacao/galho2.png")
        imagem_galho_dupla1 = imagem_galho_dupla1.resize((65, 65))
        self.imagem_galho_dupla1 = ImageTk.PhotoImage(imagem_galho_dupla1)

        imagem_galho_dupla2 = Image.open("images/tela_pontuacao/galho1.png")
        imagem_galho_dupla2 = imagem_galho_dupla2.resize((65, 65))
        self.imagem_galho_dupla2 = ImageTk.PhotoImage(imagem_galho_dupla2)

        self.canvas.create_image(270, 270, anchor="center", image=self.imagem_galho_dupla1)    
        self.canvas.create_image(480, 270, anchor="center", image=self.imagem_galho_dupla2)


