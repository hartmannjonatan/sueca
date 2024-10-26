from tkinter import *
from PIL import Image, ImageTk

import time
import os

from images import IMAGES_DIR

from tela_secundaria import TelaSecundaria


class TelaConexaoDOG(TelaSecundaria):
    def __init__(self, interface_jogador):
        super().__init__()
        self._interface_jogador = interface_jogador
        self._nome_jogador = None
        self._mensagem_dog = None
    
    def configurar_tela(self):
        self.tela.title("Conectar ao DOG Server")
        self.tela.resizable(False, False)

        self.tela.attributes("-topmost", True)
        self.tela.focus_force()
        self.tela.grab_set()

        self.canvas.config(width=400, height=200)

        x = (self.tela.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (200 // 2) - 10
        self.tela.geometry(f"400x200+{x}+{y}")

        imagem_fundo = Image.open(IMAGES_DIR / "tela_conexao_dog/imagem_fundo.png")
        imagem_fundo = imagem_fundo.resize((400, 200))
        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        imagem_botao = Image.open(IMAGES_DIR / "tela_conexao_dog/botao_conectar.png")
        imagem_botao = imagem_botao.resize((105, 44))
        self.imagem_botao = ImageTk.PhotoImage(imagem_botao)

        self._input_nome = Entry(self.tela, font=("Arial", 12))
        self.input_nome.place(x=200, y=70, width=300, height=35, anchor="center")

        self.input_nome.insert(0, "Digite seu nome...")
        self.input_nome.bind("<FocusIn>", self.limpar_input)

        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)
        self.botao_conectar = self.canvas.create_image(200, 150, anchor="center", image=self.imagem_botao)

        self.canvas.tag_bind(self.botao_conectar, "<Button-1>", self.acao_botao_conectar)
        self.canvas.tag_bind(self.botao_conectar, "<Enter>",   self.on_hover_botao)
        self.canvas.tag_bind(self.botao_conectar, "<Leave>",  self.saida_botao)
    
    def fechar_tela(self):
        self.nome_jogador = self.gerar_nome_jogador() 

        self.tela.grab_release()
        self.tela.withdraw()
    
        self.conectar_ao_dog()
        self.interface_jogador.analisar_mensagem_dog(self.mensagem_dog)
    
    def limpar_input(self, event):
        if self.input_nome.get() == 'Digite seu nome...':
            self.input_nome.delete(0, "end")
        
    def acao_botao_conectar(self, event):
        self.nome_jogador = self.input_nome.get()

        if self.nome_jogador == "Digite seu nome..." or self.nome_jogador == "":
            self.nome_jogador = self.gerar_nome_jogador()

        self.tela.grab_release()
        self.tela.withdraw()

        self.conectar_ao_dog()
        self.interface_jogador.analisar_mensagem_dog(self.mensagem_dog)

    def on_hover_botao(self, event):
        imagem_botao_grande = Image.open(IMAGES_DIR / "tela_conexao_dog/botao_conectar.png")
        imagem_botao_grande = imagem_botao_grande.resize((125, 50))
        self.imagem_botao_grande = ImageTk.PhotoImage(imagem_botao_grande)

        self.canvas.itemconfig(self.botao_conectar, image=self.imagem_botao_grande)
        self.canvas.config(cursor="hand2")
    
    def saida_botao(self, event):
        self.canvas.itemconfig(self.botao_conectar, image=self.imagem_botao)
        self.canvas.config(cursor="")
 
    def conectar_ao_dog(self):
        try:
            diretorio_atual = os.getcwd()
            if "src" not in diretorio_atual:
                os.chdir("src")
                
            self.mensagem_dog = self.interface_jogador.dog_server_interface.initialize(self.nome_jogador, self.interface_jogador)
        except:
            self.mensagem_dog = "Não conectado a Dog Server"
        
    def gerar_nome_jogador(self):
        horario_atual = time.gmtime()
        hora = horario_atual.tm_hour - 3
        minuto = horario_atual.tm_min
        segundo = horario_atual.tm_sec

        return f"Jogador{hora}{minuto}{segundo}"
        
    @property
    def interface_jogador(self):
        return self._interface_jogador

    @property
    def input_nome(self):
        return self._input_nome

    @property
    def nome_jogador(self):
        return self._nome_jogador
    
    @nome_jogador.setter
    def nome_jogador(self, novo_nome):
        self._nome_jogador = novo_nome
    
    @property
    def mensagem_dog(self):
        return self._mensagem_dog
    
    @mensagem_dog.setter
    def mensagem_dog(self, nova_mensagem):
        self._mensagem_dog = nova_mensagem
