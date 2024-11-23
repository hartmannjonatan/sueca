from .vaza import Vaza
from .naipe import Naipe
from .jogador import Jogador
from .carta import Carta

class Rodada:
	def __init__(self):
		self._vazas : list[Vaza] = None
		self._trunfo : Naipe = None

	def nova_vaza(self):
		pass

	def definir_trunfo(self, naipe_trunfo : Naipe):
		pass

	def avaliar_vaza(self) -> tuple[int, Jogador]:
		pass

	def rodada_finalizada(self) -> bool:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe | None:
		pass

	@property
	def vazas(self) -> list[Vaza]:
		return self._vazas
	
	@property
	def trunfo(self) -> Naipe:
		return self._trunfo


