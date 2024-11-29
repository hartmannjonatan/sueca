from .jogador import Jogador
from .carta import Carta
from .naipe import Naipe

import random

class Baralho:
	def __init__(self):
		self._cartas : list[Carta] = list()

		self.gerar_cartas()

	def gerar_cartas(self):
		for (carta, naipe) in [(c, n) for c in ["a", "2", "3", "4", "5", "6", "7", "j", "q", "k"] for n in [Naipe.paus, Naipe.copas, Naipe.espadas, Naipe.ouros]]:
			self.cartas.append(Carta(carta, naipe))
			
	def distribuir_cartas(self) -> None:
		cartas_jogadores = list()
		cartas_baralho = self.cartas

		random.shuffle(cartas_baralho)
		random.shuffle(cartas_baralho)
		random.shuffle(cartas_baralho)
	
		naipe_trunfo = cartas_baralho[0].naipe

		for i in range(4):
			mao = list()
			for j in range(10):
				carta = cartas_baralho.pop()
				mao.append(carta)
			cartas_jogadores.append(mao)
	
		return cartas_jogadores, naipe_trunfo

	def novas_cartas(self, cartas : dict, jogadores : list[Jogador], naipe_trunfo: Naipe):
		for id in cartas.keys():
			for jogador in jogadores:
				if jogador.id == id:
					for carta in cartas[id]:
						jogador.add_carta(Carta(carta["carta"], Naipe[carta["naipe"]]))
					jogador.ordenar_cartas(naipe_trunfo)
				

	@property
	def cartas(self) -> list[Carta]:
		return self._cartas

	@cartas.setter
	def cartas(self, cartas):
		self._cartas = cartas

