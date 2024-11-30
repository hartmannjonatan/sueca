from .carta import Carta
from .naipe import Naipe 


class Jogador:
	def __init__(self, nome, id):
		self._nome : str = nome
		self._cartas : list[Carta] = list()
		self._meu_turno : bool = None
		self._isLocal : bool = None
		self._vencedor : bool = None
		self._id : int = id

	def quantidade_cartas(self) -> int:
		return len(self.cartas)
	
	def add_carta(self, carta : Carta):
		self.cartas.append(carta)

	def remover_carta(self, carta : dict) -> Carta:
		for c in self.cartas:
			if c.naipe.name == carta["naipe"] and c.numero == carta["carta"]:
				self.cartas.remove(c)
				return c
		print(f"CARTA {carta["carta"]}_{carta['naipe']} NÃO ENCONTRADA NA MÃO DE JOGADOR {self.nome}")
	
	def jogar_carta(self, indice: int) -> Carta:
		return self.cartas.pop(indice)

	def ordenar_cartas(self, naipe_trunfo : Naipe):
		ouros = list()
		copas = list()
		espadas = list()
		paus = list()

		for carta in self.cartas:
			if carta.naipe == Naipe.ouros:
				ouros.append(carta)
			elif carta.naipe == Naipe.copas:
				copas.append(carta)
			elif carta.naipe == Naipe.espadas:
				espadas.append(carta)
			else:
				paus.append(carta)
		
		trunfo = list()
		self.cartas = list()

		for cartas_naipe in [paus, copas, espadas, ouros]:
			ordem_cartas = ["a", "2", "3", "4", "5", "6", "7", "j", "q", "k"]
			cartas_naipe = sorted(cartas_naipe, key=lambda carta: ordem_cartas.index(carta.numero))

			if len(cartas_naipe) > 0:
				if cartas_naipe[0].naipe == naipe_trunfo:
					trunfo = cartas_naipe
					continue
				else:
					self.cartas += cartas_naipe
				
		self.cartas += trunfo

	def cartas_validas(self, naipe_vaza : Naipe | None) -> list[Carta]:
		cartas_validas = list()
		quantidade_cartas = self.quantidade_cartas()

		if naipe_vaza == None:
			cartas_validas = self.cartas
		else:
			contador_cartas = 0

			for i in range(0, quantidade_cartas):
				if self.cartas[i].naipe == naipe_vaza:
					cartas_validas.append(self.cartas[i])	
					contador_cartas += 1
				else:
					cartas_validas.append(None)
				
			if contador_cartas == 0:
				cartas_validas = self.cartas
			
		return cartas_validas

	def novas_cartas(self, cartas : list[Carta]):
		self.cartas = cartas

	def habilitar_turno(self):
		self.meu_turno = True

	def desabilitar_turno(self):
		self.meu_turno = False

	def reiniciar(self):
		pass

	def definir_vencedor(self):
		self.vencedor = True

	@property
	def nome(self) -> str:
		return self._nome
	
	@nome.setter
	def nome(self, nome: str):
		self._nome = nome

	@property
	def cartas(self) -> list[Carta]:
		return self._cartas

	@cartas.setter
	def cartas(self, cartas):
		self._cartas = cartas
	
	@property
	def meu_turno(self) -> bool:
		return self._meu_turno
	
	@meu_turno.setter
	def meu_turno(self, meu_turno):
		self._meu_turno = meu_turno
	
	@property
	def isLocal(self) -> bool:
		return self._isLocal
	
	@isLocal.setter
	def isLocal(self, isLocal):
		self._isLocal = isLocal
	
	@property
	def vencedor(self) -> bool:
		return self._vencedor
	
	@property
	def id(self) -> int:
		return self._id
	
	@id.setter
	def id(self, id):
		self._id = id

