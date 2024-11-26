from .naipe import Naipe


class Carta:
	def __init__(self, numero: str, naipe: Naipe):
		self._numero : str = numero
		self._naipe : Naipe = naipe
		self._valor : int = None
		self._nome : str = f"{numero}_{naipe}"

	@property
	def numero(self) -> str:
		return self._numero
	
	@numero.setter
	def numero(self, numero):
		self._numero = numero
	
	@property
	def naipe(self) -> Naipe:
		return self._naipe
	
	@naipe.setter
	def naipe(self, naipe):
		self._naipe = naipe
	
	@property
	def valor(self) -> int:
		return self._valor

	@valor.setter
	def valor(self, valor):
		self._valor = valor
	
	@property
	def nome(self) -> str:
		return self._nome
	
	@nome.setter
	def nome(self, nome):
		self._nome = nome
	



