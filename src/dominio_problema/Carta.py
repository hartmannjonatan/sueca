from naipe import Naipe


class Carta:
	def __init__(self):
		self._numero : str = None
		self._naipe : Naipe = None
		self._valor : int = None
		self._nome : str = None

	@property
	def numero(self) -> str:
		return self._numero
	
	@property
	def naipe(self) -> Naipe:
		return self._naipe
	
	@property
	def valor(self) -> int:
		return self._valor
	
	@property
	def nome(self) -> str:
		return self._nome
	



