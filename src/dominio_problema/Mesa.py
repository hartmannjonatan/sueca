from baralho import Baralho
from rodada import Rodada
from naipe import Naipe
from carta import Carta
from jogador import Jogador


class Mesa:
	def __init__(self):
		self._baralho : Baralho = None
		self._rodadas : list[Rodada] = None
	
	def nova_rodada(self):
		pass

	def novo_baralho(self) -> tuple[list[Carta], Naipe]:
		pass

	def novas_cartas(self, cartas : dict, jogadores : list[Jogador], naipe_trunfo : Naipe):
		pass

	def nova_vaza(self):
		pass

	def avaliar_jogada(self) -> dict:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe | None:
		pass


	@property
	def baralho(self) -> Baralho:
		return self._baralho
	
	@property
	def rodada(self) -> list[Rodada]:
		return self._rodada

