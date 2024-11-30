from .naipe import Naipe


class Carta:
	def __init__(self, numero: str, naipe: Naipe):
		self._numero : str = numero
		self._naipe : Naipe = naipe
		match self._numero:
			case "a": self._valor = 11
			case "7": self._valor = 10
			case "k": self._valor = 4
			case "j": self._valor = 3
			case "q": self._valor = 2
			case _: self._valor = 0
		self._nome : str = f"{numero}_{naipe.name}"

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
	



