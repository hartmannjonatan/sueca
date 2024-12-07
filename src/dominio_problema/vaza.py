from .carta import Carta
from .jogador import Jogador
from .naipe import Naipe


class Vaza:
	def __init__(self):
		self._cartas_jogadas : list[Carta] = []
		self._primeiro_jogador : Jogador = None
		self._naipe_obrigatorio : Naipe = None
		self._jogadores : list[Jogador] = None

	def vaza_finalizada(self) -> bool:
		return len(self.cartas_jogadas) == 4

	def definir_vencedor(self, trunfo : Naipe) -> Jogador:
		vencedorCartaTrunfo = None
		vencedorCartaVaza = self.jogadores[0]
		cartaVencedoraNaipeVaza: Carta = self.cartas_jogadas[0]
		cartaVencedoraTrunfo: Carta = None

		for i in range(4):
			carta = self.cartas_jogadas[i]
			if carta.naipe == self.naipe_obrigatorio:
				if carta.valor > cartaVencedoraNaipeVaza.valor:
					cartaVencedoraNaipeVaza = carta
					vencedorCartaVaza = self.jogadores[i]
			else:
				if carta.naipe == trunfo:
					if cartaVencedoraTrunfo == None or carta.valor > cartaVencedoraTrunfo.valor:
						cartaVencedoraTrunfo = carta
						vencedorCartaTrunfo = self.jogadores[i]
						
		if vencedorCartaTrunfo == None:
			return vencedorCartaVaza
		else:
			return vencedorCartaTrunfo

	def somar_pontuacao(self) -> int:
		pontos = 0
		for i in range(len(self.cartas_jogadas)):
			pontos += self.cartas_jogadas[i].valor
		return pontos

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		if self.jogadores is None:
			self._jogadores = []
			self._primeiro_jogador = jogador

		if self.naipe_obrigatorio is None:
			self._naipe_obrigatorio = carta.naipe

		self.add_carta(carta, jogador)


	def naipe_vaza(self) -> Naipe | None:
		return self._naipe_obrigatorio

	def add_carta(self, carta : Carta, jogador : Jogador):
		self.cartas_jogadas.append(carta)
		self.jogadores.append(jogador)

	@property
	def cartas_jogadas(self) -> list[Carta]:
		return self._cartas_jogadas
	
	@property
	def primeiro_jogador(self) -> Jogador:
		return self._primeiro_jogador
	
	
	@property
	def naipe_obrigatorio(self) -> Naipe:
		return self._naipe_obrigatorio
	
	@property
	def jogadores(self) -> list[Jogador]:
		return self._jogadores


