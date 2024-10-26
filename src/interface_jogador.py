from tkinter import *

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from tela_inicial import TelaInicial
from tela_jogo import TelaJogo


class InterfaceJogador(DogPlayerInterface):

    def __init__(self):
        self.janela_principal = Tk()
        self.canvas = Canvas(self.janela_principal, width=1200, height=700)

        self._tela_inicial = TelaInicial(self.janela_principal, self.canvas, self)
        self._tela_jogo = TelaJogo(self.janela_principal, self.canvas)
        self._dog_server_interface = DogActor()
        #self._jogo = Jogo()
        
        self.configurar_tela_inicial()

        self.janela_principal.mainloop()

    def configurar_tela_inicial(self):
        self.tela_inicial.configurar_tela()
        self.tela_inicial.tela_conexao_dog.abrir_tela()
        self.janela_principal.focus_force()
    
    def desbloquear_botao_iniciar(self):
        self.tela_inicial.canvas.itemconfig(self.tela_inicial.botao_jogar, state="normal")
    
    def analisar_mensagem_dog(self, mensagem, jogadores=None, id_jogador_local=None):
        if mensagem == "Conectado a Dog Server":
            self.tela_inicial.tela_conectado.abrir_tela()
            self.desbloquear_botao_iniciar()
        elif mensagem == "Não conectado a Dog Server":
            self.tela_inicial.tela_conexao_falhou.abrir_tela()
        elif mensagem == "Jogadores insuficientes":
            self.tela_inicial.tela_jogadores_insuficientes.abrir_tela()
        elif mensagem == "Partida iniciada":
            self.tela_inicial.tela_recebimento_partida.abrir_tela()
            #self.jogo.inicializar_jogadores_duplas_e_mesas(jogadores, id_jogador_local)
            self.tela_jogo.configurar_tela()

    def iniciar_partida(self):
        start_status = self.dog_server_interface.start_match(3)
        mensagem = start_status.get_message()
        jogadores = start_status.get_players()
        id_jogador_local = start_status.get_local_id()
        self.analisar_mensagem_dog(mensagem, jogadores, id_jogador_local)
    
    def receive_start(self, start_status):
        mensagem = start_status.get_message()
        jogadores = start_status.get_players()
        id_jogador_local = start_status.get_local_id()
        self.analisar_mensagem_dog(mensagem, jogadores, id_jogador_local)

    @property
    def tela_inicial(self):
        return self._tela_inicial
    
    @property
    def tela_jogo(self):
        return self._tela_jogo
    
    @property
    def dog_server_interface(self):
        return self._dog_server_interface
    
    


    