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

        imagem_fundo = Image.open("images/tela_pontuacao/imagem_pontuacao.png")
        imagem_fundo = imagem_fundo.resize((600, 400))

        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
