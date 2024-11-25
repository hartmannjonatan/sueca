from .jogador import Jogador
from .carta import Carta
from .naipe import Naipe

class Baralho:
	def __init__(self):
		self._cartas : list[Carta] = list()

		self.gerar_cartas()

	def gerar_cartas(self):
		for (carta, naipe) in [(c, n) for c in ["a", "2", "3", "4", "5", "6", "7", "j", "q", "k"] for n in [Naipe.paus, Naipe.copas, Naipe.espadas, Naipe.ouros]]:
			self.cartas.append(Carta(carta, naipe))
			
	def distribuir_cartas(self) -> None:
		pass

	def novas_cartas(self, cartas : dict, jogadores : list[Jogador]):
		pass
	

	@property
	def cartas(self) -> list[Carta]:
		return self._cartas

	@cartas.setter
	def cartas(self, cartas):
		self._cartas = cartas

