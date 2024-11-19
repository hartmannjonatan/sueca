#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Carta
import Jogador
import Naipe
import Rodada
from typing import List

class Vaza(object):
	def vaza_finalizada(self) -> long:
		pass

	def definir_vencedor(self, trunfo : Naipe) -> Jogador:
		pass

	def somar_pontuacao(self) -> int:
		pass

	def jogar_carta(self, carta : Carta, jogador : Jogador):
		pass

	def naipe_vaza(self) -> Naipe___None:
		pass

	def add_carta(self, carta : Carta, jogador : Jogador):
		pass

	def __init__(self):
		self._cartas_jogadas : Carta* = None
		self._primeiro_jogador : Jogador = None
		self._naipe_obrigatorio : Naipe = None
		self._jogadores : Jogador* = None
		self. : Rodada = None
		self._unnamed_Carta_ : Carta = None

