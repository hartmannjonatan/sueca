from .dupla import Dupla
from .mesa import Mesa
from .jogador import Jogador


class Jogo:
	def __init__(self):
		self._duplas : list[Dupla] = None
		self._mesa : Mesa = None
		self._ordem_jogadores : list[Jogador] = None
		self._status_jogo : str = None
		self._proximo_jogador : Jogador = None
		self._interface_jogador = None
		self._jogador_local : Jogador = None
		self._partida_encerrada : bool = False
		self._rodada_encerrada : bool = False
		self._vaza_encerrada : bool = False	

	def receber_jogada(self, jogada : dict):
		pass

	def nova_rodada(self, cartas : dict = None):
		pass

	def habilitar_proximo_jogador(self, vencedor : Jogador | None):
		pass

	def atualizar_tela_jogo(self):
		pass

	def avaliar_jogada(self):
		pass

	def atualizar_galhos(self):
		pass

	def avaliar_dupla_vencedora(self) -> list[Dupla] | None:
		pass

	def jogar_carta(self, indice_carta : int):
		pass

	def inicializar_jogadores_duplas_e_mesa(self, jogadores : list[list[str]], id_jogador_local : str):
		self.definir_jogadores(jogadores, id_jogador_local)

		self.duplas[0] = Dupla(self.ordem_jogadores[0], self.ordem_jogadores[1])
		self.duplas[1] = Dupla(self.ordem_jogadores[1], self.ordem_jogadores[3])

		self.mesa = Mesa()

	def definir_jogadores(self, jogadores : list[list[str]], id_jogador_local : str):
		self._ordem_jogadores = [None, None, None, None]

		for i in range(0, 2):
			nome = jogadores[i][0]
			id_jogador = jogadores[i][1]
			ordem = jogadores[i][2]
			jogador = Jogador(nome)
			self.ordem_jogadores[int(ordem)-1] = jogador

			if id_jogador == id_jogador_local:
				self.jogador_local = jogador
				jogador.isLocal = True

	def reiniciar_partida(self):
		pass

	@property
	def duplas(self) -> list[Dupla]:
		return self._duplas
	
	@property
	def mesa(self) -> Mesa:
		return self._mesa

	@property
	def ordem_jogadores(self) -> list[Jogador]:
		return self._ordem_jogadores
	
	@property
	def status_jogo(self) -> str:
		return self._status_jogo
	
	@property
	def proximo_jogador(self) -> Jogador:
		return self._proximo_jogador
	
	@property
	def interface_jogador(self):
		return self._interface_jogador
	
	@property
	def jogador_local(self) -> Jogador:
		return self._jogador_local
	
	@jogador_local.setter
	def jogador_local(self, jogador_local):
		self._jogador_local = jogador_local

	@property
	def partida_encerrada(self) -> bool:
		return self._partida_encerrada
	
	@property
	def rodada_encerrada(self) -> bool:
		return self._rodada_encerrada
	
	@property
	def vaza_encerrada(self) -> bool:
		return self._vaza_encerrada


