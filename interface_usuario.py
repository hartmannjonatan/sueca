from tkinter import *
from PIL import Image, ImageTk

from tela_inicial import TelaInicial
from tela_jogo import TelaJogo

class InterfaceUsuario:

    def __init__(self):
        self.janela_principal = Tk()
        self.canvas = Canvas(self.janela_principal, width=1200, height=700)

        self.tela_inicial = TelaInicial(self.janela_principal, self.canvas, self.iniciar_jogo)
        self.tela_jogo = TelaJogo(self.janela_principal, self.canvas)

        self.configurar_tela_inicial()

        self.janela_principal.mainloop()

    def configurar_tela_inicial(self):
        self.tela_inicial.configurar_tela()

    def iniciar_jogo(self):
        self.tela_jogo.configurar_tela()

    