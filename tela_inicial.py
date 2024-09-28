from tkinter import *
from PIL import Image, ImageTk

class TelaInicial:

    def __init__(self, janela_principal, canvas, funcao):
        self.janela_principal = janela_principal
        self.canvas = canvas

        self.funcao_botao_jogar = funcao

    def configurar_tela(self):
        largura = 1200
        altura = 700
        
        self.janela_principal.title("Sueca")
        self.janela_principal.geometry("1200x700")
        self.janela_principal.resizable(False, False)

        imagem_fundo = Image.open("images/tela_inicial/background.png")
        imagem_fundo = imagem_fundo.resize((largura, altura), Image.LANCZOS)
        
        self.imagem_fundo_inicial = ImageTk.PhotoImage(imagem_fundo)

        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo_inicial)
       
        x = (self.janela_principal.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.janela_principal.winfo_screenheight() // 2) - (altura // 2) - 10
        self.janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")

        imagem_botao = Image.open("images/tela_inicial/botao_jogar.png")
        imagem_botao = imagem_botao.resize((200, 80), Image.LANCZOS)
        self.imagem_botao = ImageTk.PhotoImage(imagem_botao)

        self.botao_jogar = self.canvas.create_image(600, 450, anchor="center", image=self.imagem_botao)

        self.canvas.tag_bind(self.botao_jogar, "<Button-1>", self.acao_botao)
        self.canvas.tag_bind(self.botao_jogar, "<Enter>",   self.on_hover_botao)
        self.canvas.tag_bind(self.botao_jogar, "<Leave>",  self.saida_botao)
    
    def acao_botao(self, event):
        self.funcao_botao_jogar()

    def on_hover_botao(self, event):
        imagem_botao = Image.open("images/tela_inicial/botao_jogar.png")
        imagem_botao = imagem_botao.resize((210, 85), Image.LANCZOS)
        self.imagem_botao_grande = ImageTk.PhotoImage(imagem_botao)

        self.canvas.itemconfig(self.botao_jogar, image=self.imagem_botao_grande)
        self.canvas.config(cursor="hand2")


    def saida_botao(self, event):
        self.canvas.itemconfig(self.botao_jogar, image=self.imagem_botao)
        self.canvas.config(cursor="")

    
