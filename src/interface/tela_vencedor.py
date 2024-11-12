from tkinter import *

from .tela_secundaria import TelaSecundaria

from PIL import Image, ImageTk
from images import IMAGES_DIR


class TelaVencedor(TelaSecundaria):

    def __init__(self, interface_jogador):
        super().__init__()

        self._interface_jogador = interface_jogador
        self._nome_vencedor_1 = None
        self._nome_vencedor_2 = None

        self._botao_reiniciar_partida = None
        self.configurar_tela()

    def configurar_tela(self):
        self.tela.title("Aviso")
        self.tela.resizable(False, False)

        self.canvas.config(width=600, height=400)

        x = (self.tela.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (400 // 2) - 10
        self.tela.geometry(f"600x400+{x}+{y}")

        imagem_fundo = Image.open(IMAGES_DIR / "tela_vencedor/imagem_fundo.png")
        imagem_fundo = imagem_fundo.resize((600, 400))
        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        imagem_botao = Image.open(IMAGES_DIR / "tela_vencedor/botao_reiniciar_partida.png")
        imagem_botao = imagem_botao.resize((200, 60))
        self.imagem_botao = ImageTk.PhotoImage(imagem_botao)

        self.nome_vencedores = Label(self.tela, text="Rodrigo e Henrique", font=("Arial", 28), bg="#D9D9D9", fg="#0E400D")
        self.texto = Label(self.tela, text="ganharam!", font=("Arial", 28), bg="#D9D9D9", fg="#0E400D")

        self.nome_vencedores.place(anchor="center", x=300, y=150)
        self.texto.place(anchor="center", x=300, y=195)


        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
        self.botao_reiniciar_partida = self.canvas.create_image(300, 300, anchor="center", image=self.imagem_botao)

        self.canvas.tag_bind(self.botao_reiniciar_partida, "<Button-1>", self.acao_botao)
        self.canvas.tag_bind(self.botao_reiniciar_partida, "<Enter>",   self.on_hover_botao)
        self.canvas.tag_bind(self.botao_reiniciar_partida, "<Leave>",  self.saida_botao)


    def acao_botao(self, event):
        pass

    def on_hover_botao(self, event):
        imagem_botao_grande = Image.open(IMAGES_DIR / "tela_vencedor/botao_reiniciar_partida.png")
        imagem_botao_grande = imagem_botao_grande.resize((220, 60))
        self.imagem_botao_grande = ImageTk.PhotoImage(imagem_botao_grande)

        self.canvas.itemconfig(self.botao_reiniciar_partida, image=self.imagem_botao_grande)
        self.canvas.config(cursor="hand2")

    def saida_botao(self, event):
        self.canvas.itemconfig(self.botao_reiniciar_partida, image=self.imagem_botao)
        self.canvas.config(cursor="")

    @property
    def interface_jogador(self):
        return self._interface_jogador

    @property
    def nome_vencedor1(self):
        return self._nome_vencedor_1

    @nome_vencedor1.setter
    def nome_vencedor1(self, nome):
        self._nome_vencedor_1 = nome

    @property
    def nome_vencedor2(self):
        return self._nome_vencedor_2

    @nome_vencedor2.setter
    def nome_vencedor2(self, nome):
        self._nome_vencedor_2 = nome
    
    @property
    def botao_reiniciar_partida(self):
        return self._botao_reiniciar_partida

    @botao_reiniciar_partida.setter
    def botao_reiniciar_partida(self, botao):
        self._botao_reiniciar_partida = botao