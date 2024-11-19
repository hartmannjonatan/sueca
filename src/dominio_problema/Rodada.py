#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Vaza
import Naipe
import Mesa
import Carta
import Jogador
from typing import List

class Rodada(object):
	def nova_vaza(self):
		pass

	def definir_trunfo(self, naipe_trunfo : Naipe):
		pass

	def avaliar_vaza(self) -> Tuple_Int__Jogador_:
		pass

	def rodada_finalizada(self) -> long:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe___None:
		pass

	def __init__(self):
		self._vazas : Vaza* = None
		self._trunfo : Naipe = None
		self._unnamed_Mesa_ : Mesa = None
		self. : Vaza = None
		"""# @AssociationKind Composition"""

