from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

from tela_secundaria import TelaSecundaria

class TelaInputNome(TelaSecundaria):
    def __init__(self):
        super().__init__()
    
    def configurar_tela(self):
        self.tela.title("Insira seu nome")
        self.tela.resizable(False, False)

        self.tela.attributes("-topmost", True)
        self.tela.focus_force()
        self.tela.grab_set()

        self.canvas.config(width=400, height=200)

        x = (self.tela.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (200 // 2) - 10
        self.tela.geometry(f"400x200+{x}+{y}")

        imagem_fundo = Image.open("images/tela_input_nome/imagem_fundo.png")
        imagem_fundo = imagem_fundo.resize((400, 200))
        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        imagem_botao = Image.open("images/tela_input_nome/botao_conectar.png")
        imagem_botao = imagem_botao.resize((105, 44))
        self.imagem_botao = ImageTk.PhotoImage(imagem_botao)

        self.input_nome = Entry(self.tela, font=("Arial", 12))
        self.input_nome.place(x=200, y=70, width=300, height=35, anchor="center")

        self.input_nome.insert(0, "Digite seu nome...")
        self.input_nome.bind("<FocusIn>", self.limpar_input)

        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
        self.botao = self.canvas.create_image(200, 150, anchor="center", image=self.imagem_botao)

        self.canvas.tag_bind(self.botao, "<Button-1>", self.acao_botao)
        self.canvas.tag_bind(self.botao, "<Enter>",   self.on_hover_botao)
        self.canvas.tag_bind(self.botao, "<Leave>",  self.saida_botao)
    
    def fechar_tela(self):
        self.tela.grab_release()
        self.tela.destroy()
    
    def limpar_input(self, event):
        if self.input_nome.get() == 'Digite seu nome...':
            self.input_nome.delete(0, "end")
        
    def acao_botao(self, event):
        self.fechar_tela()
    
    def on_hover_botao(self, event):
        imagem_botao_grande = Image.open("images/tela_input_nome/botao_conectar.png")
        imagem_botao_grande = imagem_botao_grande.resize((125, 50))
        self.imagem_botao_grande = ImageTk.PhotoImage(imagem_botao_grande)

        self.canvas.itemconfig(self.botao, image=self.imagem_botao_grande)
    
    def saida_botao(self, event):
        self.canvas.itemconfig(self.botao, image=self.imagem_botao)