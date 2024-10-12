from tkinter import *
from tkinter import simpledialog

from PIL import Image, ImageTk

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from tela_inicial import TelaInicial
from tela_jogo import TelaJogo
from tela_conectado import TelaConectado
from tela_conexao_dog import TelaConexaoDOG


class InterfaceJogador(DogPlayerInterface):

    def __init__(self):
        self.janela_principal = Tk()
        self.canvas = Canvas(self.janela_principal, width=1200, height=700)

        self.tela_inicial = TelaInicial(self.janela_principal, self.canvas, self.iniciar_jogo)
        self.tela_jogo = TelaJogo(self.janela_principal, self.canvas)
        self.dog_server_interface = DogActor()
        self.tela_input_nome = TelaConexaoDOG(self, self.dog_server_interface)
        self.tela_conectado = TelaConectado()

        self.configurar_tela_inicial()

        self.janela_principal.mainloop()

    def configurar_tela_inicial(self):
        self.tela_inicial.configurar_tela()
        self.tela_input_nome.abrir_tela()
        self.janela_principal.focus_force()

    def iniciar_jogo(self):
        self.tela_jogo.configurar_tela()
    
    def analisar_mensagem_dog(self, mensagem):
        if mensagem == "Conectado a Dog Server":
            self.tela_conectado.abrir_tela()
        else:
            print("Erro de conexão")
    


    