#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Dupla
import Mesa
import Jogador
import InterfaceJogador
from typing import List

class Jogo(object):
	def __init__(self):
		self._duplas : Dupla* = None
		self._mesa : Mesa = None
		self._ordem_jogadores : Jogador* = None
		self._status_jogo : str = None
		self._proximo_jogador : Jogador = None
		self._interface_jogador : InterfaceJogador = None
		self._jogador_local : Jogador = None
		self._partida_encerrada : long = false
		self._rodada_encerrada : long = false
		self._vaza_encerrada : long = false
		self._.4 : Jogador = None
		self._unnamed_Mesa_21 : Mesa = None
		"""# @AssociationKind Composition"""
		self._unnamed_Dupla_22 : Dupla = None
		"""# @AssociationKind Composition"""
		self._unnamed_InterfaceJogador_23 : InterfaceJogador = None

	def jogador_local(self) -> Jogador:
		pass

	def duplas(self) -> Dupla*:
		pass

	def interface_jogador(self) -> InterfaceJogador:
		pass

	def receber_jogada(self, jogada : Dict):
		pass

	def nova_rodada(self, cartas : Dict = None):
		pass

	def habilitar_proximo_jogador(self, vencedor : Jogador___None):
		pass

	def atualizar_tela_jogo(self):
		pass

	def avaliar_jogada(self):
		pass

	def atualizar_galhos(self):
		pass

	def avaliar_dupla_vencedora(self) -> Dupla_____None:
		pass

	def jogar_carta(self, indice_carta : int):
		pass

	def inicializar_jogadores_duplas_e_mesa(self, **jogadores : str**, id_jogador_local : str):
		pass

	def definir_jogadores(self, jogadores : string____, id_jogador_local : str):
		pass

	def ordem_jogadores(self) -> Jogador*:
		pass

	def reiniciar_partida(self):
		pass

