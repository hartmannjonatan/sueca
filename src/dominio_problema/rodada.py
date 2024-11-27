from .vaza import Vaza
from .naipe import Naipe
from .jogador import Jogador
from .carta import Carta

class Rodada:
	def __init__(self):
		self._vazas : list[Vaza] = None
		self._trunfo : Naipe = None

	def nova_vaza(self) -> Vaza:
		vaza = Vaza()
		self.vazas.append(vaza)
		return vaza

	def definir_trunfo(self, naipe_trunfo : Naipe):
		self.trunfo = naipe_trunfo

	def avaliar_vaza(self) -> tuple[int, Jogador]:
		pass

	def rodada_finalizada(self) -> bool:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe | None:
		vaza_atual = self.vazas[len(self.vazas)-1]
		return vaza_atual.naipe_vaza()

	@property
	def vazas(self) -> list[Vaza]:
		return self._vazas
	
	@vazas.setter
	def vazas(self, vazas):
		self._vazas = vazas
	
	@property
	def trunfo(self) -> Naipe:
		return self._trunfo

	@trunfo.setter
	def trunfo(self, trunfo):
		self._trunfo = trunfo


