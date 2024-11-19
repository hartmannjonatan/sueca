#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Baralho
import Rodada
import Jogo
import Jogador
import Naipe
import Carta
from typing import List

class Mesa(object):
	def nova_rodada(self):
		pass

	def novo_baralho(self) -> Tuple_Carta____Naipe_:
		pass

	def novas_cartas(self, cartas : Dict, *jogadores : Jogador*, naipe_trunfo : Naipe):
		pass

	def nova_vaza(self):
		pass

	def avaliar_jogada(self) -> Dict:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe___None:
		pass

	def __init__(self):
		self._baralho : Baralho = None
		self._rodadas : Rodada* = None
		self._unnamed_Jogo_ : Jogo = None
		self._unnamed_Baralho_ : Baralho = None
		"""# @AssociationMultiplicity 1
		# @AssociationKind Composition"""
		self._unnamed_Rodada_ = []
		"""# @AssociationMultiplicity 1..*
		# @AssociationKind Aggregation"""

