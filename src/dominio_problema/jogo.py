from time import sleep
from dominio_problema.naipe import Naipe
from .dupla import Dupla
from .mesa import Mesa
from .jogador import Jogador
from .vaza import Vaza


class Jogo:
	def __init__(self, interface_jogador):
		self._duplas : list[Dupla] = None
		self._mesa : Mesa = None
		self._ordem_jogadores : list[Jogador] = None
		self._status_jogo : str = None
		self._proximo_jogador : Jogador = None
		self._interface_jogador = interface_jogador
		self._jogador_local : Jogador = None
		self._partida_encerrada : bool = False
		self._rodada_encerrada : bool = False
		self._vaza_encerrada : bool = False	

	def receber_jogada(self, jogada : dict):
		carta_jogada = self.proximo_jogador.remover_carta(jogada["carta_jogada"])
		self.mesa.jogar_carta(carta_jogada, self.proximo_jogador)

		vencedor_vaza: Jogador = None
		for jogador in self.ordem_jogadores:
			if jogada["vencedor_vaza"] == jogador.nome:
				vencedor_vaza = jogador
				break
		
		if jogada["status_vaza"] == "encerrada":
			self.vaza_encerrada = True
			for dupla in self.duplas:
				pontuacao = jogada["pontuacao_duplas"].get(dupla.jogadores[0].nome)
				pontuacao = jogada["pontuacao_duplas"].get(dupla.jogadores[1].nome) if pontuacao is None else pontuacao
				dupla.add_pontuacao(pontuacao)

			if jogada["status_rodada"] == "encerrada":
				self.rodada_encerrada = True
				for dupla in self.duplas:
					galhos = jogada["galhos_duplas"].get(dupla.jogadores[0].nome)
					if galhos is None:
						galhos = jogada["galhos_duplas"].get(dupla.jogadores[1].nome)
					dupla.set_galhos(galhos)
				
				self.status_jogo = "Rodada Encerrada. Galhos atualizados!"
				self.interface_jogador.atualizar_status_tela_jogo(self.status_jogo) # NOVO ADICIONAR NO DIAGRAMA
				#sleep(5) # NOVO ADICIONAR NO DIAGRAMA

				if jogada["status_partida"] == "encerrada":
					self.partida_encerrada = True
					self.status_jogo = "A partida foi encerrada!"
					vencedora = self.avaliar_dupla_vencedora()
					self.atualizar_tela_jogo(self.status_jogo, self.mesa.rodadas[-1].vazas[-1], self.jogador_local)
					self.interface_jogador.atualizar_tela_vencedor(vencedora)
			else:
				self.rodada_encerrada = False
				self.partida_encerrada = False
				self.status_jogo = "Vaza finalizada! Pontuações atualizadas."
				self.atualizar_tela_jogo(self.status_jogo, self.mesa.rodadas[-1].vazas[-1], self.jogador_local) # NOVO ADICIONAR NO DIAGRAMA
				#sleep(5) # NOVO ADICIONAR NO DIAGRAMA
				nova_vaza = self.mesa.nova_vaza()
				self.atualizar_tela_jogo(self.status_jogo, nova_vaza, self.jogador_local)
				self.habilitar_proximo_jogador(vencedor_vaza)
				self.status_jogo = f"Vez de {jogada['proximo_jogador']}" if jogada['proximo_jogador'] != self.jogador_local.nome else "Sua vez de jogar!"
				self.interface_jogador.atualizar_status_tela_jogo(self.status_jogo)
		else:
			self.vaza_encerrada = False
			self.status_jogo = f"Vez de {jogada['proximo_jogador']}" if jogada['proximo_jogador'] != self.jogador_local.nome else "Sua vez de jogar!"
			self.atualizar_tela_jogo(self.status_jogo, self.mesa.rodadas[-1].vazas[-1], self.jogador_local)
			self.habilitar_proximo_jogador(None)

		if jogada["status_rodada"] == "encerrada" and jogada["status_partida"] == "não encerrada":
			for jogador in self.ordem_jogadores:
				if jogada["proximo_jogador"] == jogador.nome:
					self.proximo_jogador = jogador 
					break
			self.nova_rodada()

	def nova_rodada(self):
		self.mesa.nova_rodada()
		self.duplas[0].zerar_pontuacao_rodada()
		self.duplas[1].zerar_pontuacao_rodada()

		self.habilitar_proximo_jogador(self.proximo_jogador)

		meu_turno = self.jogador_local.meu_turno

		if meu_turno:
			cartas_novo_baralho, naipe_trunfo = self.mesa.novo_baralho()

			jogada = {
				"tipo" : "nova rodada",
				"cartas" : {
				},
				"trunfo" : f"{naipe_trunfo.name}",
				"match_status" : "next"
			}

			for i in range(len(self.ordem_jogadores)):
				self.ordem_jogadores[i].novas_cartas(cartas_novo_baralho[i])
				self.ordem_jogadores[i].ordenar_cartas(naipe_trunfo)
				jogada["cartas"][self.ordem_jogadores[i].id] = []
				for carta in cartas_novo_baralho[i]:
					jogada["cartas"][self.ordem_jogadores[i].id].append({"carta": f"{carta.numero}", "naipe" : f"{carta.naipe.name}"})

			self.interface_jogador.enviar_jogada(jogada)
			vaza = self.mesa.nova_vaza()
			self.status_jogo = f"Nova rodadada iniciada!"
			self.atualizar_tela_jogo(self.status_jogo, vaza, self.jogador_local)
			self.interface_jogador.revelar_trunfo(naipe_trunfo)
			self.habilitar_proximo_jogador(None)
			self.status_jogo = "Sua vez de jogar!" if self.jogador_local.meu_turno else f"Vez do jogador {self.proximo_jogador.nome}"
			self.interface_jogador.atualizar_status_tela_jogo(self.status_jogo)
			
		else:
			vaza = self.mesa.nova_vaza()
			self.status_jogo = "Aguardando distribuição de cartas..."
			self.atualizar_tela_jogo(self.status_jogo, vaza, self.jogador_local)

	def receber_nova_rodada(self, cartas : dict, naipe_trunfo: Naipe):
		self.mesa.novas_cartas(cartas, self.ordem_jogadores, naipe_trunfo)
		self.status_jogo = f"Nova rodadada iniciada!"
		self.atualizar_tela_jogo(self.status_jogo, self.mesa.rodadas[-1].vazas[-1], self.jogador_local)
		self.interface_jogador.revelar_trunfo(naipe_trunfo)
		self.habilitar_proximo_jogador(None)
		self.status_jogo = "Sua vez de jogar!" if self.jogador_local.meu_turno else f"Vez do jogador {self.proximo_jogador.nome}"
		self.interface_jogador.atualizar_status_tela_jogo(self.status_jogo)

	def habilitar_proximo_jogador(self, vencedor : Jogador | None):
		for jogador in self.ordem_jogadores:
			jogador.desabilitar_turno()

		if vencedor == None:
			for i in range(len(self.ordem_jogadores)):
				if self.proximo_jogador == self.ordem_jogadores[i]:
					self.proximo_jogador = self.ordem_jogadores[(i+1) % 4]
					break
		else:
			self.proximo_jogador = vencedor

		self.proximo_jogador.habilitar_turno()

		if self.proximo_jogador.id == self.jogador_local.id:
			quantidade_cartas = self.proximo_jogador.quantidade_cartas()

			if quantidade_cartas > 0:
				naipe = self.mesa.naipe_vaza()
				cartas_validas = self.proximo_jogador.cartas_validas(naipe)
				self.interface_jogador.habilitar_cartas(cartas_validas)

	def atualizar_tela_jogo(self, status: str, vaza: Vaza, jogador_local: Jogador):
		self.interface_jogador.atualizar_interface_jogo(status, vaza, jogador_local)

	def avaliar_jogada(self):
		jogada = self.mesa.avaliar_jogada()
		self.interface_jogador.enviar_jogada(jogada)
		if self.rodada_encerrada and not self.partida_encerrada:
			self.nova_rodada()

	def atualizar_galhos(self):
		for i in range(2):
			pontuacao = self.duplas[i].pontuacao.pontos
			galhos = 0
			if pontuacao >=60 and pontuacao < 90:
				galhos = 1
			if pontuacao >= 90 and pontuacao < 120:
				galhos = 2
			if pontuacao >= 120:
				galhos = 4
			self.duplas[i].pontuacao.galhos += galhos

	def avaliar_dupla_vencedora(self) -> list[Dupla] | None:
		vencedora = None
		if self.duplas[0].pontuacao.galhos >= 4 or self.duplas[1].pontuacao.galhos >= 4:
			vencedora = []
			if self.duplas[0].pontuacao.galhos >= 4:
				vencedora.append(self.duplas[0])
				self.duplas[0].jogadores[0].definir_vencedor()
				self.duplas[0].jogadores[1].definir_vencedor()
			if self.duplas[1].pontuacao.galhos >= 4:
				vencedora.append(self.duplas[1])
				self.duplas[1].jogadores[0].definir_vencedor()
				self.duplas[1].jogadores[1].definir_vencedor()
		return vencedora

	def jogar_carta(self, indice_carta : int):
		if self.jogador_local.meu_turno:
			carta = self.jogador_local.jogar_carta(indice_carta)
			self.mesa.jogar_carta(carta, self.jogador_local)
			self.avaliar_jogada()

	def inicializar_jogadores_duplas_e_mesa(self, jogadores : list[list[str]], id_jogador_local : str):
		self.definir_jogadores(jogadores, id_jogador_local)

		self.duplas = list()
		dupla1 = Dupla(self.ordem_jogadores[0], self.ordem_jogadores[2])
		dupla2 = Dupla(self.ordem_jogadores[1], self.ordem_jogadores[3])
		self.duplas.append(dupla1)
		self.duplas.append(dupla2)

		self.proximo_jogador = self.ordem_jogadores[0]
		self.mesa = Mesa(self)

	def definir_jogadores(self, jogadores : list[list[str]], id_jogador_local : str):
		self.ordem_jogadores = [None, None, None, None]

		for i in range(0, 4):
			nome = jogadores[i][0]
			id_jogador = jogadores[i][1]
			ordem = jogadores[i][2]
			jogador = Jogador(nome, id_jogador)
			self.ordem_jogadores[int(ordem)-1] = jogador

			if id_jogador == id_jogador_local:
				self.jogador_local = jogador
				jogador.isLocal = True

	def reiniciar_partida(self):
		self.partida_encerrada = False
		for dupla in self.duplas:
			dupla.zerar_pontuacao_rodada()
			dupla.set_galhos(0)
			for jogador in dupla.jogadores:
				jogador.vencedor = False
		self.mesa.reiniciar()
		self.interface_jogador.tela_jogo.configurar_tela(self.ordem_jogadores, self.jogador_local)
		self.nova_rodada()
				

	@property
	def duplas(self) -> list[Dupla]:
		return self._duplas
	
	@duplas.setter
	def duplas(self, duplas):
		self._duplas = duplas

	@property
	def mesa(self) -> Mesa:
		return self._mesa
	
	@mesa.setter
	def mesa(self, mesa):
		self._mesa = mesa

	@property
	def ordem_jogadores(self) -> list[Jogador]:
		return self._ordem_jogadores
	
	@ordem_jogadores.setter
	def ordem_jogadores(self, ordem_jogadores):
		self._ordem_jogadores = ordem_jogadores
	
	@property
	def status_jogo(self) -> str:
		return self._status_jogo

	@status_jogo.setter
	def status_jogo(self, status_jogo):
		self._status_jogo = status_jogo
	
	@property
	def proximo_jogador(self) -> Jogador:
		return self._proximo_jogador
	
	@proximo_jogador.setter
	def proximo_jogador(self, proximo_jogador):
		self._proximo_jogador = proximo_jogador
	
	@property
	def interface_jogador(self):
		return self._interface_jogador
	
	@property
	def jogador_local(self) -> Jogador:
		return self._jogador_local
	
	@jogador_local.setter
	def jogador_local(self, jogador_local):
		self._jogador_local = jogador_local

	@property
	def partida_encerrada(self) -> bool:
		return self._partida_encerrada
	
	@partida_encerrada.setter
	def partida_encerrada(self, partida_encerrada):
		self._partida_encerrada = partida_encerrada
	
	@property
	def rodada_encerrada(self) -> bool:
		return self._rodada_encerrada
	
	@rodada_encerrada.setter
	def rodada_encerrada(self, rodada_encerrada):
		self._rodada_encerrada = rodada_encerrada
	
	@property
	def vaza_encerrada(self) -> bool:
		return self._vaza_encerrada
	
	@vaza_encerrada.setter
	def vaza_encerrada(self, vaza_encerrada):
		self._vaza_encerrada = vaza_encerrada


