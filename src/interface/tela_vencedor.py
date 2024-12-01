from tkinter import *

from PIL import Image, ImageTk
from images import IMAGES_DIR

from .tela_secundaria import TelaSecundaria
from dominio_problema.dupla import Dupla


class TelaVencedor(TelaSecundaria):

    def __init__(self, interface_jogador):
        super().__init__()

        self._interface_jogador = interface_jogador
        self._vencedores_label: Label = None

        self._botao_reiniciar_partida: int = None
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

        self.texto = Label(self.tela, text="ganharam!", font=("Arial", 28), bg="#D9D9D9", fg="#0E400D")
        self.vencedores_label = Label(self.tela, text="...", font=("Arial", 28), bg="#D9D9D9", fg="#0E400D")

        self.vencedores_label.place(anchor="center", x=300, y=150)
        self.texto.place(anchor="center", x=300, y=195)

        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
        self.botao_reiniciar_partida = self.canvas.create_image(300, 300, anchor="center", image=self.imagem_botao)

        self.canvas.tag_bind(self.botao_reiniciar_partida, "<Button-1>", self.click_botao_reiniciar_partida)
        self.canvas.tag_bind(self.botao_reiniciar_partida, "<Enter>",   self.on_hover_botao)
        self.canvas.tag_bind(self.botao_reiniciar_partida, "<Leave>",  self.saida_botao)

    def click_botao_reiniciar_partida(self, event):
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
    
    def atualizar(self, dupla_vencedora: list[Dupla]):
        if len(dupla_vencedora) > 1:
            self.vencedores_label.config(text="Houve um empate!")
            self.texto.config(text="")
        else:
            self.vencedores_label.config(text=f"{dupla_vencedora[0].jogadores[0].nome} e {dupla_vencedora[0].jogadores[1].nome}")

    @property
    def interface_jogador(self):
        return self._interface_jogador

    @property
    def vencedores_label(self):
        return self._vencedores_label

    @vencedores_label.setter
    def vencedores_label(self, nome):
        self._vencedores_label = nome

    @property
    def botao_reiniciar_partida(self):
        return self._botao_reiniciar_partida

    @botao_reiniciar_partida.setter
    def botao_reiniciar_partida(self, botao):
        self._botao_reiniciar_partida = botao