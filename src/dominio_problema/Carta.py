#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Naipe
import Jogador
import Baralho
from typing import List

class Carta(object):
	def __init__(self):
		self._numero : str = None
		self._naipe : Naipe = None
		self._valor : int = None
		self._nome : str = None
		self._unnamed_Jogador_ : Jogador = None
		self._unnamed_Baralho_ : Baralho = None
		self._unnamed_Naipe_ : Naipe = None
		self._unnamed_Vaza_ = []
		"""# @AssociationMultiplicity 0..4"""

