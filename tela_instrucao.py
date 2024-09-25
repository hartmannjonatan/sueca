from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class TelaInstrucao:
        
    def abrir_tela(self):
        janela_instrucao = tk.Toplevel()
        janela_instrucao.title("Instruções de Jogo")
        janela_instrucao.resizable(False, False)

        canvas = Canvas(janela_instrucao, width=600, height=400)

        x = (janela_instrucao.winfo_screenwidth() // 2) - (600 // 2)
        y = (janela_instrucao.winfo_screenheight() // 2) - (400 // 2) - 10
        janela_instrucao.geometry(f"600x400+{x}+{y}")

        imagem_fundo = Image.open("images/tela_instrucao/imagem_tutorial.png")
        imagem_fundo = imagem_fundo.resize((600, 400))

        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
        