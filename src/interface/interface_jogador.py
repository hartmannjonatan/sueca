from tkinter import *

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from dog.start_status import StartStatus

from .tela_inicial import TelaInicial
from .tela_jogo import TelaJogo

from dominio_problema.jogo import Jogo
from dominio_problema.vaza import Vaza
from dominio_problema.jogador import Jogador
from dominio_problema.naipe import Naipe
from dominio_problema.dupla import Dupla
from dominio_problema.carta import Carta


class InterfaceJogador(DogPlayerInterface):

    def __init__(self):
        self._janela_principal = Tk()
        self._canvas = Canvas(self.janela_principal, width=1200, height=700)

        self._tela_inicial = TelaInicial(self.janela_principal, self.canvas, self)
        self._tela_jogo = TelaJogo(self.janela_principal, self.canvas, self)
        self._dog_server_interface = DogActor()
        self._jogo = None
        
        self.configurar_tela_inicial()

        self.janela_principal.mainloop()

    def configurar_tela_inicial(self):
        self.tela_inicial.configurar_tela()
        self.tela_inicial.abrir_tela_conexao_dog()
        self.janela_principal.focus_force()
    
    def configurar_tela_abandono(self):
        pass

    def limpar_canva(self):
        pass
    
    def desbloquear_botao_iniciar(self):
        self.tela_inicial.canvas.itemconfig(self.tela_inicial.botao_iniciar_partida, state="normal")
    
    def iniciar_partida(self):
        start_status = self.dog_server_interface.start_match(1)
        mensagem = start_status.get_message()
        jogadores = start_status.get_players()
        id_jogador_local = start_status.get_local_id()
        self.analisar_mensagem_dog(mensagem, jogadores, id_jogador_local)
    
    def atualizar_interface_jogo(status: str, vaza: Vaza, jogador_local: Jogador):
        pass
    
    def analisar_mensagem_dog(self, mensagem: str, jogadores: list[list[str]] = None, id_jogador_local: str = None):
        if mensagem == "Conectado a Dog Server":
            self.tela_inicial.abrir_tela_conectado()
            self.desbloquear_botao_iniciar()
        elif mensagem == "Não conectado a Dog Server":
            self.tela_inicial.abrir_tela_conexao_falhou()
        elif mensagem == "Jogadores insuficientes":
            self.tela_inicial.abrir_tela_jogadores_insuficientes()
        elif mensagem == "Partida iniciada":
            self.tela_inicial.abrir_tela_recebimento_partida()
            #self.jogo.inicializar_jogadores_duplas_e_mesas(jogadores, id_jogador_local)
            self.tela_jogo.configurar_tela()
        
    def revelar_trunfo(self, trunfo: Naipe):
        pass

    def atualizar_tela_vencedor(self, dupla_vencedora: list[Dupla]):
        pass

    def remover_instancia_jogo(self):
        pass

    def jogar_carta(self, indice_carta: int):
        pass

    def habilitar_cartas(self, cartas: list[Carta]):
        pass

    def desabilitar_cartas(self):
        pass

    def enviar_jogada(self, jogada: dict):
        pass

    def receive_move(self, a_move: dict):
        pass

    def receive_withdrawal_notification(self):
        pass

    def receive_start(self, start_status: StartStatus):
        mensagem = start_status.get_message()
        jogadores = start_status.get_players()
        id_jogador_local = start_status.get_local_id()
        self.analisar_mensagem_dog(mensagem, jogadores, id_jogador_local)
    
    @property
    def janela_principal(self):
        return self._janela_principal
    
    @property
    def canvas(self) -> Tk:
        return self._canvas

    @property
    def tela_inicial(self) -> TelaInicial:
        return self._tela_inicial
    
    @property
    def tela_jogo(self) -> TelaJogo:
        return self._tela_jogo
    
    @property
    def dog_server_interface(self) -> DogActor:
        return self._dog_server_interface

    @property
    def jogo(self) -> Jogo:
        return self._jogo
    
    


    