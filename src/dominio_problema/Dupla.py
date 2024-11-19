#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Jogador
import Pontuacao
import Jogo
from typing import List

class Dupla(object):
	def zerar_pontuacao_rodada(self):
		pass

	def add_pontuacao(self, pontuacao : int):
		pass

	def set_galhos(self, galhos : int):
		pass

	def reiniciar(self):
		pass

	def __init__(self):
		self._jogadores : Jogador* = None
		self._pontuacao : Pontuacao = None
		self._unnamed_Jogo_24 : Jogo = None
		self._unnamed_Jogador_ = []
		"""# @AssociationMultiplicity 2
		# @AssociationKind Composition"""
		self._unnamed_Jogador_2 = []
		"""# @AssociationMultiplicity 2
		# @AssociationKind Aggregation"""
		self._unnamed_Pontuacao_ : Pontuacao = None
		"""# @AssociationMultiplicity 1
		# @AssociationKind Composition"""

