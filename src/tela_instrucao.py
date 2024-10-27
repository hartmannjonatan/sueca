from tkinter import *
from PIL import Image, ImageTk

from images import IMAGES_DIR

from tela_secundaria import TelaSecundaria


class TelaInstrucao(TelaSecundaria):

    def __init__(self):
        super().__init__()
        self.configurar_tela()
        
    def configurar_tela(self):
        self.tela.title("Instruções de Jogo")
        self.tela.resizable(False, False)

        self.canvas.config(width=600, height=400)

        x = (self.tela.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (400 // 2) - 10
        self.tela.geometry(f"600x400+{x}+{y}")

        imagem_fundo = Image.open(IMAGES_DIR / "tela_instrucao/imagem_tutorial.png")
        imagem_fundo = imagem_fundo.resize((600, 400))

        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
        