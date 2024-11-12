from tkinter import *
from PIL import Image, ImageTk

from images import IMAGES_DIR

from .tela_conectado import TelaConectado
from .tela_conexao_dog import TelaConexaoDOG
from .tela_conexao_falhou import TelaConexaoFalhou
from .tela_jogadores_insuficientes import TelaJogadoresInsuficientes
from .tela_recebimento_partida import TelaRecebimentoPartida
from .tela_abandono import TelaAbandono


class TelaInicial:

    def __init__(self, janela_principal, canvas, interface_jogador):
        self._janela_principal = janela_principal
        self._canvas = canvas
        self._interface_jogador = interface_jogador
        self._tela_conexao_dog = TelaConexaoDOG(interface_jogador)
        self._tela_conectado = TelaConectado()
        self._tela_conexao_falhou = TelaConexaoFalhou()
        self._tela_jogadores_insuficientes = TelaJogadoresInsuficientes()
        self._tela_recebimento_partida = TelaRecebimentoPartida()
        self._tela_abandono = TelaAbandono()

        self._botao_iniciar_partida = None

    def configurar_tela(self):
        largura = 1200
        altura = 700
        
        self.janela_principal.title("Sueca")
        self.janela_principal.geometry("1200x700")
        self.janela_principal.resizable(False, False)

        imagem_fundo = Image.open(IMAGES_DIR / "tela_inicial/background.png")
        imagem_fundo = imagem_fundo.resize((largura, altura), Image.LANCZOS)
        
        self.imagem_fundo_inicial = ImageTk.PhotoImage(imagem_fundo)

        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo_inicial)
       
        x = (self.janela_principal.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.janela_principal.winfo_screenheight() // 2) - (altura // 2) - 10
        self.janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")

        imagem_botao = Image.open(IMAGES_DIR / "tela_inicial/botao_iniciar_partida.png")
        imagem_botao = imagem_botao.resize((200, 80), Image.LANCZOS)
        self.imagem_botao = ImageTk.PhotoImage(imagem_botao)

        self.botao_iniciar_partida = self.canvas.create_image(600, 450, anchor="center", image=self.imagem_botao)
        self.canvas.itemconfig(self.botao_iniciar_partida, state="disabled")

        self.canvas.tag_bind(self.botao_iniciar_partida, "<Button-1>", self.acao_botao_iniciar_partida)
        self.canvas.tag_bind(self.botao_iniciar_partida, "<Enter>",   self.on_hover_botao)
        self.canvas.tag_bind(self.botao_iniciar_partida, "<Leave>",  self.saida_botao)
    
    def acao_botao_iniciar_partida(self, event):
        self.interface_jogador.iniciar_partida()

    def on_hover_botao(self, event):
        imagem_botao = Image.open(IMAGES_DIR / "tela_inicial/botao_iniciar_partida.png")
        imagem_botao = imagem_botao.resize((210, 85), Image.LANCZOS)
        self.imagem_botao_grande = ImageTk.PhotoImage(imagem_botao)

        self.canvas.itemconfig(self.botao_iniciar_partida, image=self.imagem_botao_grande)
        self.canvas.config(cursor="hand2")

    def saida_botao(self, event):
        self.canvas.itemconfig(self.botao_iniciar_partida, image=self.imagem_botao)
        self.canvas.config(cursor="")
    
    def abrir_tela_conexao_dog(self):
        self.tela_conexao_dog.abrir_tela()
    
    def abrir_tela_conectado(self):
        self.tela_conectado.abrir_tela()
    
    def abrir_tela_conexao_falhou(self):
        self.tela_conexao_falhou.abrir_tela()
    
    def abrir_tela_jogadores_insuficientes(self):
        self.tela_jogadores_insuficientes.abrir_tela()
    
    def abrir_tela_recebimento_partida(self):
        self.tela_recebimento_partida.abrir_tela()
    
    @property
    def janela_principal(self):
        return self._janela_principal
    
    @property
    def canvas(self):
        return self._canvas

    @property
    def interface_jogador(self):
        return self._interface_jogador
    
    @property
    def tela_conexao_dog(self):
        return self._tela_conexao_dog
    
    @property
    def tela_conectado(self):
        return self._tela_conectado
    
    @property
    def tela_conexao_falhou(self):
        return self._tela_conexao_falhou
    
    @property
    def tela_jogadores_insuficientes(self):
        return self._tela_jogadores_insuficientes
    
    @property
    def tela_recebimento_partida(self):
        return self._tela_recebimento_partida
    
    @property
    def tela_abandono(self):
        return self._tela_abandono

    @property
    def botao_iniciar_partida(self):
        return self._botao_iniciar_partida
    
    @botao_iniciar_partida.setter
    def botao_iniciar_partida(self, botao_iniciar_partida):
        self._botao_iniciar_partida = botao_iniciar_partida



    
