from jogador import Jogador
from pontuacao import Pontuacao


class Dupla:
	def __init__(self):
		self._jogadores : list[Jogador] = None
		self._pontuacao : Pontuacao = None

	def zerar_pontuacao_rodada(self):
		pass

	def add_pontuacao(self, pontuacao : int):
		pass

	def set_galhos(self, galhos : int):
		pass

	def reiniciar(self):
		pass

	@property
	def jogadores(self) -> list[Jogador]:
		return self._jogadores
	
	@property
	def pontuacao(self) -> Pontuacao:
		return self._pontuacao


