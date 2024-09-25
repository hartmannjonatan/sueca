from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class TelaPontuacao:

    def abrir_tela(self):
        janela_pontuacao = tk.Toplevel()
        janela_pontuacao.title("Pontuação")
        janela_pontuacao.resizable(False, False)

        canvas = Canvas(janela_pontuacao, width=600, height=400)

        x = (janela_pontuacao.winfo_screenwidth() // 2) - (600 // 2)
        y = (janela_pontuacao.winfo_screenheight() // 2) - (400 // 2) - 10
        janela_pontuacao.geometry(f"600x400+{x}+{y}")

        imagem_fundo = Image.open("images/tela_pontuacao/imagem_pontuacao.png")
        imagem_fundo = imagem_fundo.resize((600, 400))

        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)