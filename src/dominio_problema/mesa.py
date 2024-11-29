from .baralho import Baralho
from .rodada import Rodada
from .naipe import Naipe
from .carta import Carta
from .jogador import Jogador
from .vaza import Vaza


class Mesa:
	def __init__(self):
		self._baralho : Baralho = None
		self._rodadas : list[Rodada] = list()
	
	def nova_rodada(self):
		nova_rodada = Rodada()
		self.rodadas.append(nova_rodada)

	def novo_baralho(self) -> tuple[list[Carta], Naipe]:
		self.baralho = Baralho()
		cartas, naipe_trunfo = self.baralho.distribuir_cartas()
		self.rodadas[len(self.rodadas)-1].definir_trunfo(naipe_trunfo)

		return cartas, naipe_trunfo

	def novas_cartas(self, cartas : dict, jogadores : list[Jogador], naipe_trunfo : Naipe):
		if self.baralho == None:
			self._baralho = Baralho()
		self.baralho.novas_cartas(cartas, jogadores, naipe_trunfo)
		self.rodadas[len(self.rodadas)-1].definir_trunfo(naipe_trunfo)
			
	def nova_vaza(self) -> Vaza:
		return self.rodadas[len(self.rodadas)-1].nova_vaza()

	def avaliar_jogada(self) -> dict:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe | None:
		self.rodadas[len(self.rodadas)-1].naipe_vaza()


	@property
	def baralho(self) -> Baralho:
		return self._baralho
	
	@baralho.setter
	def baralho(self, baralho):
		self._baralho = baralho
	
	@property
	def rodadas(self) -> list[Rodada]:
		return self._rodadas
	
	@rodadas.setter
	def rodadas(self, rodada):
		self._rodadas = rodada

