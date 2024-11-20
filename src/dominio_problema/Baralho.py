from .jogador import Jogador
from .carta import Carta


class Baralho:
	def __init__(self):
		self._cartas : list[Carta] = None

	def distribuir_cartas(self) -> None:
		pass

	def novas_cartas(self, cartas : dict, jogadores : list[Jogador]):
		pass

	@property
	def cartas(self) -> list[Carta]:
		return self._cartas


