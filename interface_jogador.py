from tkinter import *
from PIL import Image, ImageTk

import time

from tela_inicial import TelaInicial
from tela_jogo import TelaJogo
from tela_input_nome import TelaInputNome

class InterfaceJogador:

    def __init__(self):
        self.janela_principal = Tk()
        self.canvas = Canvas(self.janela_principal, width=1200, height=700)

        self.tela_inicial = TelaInicial(self.janela_principal, self.canvas, self.iniciar_jogo)
        self.tela_jogo = TelaJogo(self.janela_principal, self.canvas)
        self.tela_input_nome = TelaInputNome()

        self.configurar_tela_inicial()

        self.janela_principal.mainloop()

    def configurar_tela_inicial(self):
        self.tela_inicial.configurar_tela()
        self.tela_input_nome.abrir_tela()
        self.janela_principal.focus_force()


    def iniciar_jogo(self):
        self.tela_jogo.configurar_tela()

    