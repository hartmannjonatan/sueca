from .jogador import Jogador
from .pontuacao import Pontuacao


class Dupla:
	def __init__(self, jogador1, jogador2):
		self._jogadores : list[Jogador] = [jogador1, jogador2]
		self._pontuacao : Pontuacao = Pontuacao()

	def zerar_pontuacao_rodada(self):
		self.pontuacao.zerar_pontuacao_rodada()

	def add_pontuacao(self, pontuacao : int):
		self.pontuacao.add_pontuacao(pontuacao)

	def set_galhos(self, galhos : int):
		self.pontuacao.galhos = galhos

	def reiniciar(self):
		pass

	@property
	def jogadores(self) -> list[Jogador]:
		return self._jogadores
	
	@property
	def pontuacao(self) -> Pontuacao:
		return self._pontuacao


