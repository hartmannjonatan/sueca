from time import sleep
from .baralho import Baralho
from .rodada import Rodada
from .naipe import Naipe
from .carta import Carta
from .jogador import Jogador
from .vaza import Vaza

class Mesa:
	def __init__(self, jogo):
		self._baralho : Baralho = None
		self._rodadas : list[Rodada] = list()
		self._jogo = jogo
	
	def nova_rodada(self):
		self.jogo.rodada_encerrada = False
		nova_rodada = Rodada()
		self.rodadas.append(nova_rodada)

	def novo_baralho(self) -> tuple[list[Carta], Naipe]:
		self.baralho = Baralho()
		cartas, naipe_trunfo = self.baralho.distribuir_cartas()
		self.rodadas[len(self.rodadas)-1].definir_trunfo(naipe_trunfo)

		return cartas, naipe_trunfo

	def novas_cartas(self, cartas : dict, jogadores : list[Jogador], naipe_trunfo : Naipe):
		if self.baralho == None:
			self._baralho = Baralho()
		self.baralho.novas_cartas(cartas, jogadores, naipe_trunfo)
		self.rodadas[len(self.rodadas)-1].definir_trunfo(naipe_trunfo)
			
	def nova_vaza(self) -> Vaza:
		self.jogo.vaza_encerrada = False
		return self.rodadas[len(self.rodadas)-1].nova_vaza()

	def avaliar_jogada(self) -> dict:
		pontuacao, vencedor = self.rodadas[-1].avaliar_vaza()
		jogada = {
			"match_status": "next",
			"tipo": "jogada",
			"carta_jogada": {"carta": self.rodadas[-1].vazas[-1].cartas_jogadas[-1].numero, "naipe": self.rodadas[-1].vazas[-1].cartas_jogadas[-1].naipe.name},
			"status_vaza": None,
			"vencedor_vaza": None,
			"status_rodada": None,
			"status_partida": None,
			"proximo_jogador": None,
			"pontuacao_duplas": {},
			"galhos_duplas": {}
		}

		if vencedor == None:
			jogada["status_vaza"] = "nao encerrada"
			self.jogo.vaza_encerrada = False
			jogada["status_rodada"] = "nao encerrada"
			self.jogo.rodada_encerrada = False
			jogada["status_partida"] = "nao encerrada"
			self.jogo.partida_encerrada = False
			self.jogo.atualizar_tela_jogo(None, self.rodadas[-1].vazas[-1], self.jogo.jogador_local)
			self.jogo.habilitar_proximo_jogador(None)
			self.jogo.status_jogo = "Sua vez de jogar!" if self.jogo.jogador_local.meu_turno else f"Vez do jogador {self.jogo.proximo_jogador.nome}"
			self.jogo.interface_jogador.atualizar_status_tela_jogo(self.jogo.status_jogo)
		else:
			jogada["status_vaza"] = "encerrada"
			self.jogo.vaza_encerrada = True
			jogada["vencedor_vaza"] = vencedor.nome

			for dupla in self.jogo.duplas:
				jogada["pontuacao_duplas"][dupla.jogadores[0].nome] = 0
				if vencedor in dupla.jogadores:
					dupla.add_pontuacao(pontuacao)
					jogada["pontuacao_duplas"][dupla.jogadores[0].nome] = pontuacao

			rodada_finalizada = self.rodadas[-1].rodada_finalizada()

			if rodada_finalizada:
				self.jogo.atualizar_galhos()
				jogada["status_rodada"] = "encerrada"
				self.jogo.rodada_encerrada = True
				for dupla in self.jogo.duplas:
					jogada["galhos_duplas"][dupla.jogadores[0].nome] = dupla.pontuacao.galhos

				self.jogo.status_jogo = "Rodada finalizada! Galhos atualizados."
				self.jogo.interface_jogador.atualizar_status_tela_jogo(self.jogo.status_jogo)
				sleep(3) 

				vencedora = self.jogo.avaliar_dupla_vencedora()
				if vencedora != None:
					jogada["status_partida"] = "encerrada"
					self.jogo.partida_encerrada = True
					self.jogo.status_jogo = "A partida foi encerrada!"
					self.jogo.atualizar_tela_jogo(self.jogo.status_jogo, self.rodadas[-1].vazas[-1], self.jogo.jogador_local)
					self.jogo.interface_jogador.atualizar_tela_vencedor(vencedora)
				else:
					jogada["status_partida"] = "nao encerrada"
					self.jogo.partida_encerrada = False
					self.jogo.status_jogo = "Uma nova rodada será iniciada!"
					self.jogo.atualizar_tela_jogo(self.jogo.status_jogo, self.rodadas[-1].vazas[-1], self.jogo.jogador_local)
					self.jogo.proximo_jogador = vencedor 
			else:
				jogada["status_rodada"] = "nao encerrada"
				self.jogo.rodada_encerrada = False
				self.jogo.status_jogo = "Vaza finalizada! Pontuações atualizadas."
				self.jogo.atualizar_tela_jogo(self.jogo.status_jogo, self.rodadas[-1].vazas[-1], self.jogo.jogador_local) # NOVO ADICIONAR NO DIAGRAMA
				sleep(3) 
				nova_vaza = self.nova_vaza()
				self.jogo.status_jogo = "Nova vaza iniciada!"
				self.jogo.atualizar_tela_jogo(self.jogo.status_jogo, nova_vaza, self.jogo.jogador_local)
				self.jogo.habilitar_proximo_jogador(vencedor)
				self.jogo.status_jogo = "Sua vez de jogar!" if self.jogo.jogador_local.meu_turno else f"Vez do jogador {self.jogo.proximo_jogador.nome}"
				self.jogo.interface_jogador.atualizar_status_tela_jogo(self.jogo.status_jogo)
		
		jogada["proximo_jogador"] = self.jogo.proximo_jogador.nome

		return jogada


	def jogar_carta(self, carta : Carta, jogador : Jogador):
		self.rodadas[-1].jogar_carta(carta, jogador)

	def naipe_vaza(self) -> Naipe | None:
		return self.rodadas[-1].naipe_vaza()
	
	def reiniciar(self):
		self.rodadas = list()
		

	@property
	def baralho(self) -> Baralho:
		return self._baralho
	
	@baralho.setter
	def baralho(self, baralho):
		self._baralho = baralho
	
	@property
	def rodadas(self) -> list[Rodada]:
		return self._rodadas
	
	@rodadas.setter
	def rodadas(self, rodada):
		self._rodadas = rodada

	@property
	def jogo(self):
		return self._jogo
	
	@jogo.setter
	def jogo(self, jogo):
		self._jogo = jogo

