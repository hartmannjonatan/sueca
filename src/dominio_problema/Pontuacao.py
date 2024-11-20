class Pontuacao:
	def __init__(self):
		self._galhos : int = None
		self._pontos : int = None

	def zerar_pontuacao_rodada(self):
		pass

	def add_pontuacao(self, pontuacao : int):
		pass

	@property
	def galhos(self) -> int:
		return self._galhos

	@property
	def pontos(self) -> int:
		return self._pontos

