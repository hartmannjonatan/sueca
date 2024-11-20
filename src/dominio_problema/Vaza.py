from carta import Carta
from jogador import Jogador
from naipe import Naipe
from rodada import Rodada


class Vaza:
	def __init__(self):
		self._cartas_jogadas : list[Carta] = None
		self._primeiro_jogador : Jogador = None
		self._naipe_obrigatorio : Naipe = None
		self._jogadores : list[Jogador] = None

	def vaza_finalizada(self) -> bool:
		pass

	def definir_vencedor(self, trunfo : Naipe) -> Jogador:
		pass

	def somar_pontuacao(self) -> int:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe | None:
		pass

	def add_carta(self, carta : Carta, jogador : Jogador):
		pass

	@property
	def cartas_jogadas(self) -> list[Carta]:
		return self._cartas_jogadas
	
	@property
	def primeiro_jogador(self) -> Jogador:
		return self._primeiro_jogador
	
	@property
	def naipe_obrigatorio(self) -> Naipe:
		return self._naipe_obrigatorio
	
	@property
	def jogadores(self) -> list[Jogador]:
		return self._jogadores


