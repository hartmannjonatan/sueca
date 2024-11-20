from .carta import Carta
from .naipe import Naipe 


class Jogador:
	def __init__(self):
		self._nome : str = None
		self._cartas : Carta = None
		self._meu_turno : bool = None
		self._isLocal : bool = None
		self._vencedor : bool = None

	def quantidade_cartas(self) -> int:
		pass

	def add_carta(self, carta : Carta):
		pass

	def remover_carta(self, carta : dict) -> Carta:
		pass

	def ordenar_cartas(self, naipe_trunfo : Naipe):
		pass

	def cartas_validas(self, naipe_vaza : Naipe | None) -> list[Carta]:
		pass

	def novas_cartas(self, cartas : list[Carta]):
		pass

	def habilitar_turno(self):
		pass

	def desabilitar_turno(self):
		pass

	def reiniciar(self):
		pass

	def definir_vencedor(self):
		pass


	@property
	def nome(self) -> str:
		return self._nome
	
	@nome.setter
	def nome(self, nome: str):
		self._nome = nome

	@property
	def cartas(self) -> list[Carta]:
		return self._cartas
	
	@property
	def meu_turno(self) -> bool:
		return self._meu_turno
	
	@property
	def isLocal(self) -> bool:
		return self._isLocal
	
	@property
	def vencedor(self) -> bool:
		return self._vencedor

