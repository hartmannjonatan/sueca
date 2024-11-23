class Pontuacao:
	def __init__(self):
		self._galhos : int = 0
		self._pontos : int = 0

	def zerar_pontuacao_rodada(self):
		self.pontos = 0

	def add_pontuacao(self, pontuacao : int):
		self.pontos += pontuacao

	@property
	def galhos(self) -> int:
		return self._galhos
	
	@galhos.setter
	def galhos(self, galhos):
		self._galhos = galhos

	@property
	def pontos(self) -> int:
		return self._pontos
	
	@pontos.setter
	def pontos(self, pontos):
		self._pontos = pontos

