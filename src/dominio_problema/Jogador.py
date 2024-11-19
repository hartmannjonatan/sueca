#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Carta
import Dupla
import Jogo
import Naipe
from typing import List

class Jogador(object):
	def meu_turno(self) -> long:
		pass

	def quantidade_cartas(self) -> int:
		pass

	def add_carta(self, carta : Carta):
		pass

	def remover_carta(self, carta : Dict) -> Carta:
		pass

	def ordenar_cartas(self, naipe_trunfo : Naipe):
		pass

	def cartas_validas(self, naipe_vaza : Naipe___None) -> Carta*:
		pass

	def novas_cartas(self, *cartas : Carta*):
		pass

	def habilitar_turno(self):
		pass

	def desabilitar_turno(self):
		pass

	def reiniciar(self):
		pass

	def definir_vencedor(self):
		pass

	def set_nome(self, nome : String):
		pass

	def __init__(self):
		self._nome : str = None
		self._cartas : Carta* = None
		self._meu_turno : long = None
		self._isLocal : long = None
		self._vencedor : long = None
		self._unnamed_Dupla_ : Dupla = None
		self._unnamed_Dupla_2 : Dupla = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Carta_ = []
		"""# @AssociationMultiplicity 0..10"""
		self._.4 : Jogo = None

