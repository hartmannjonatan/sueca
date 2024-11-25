from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

from images import IMAGES_DIR

from .tela_secundaria import TelaSecundaria
from dominio_problema.dupla import Dupla


class TelaPontuacao(TelaSecundaria):

    def __init__(self):
        super().__init__()

        self._pontuacao_dupla1: Label = None
        self._pontuacao_dupla2: Label = None
        self._nome_jogador1: Label = None
        self._nome_jogador2: Label = None
        self._nome_jogador3: Label = None
        self._nome_jogador4: Label = None
        self.configurar_tela()

    def configurar_tela(self):
        self.tela.title("Pontuação")
        self.tela.resizable(False, False)

        self.canvas.config(width=600, height=400)

        x = (self.tela.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (400 // 2) - 10
        self.tela.geometry(f"600x400+{x}+{y}")

        imagem_fundo = Image.open(IMAGES_DIR / "tela_pontuacao/imagem_pontuacao.png")
        imagem_fundo = imagem_fundo.resize((600, 400))

        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)


        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)

        self.nome_jogador1 = Label(self.tela, text=f"Jogador1 e", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        self.nome_jogador3 = Label(self.tela, text="Jogdor2", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        self.nome_jogador2 = Label(self.tela, text="Jogador3 e", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        self.nome_jogador4 = Label(self.tela, text="Jogador4", font=("Arial", 18), bg="#D9D9D9", fg="#0E400D")
        
        self.pontuacao_dupla1 = Label(self.tela, text="0", font=("Arial", 22), bg="#D9D9D9", fg="#0E400D")
        self.pontuacao_dupla2 = Label(self.tela, text="0", font=("Arial", 22), bg="#D9D9D9", fg="#0E400D")

        self.nome_jogador1.place(anchor="center", x=270, y=115)
        self.nome_jogador3.place(anchor="center", x=270, y=145)
        self.nome_jogador2.place(anchor="center", x=480, y=115)
        self.nome_jogador4.place(anchor="center", x=480, y=145)

        self.pontuacao_dupla1.place(anchor="center", x=270, y=200)
        self.pontuacao_dupla2.place(anchor="center", x=480, y=200)

        imagem_galho_dupla1 = Image.open(IMAGES_DIR / "tela_pontuacao/galho0.png")
        imagem_galho_dupla1 = imagem_galho_dupla1.resize((65, 65))
        self.imagem_galho_dupla1 = ImageTk.PhotoImage(imagem_galho_dupla1)

        imagem_galho_dupla2 = Image.open(IMAGES_DIR / "tela_pontuacao/galho0.png")
        imagem_galho_dupla2 = imagem_galho_dupla2.resize((65, 65))
        self.imagem_galho_dupla2 = ImageTk.PhotoImage(imagem_galho_dupla2)

        self.canvas.create_image(270, 270, anchor="center", image=self.imagem_galho_dupla1)    
        self.canvas.create_image(480, 270, anchor="center", image=self.imagem_galho_dupla2)
    
    def atualizar_tela_pontuacao(self, dupla1: Dupla, dupla2: Dupla):
        self.nome_jogador1.config(text=f"{dupla1.jogadores[0].nome} e")
        self.nome_jogador3.config(text=f"{dupla1.jogadores[1].nome}")
        self.nome_jogador2.config(text=f"{dupla2.jogadores[0].nome} e")
        self.nome_jogador4.config(text=f"{dupla2.jogadores[1].nome}")

        self.pontuacao_dupla1.config(text=str(dupla1.pontuacao.pontos))
        self.pontuacao_dupla2.config(text=str(dupla2.pontuacao.pontos))

        imagem_galho_dupla1 = Image.open(IMAGES_DIR / f"tela_pontuacao/galho{4 if dupla1.pontuacao.galhos >= 4 else dupla1.pontuacao.galhos}.png")
        imagem_galho_dupla1 = imagem_galho_dupla1.resize((65, 65))
        self.imagem_galho_dupla1 = ImageTk.PhotoImage(imagem_galho_dupla1)

        imagem_galho_dupla2 = Image.open(IMAGES_DIR / f"tela_pontuacao/galho{4 if dupla2.pontuacao.galhos >= 4 else dupla2.pontuacao.galhos}.png")
        imagem_galho_dupla2 = imagem_galho_dupla2.resize((65, 65))
        self.imagem_galho_dupla2 = ImageTk.PhotoImage(imagem_galho_dupla2)

        self.canvas.create_image(270, 270, anchor="center", image=self.imagem_galho_dupla1)    
        self.canvas.create_image(480, 270, anchor="center", image=self.imagem_galho_dupla2)

    @property
    def pontuacao_dupla1(self) -> Label:
        return self._pontuacao_dupla1
    
    @pontuacao_dupla1.setter
    def pontuacao_dupla1(self, pontuacao):
        self._pontuacao_dupla1 = pontuacao

    @property
    def pontuacao_dupla2(self) -> Label:
        return self._pontuacao_dupla2
    
    @pontuacao_dupla2.setter
    def pontuacao_dupla2(self, pontuacao):
        self._pontuacao_dupla2 = pontuacao

    @property
    def nome_jogador1(self) -> Label:
        return self._nome_jogador1
    
    @nome_jogador1.setter
    def nome_jogador1(self, nome):
        self._nome_jogador1 = nome

    @property
    def nome_jogador2(self) -> Label:
        return self._nome_jogador2
    
    @nome_jogador2.setter
    def nome_jogador2(self, nome):
        self._nome_jogador2 = nome

    @property
    def nome_jogador3(self) -> Label:
        return self._nome_jogador3
    
    @nome_jogador3.setter
    def nome_jogador3(self, nome):
        self._nome_jogador3 = nome

    @property
    def nome_jogador4(self) -> Label:
        return self._nome_jogador4
    
    @nome_jogador4.setter
    def nome_jogador4(self, nome):
        self._nome_jogador4 = nome





