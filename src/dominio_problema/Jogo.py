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
		self.mesa.nova_rodada()
		self.duplas[0].zerar_pontuacao_rodada()
		self.duplas[1].zerar_pontuacao_rodada()

		self.habilitar_proximo_jogador(self.proximo_jogador)

	def habilitar_proximo_jogador(self, vencedor : Jogador | None):
		for jogador in self.ordem_jogadores:
			jogador.desabilitar_turno()

		if vencedor == None:
			for i in range(len(self.ordem_jogadores)):
				if self.proximo_jogador == self.ordem_jogadores[i]:
					self.proximo_jogador = self.ordem_jogadores[(i+1) % 4]
		else:
			self.proximo_jogador = vencedor

		self.proximo_jogador.habilitar_turno()
		quantidade_cartas = self.proximo_jogador.quantidade_cartas()

		if quantidade_cartas > 0:
			naipe = self.mesa.naipe_vaza()
			cartas_validas = self.proximo_jogador.cartas_validas(naipe)
			self.interface_jogador.habilitar_cartas(cartas_validas)

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

		self.duplas = list()
		dupla1 = Dupla(self.ordem_jogadores[0], self.ordem_jogadores[2])
		dupla2 = Dupla(self.ordem_jogadores[1], self.ordem_jogadores[3])
		self.duplas.append(dupla1)
		self.duplas.append(dupla2)

		self.proximo_jogador = self.ordem_jogadores[0]
		self.mesa = Mesa()

	def definir_jogadores(self, jogadores : list[list[str]], id_jogador_local : str):
		self.ordem_jogadores = [None, None, None, None]

		for i in range(0, 4):
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
	
	@duplas.setter
	def duplas(self, duplas):
		self._duplas = duplas

	@property
	def mesa(self) -> Mesa:
		return self._mesa
	
	@mesa.setter
	def mesa(self, mesa):
		self._mesa = mesa

	@property
	def ordem_jogadores(self) -> list[Jogador]:
		return self._ordem_jogadores
	
	@ordem_jogadores.setter
	def ordem_jogadores(self, ordem_jogadores):
		self._ordem_jogadores = ordem_jogadores
	
	@property
	def status_jogo(self) -> str:
		return self._status_jogo
	
	@property
	def proximo_jogador(self) -> Jogador:
		return self._proximo_jogador
	
	@proximo_jogador.setter
	def proximo_jogador(self, proximo_jogador):
		self._proximo_jogador = proximo_jogador
	
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


