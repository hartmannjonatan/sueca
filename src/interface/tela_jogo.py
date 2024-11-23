from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from images import IMAGES_DIR

from .tela_instrucao import TelaInstrucao
from .tela_pontuacao import TelaPontuacao
from .tela_vencedor import TelaVencedor

from dominio_problema.carta import Carta
from dominio_problema.jogador import Jogador
from dominio_problema.naipe import Naipe


class TelaJogo:

    def __init__(self, janela_principal, canvas, interface_jogador):
        self._janela_principal: Tk  = janela_principal
        self._canvas: Canvas = canvas
        self._interface_jogador = interface_jogador

        self._tela_instrucao = TelaInstrucao()
        self._tela_pontuacao = TelaPontuacao()
        self._tela_vencedor = TelaVencedor(interface_jogador)

        self._label_jogador_atual: Label = None
        self._label_jogador1: Label = None
        self._label_jogador2: Label = None
        self._label_jogador3: Label = None
        self._label_jogador4: Label = None

        self._cartas_vaza: list[Carta, int] = list()
        self._cartas_jogador: list[Carta, int] = list()
        self._imagens_cartas: dict[str, PhotoImage] = dict()
        self._slot_jogadores: dict[str, tuple] = dict()

        self.inicializar_imagens_cartas()
    
    def configurar_tela(self, ordem_jogadores: list[Jogador] = None, jogador_local: Jogador = None):
        self.canvas.delete("all")

        posicao_jogador_local = 0
        for i in range(0, len(ordem_jogadores)):
            if jogador_local == ordem_jogadores[i]:
                posicao_jogador_local = i
            
        jogador1 = jogador_local
        jogador2 = ordem_jogadores[(posicao_jogador_local + 1) % 4]
        jogador3 = ordem_jogadores[(posicao_jogador_local + 2) % 4]
        jogador4 = ordem_jogadores[(posicao_jogador_local + 3) % 4]

        self.configurar_background()
        self.criar_area_jogador_1(jogador1)
        self.criar_area_jogador_2(jogador2)
        self.criar_area_jogador_3(jogador3)
        self.criar_area_jogador_4(jogador4)

        self.criar_area_de_jogo(jogador1, jogador2, jogador3, jogador4)
        self.criar_frame_status()
        self.criar_botoes_menu()
    
    def configurar_background(self):
        imagem_fundo = Image.open(IMAGES_DIR / "tela_jogo/background.png")
        imagem_fundo = imagem_fundo.resize((1200, 700), Image.LANCZOS)
        
        self.imagem_fundo_jogo = ImageTk.PhotoImage(imagem_fundo)

        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo_jogo)
        self.canvas.config(cursor="")

    def criar_area_jogador_1(self, jogador1: Jogador):
        imagem_slot_cartas = Image.open(IMAGES_DIR / "tela_jogo/cardsslot.png")
        imagem_slot_cartas = imagem_slot_cartas.resize((1100, 153), Image.LANCZOS)
        self.imagem_slot_cartas = ImageTk.PhotoImage(imagem_slot_cartas)

        nome_jogador1 = Image.open(IMAGES_DIR / "tela_jogo/playertag.png")
        nome_jogador1 = nome_jogador1.resize((180, 35), Image.LANCZOS)
        self.nome_jogador1 = ImageTk.PhotoImage(nome_jogador1)

        self.canvas.create_image(600, 600, anchor="center", image=self.imagem_slot_cartas)
        self.canvas.create_image(135, 500, anchor="nw", image=self.nome_jogador1)

        nome_jogador = jogador1.nome
        self.label_jogador1 = Label(self.janela_principal, text=nome_jogador, font=("Arial", 14), bg="#F2B035")
        self.label_jogador1.place(anchor="nw", x=140, y=505)
    
    def criar_area_jogador_2(self, jogador2: Jogador):
        bolo_cartas = Image.open(IMAGES_DIR / "tela_jogo/cardsstack.png")
        bolo_cartas = bolo_cartas.resize((167 , 115), Image.LANCZOS)
        bolo_cartas = bolo_cartas.rotate(90, expand=True)
        self.bolo_cartas_jogador_2 = ImageTk.PhotoImage(bolo_cartas)

        nome_jogador2 = Image.open(IMAGES_DIR / "tela_jogo/playertag.png")
        nome_jogador2 = nome_jogador2.resize((180, 35), Image.LANCZOS)
        self.nome_jogador2 = ImageTk.PhotoImage(nome_jogador2)

        self.canvas.create_image(1100, 350, anchor="center", image=self.bolo_cartas_jogador_2)
        self.canvas.create_image(1190, 228, anchor="ne", image=self.nome_jogador2)

        nome_jogador = jogador2.nome
        self.label_jogador2 = Label(self.janela_principal, text=nome_jogador, font=("Arial", 14), bg="#F2B035")
        self.label_jogador2.place(anchor="nw", x=1015, y=233)
    
    def criar_area_jogador_3(self, jogador3: Jogador):
        bolo_cartas = Image.open(IMAGES_DIR / "tela_jogo/cardsstack.png")
        bolo_cartas = bolo_cartas.resize((167 , 115), Image.LANCZOS)
        self.bolo_cartas_jogador_3 = ImageTk.PhotoImage(bolo_cartas)

        nome_jogador3 = Image.open(IMAGES_DIR / "tela_jogo/playertag.png")
        nome_jogador3 = nome_jogador3.resize((180, 35), Image.LANCZOS)
        self.nome_jogador3 = ImageTk.PhotoImage(nome_jogador3)

        self.canvas.create_image(600, 100, anchor="center", image=self.bolo_cartas_jogador_3)
        self.canvas.create_image(600, 185, anchor="center", image=self.nome_jogador3)

        nome_jogador = jogador3.nome
        self.label_jogador2 = Label(self.janela_principal, text=nome_jogador, font=("Arial", 14), bg="#F2B035")
        self.label_jogador2.place(anchor="nw", x=515, y=173)
    
    def criar_area_jogador_4(self, jogador4: Jogador):
        bolo_cartas = Image.open(IMAGES_DIR / "tela_jogo/cardsstack.png")
        bolo_cartas = bolo_cartas.resize((167 , 115), Image.LANCZOS)
        bolo_cartas = bolo_cartas.rotate(90, expand=True)
        self.bolo_cartas_jogador_4 = ImageTk.PhotoImage(bolo_cartas)

        nome_jogador4 = Image.open(IMAGES_DIR / "tela_jogo/playertag.png")
        nome_jogador4 = nome_jogador4.resize((180, 35), Image.LANCZOS)
        self.nome_jogador4 = ImageTk.PhotoImage(nome_jogador4)

        self.canvas.create_image(100, 350, anchor="center", image=self.bolo_cartas_jogador_4)
        self.canvas.create_image(10, 228, anchor="nw", image=self.nome_jogador4)

        nome_jogador = jogador4.nome
        self.label_jogador2 = Label(self.janela_principal, text=nome_jogador, font=("Arial", 14), bg="#F2B035")
        self.label_jogador2.place(anchor="nw", x=15, y=233)

    def criar_frame_status(self):
        frame_jogador_atual = Image.open(IMAGES_DIR / "tela_jogo/actualplayer.png")
        frame_jogador_atual = frame_jogador_atual.resize((350, 40), Image.LANCZOS)
        self.frame_jogador_atual = ImageTk.PhotoImage(frame_jogador_atual)

        self.canvas.create_image(10, 15, anchor="nw", image=self.frame_jogador_atual)
        self.label_jogador_atual = Label(self.janela_principal, text="Aguarde, vez de Henrique...", font=("Arial", 14), bg="#f2f2f2")
        self.label_jogador_atual.place(anchor="nw", x=15, y=20)
        
    def criar_area_de_jogo(self, jogador1: Jogador, jogador2: Jogador, jogador3: Jogador, jogador4: Jogador):
        slot_carta_jogador1 = Image.open(IMAGES_DIR / "tela_jogo/singlecardslot.png")
        slot_carta_jogador1 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador1 = ImageTk.PhotoImage(slot_carta_jogador1)

        carta_jogador1 = Image.open(IMAGES_DIR / "tela_jogo/cartas/k_copas.png")
        carta_jogador1 = carta_jogador1.resize((82, 115), Image.LANCZOS)
        self.carta_jogador1 = ImageTk.PhotoImage(carta_jogador1)

        slot_carta_jogador2 = Image.open(IMAGES_DIR / "tela_jogo/singlecardslot.png")
        slot_carta_jogador2 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador2 = ImageTk.PhotoImage(slot_carta_jogador2)

        carta_jogador2 = Image.open(IMAGES_DIR / "tela_jogo/cartas/q_copas.png")
        carta_jogador2 = carta_jogador2.resize((82, 115), Image.LANCZOS)
        self.carta_jogador2 = ImageTk.PhotoImage(carta_jogador2)

        slot_carta_jogador3 = Image.open(IMAGES_DIR / "tela_jogo/singlecardslot.png")
        slot_carta_jogador3 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador3 = ImageTk.PhotoImage(slot_carta_jogador3)

        slot_carta_jogador4 = Image.open(IMAGES_DIR / "tela_jogo/singlecardslot.png")
        slot_carta_jogador4 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador4 = ImageTk.PhotoImage(slot_carta_jogador4)

        self.canvas.create_image(600, 465, anchor="center", image=self.slot_carta_jogador1)
        self.slot_jogadores[jogador1.nome] = (597, 465)

        self.canvas.create_image(750, 350, anchor="center", image=self.slot_carta_jogador2)
        self.slot_jogadores[jogador2.nome] = (747, 350)

        self.canvas.create_image(600, 275, anchor="center", image=self.slot_carta_jogador3)
        self.slot_jogadores[jogador3.nome] = (597, 275)

        self.canvas.create_image(450, 350, anchor="center", image=self.slot_carta_jogador4)
        self.slot_jogadores[jogador4.nome] = (447, 350)
    
    def criar_botoes_menu(self):
        imagem_botao_naipe_rodada = Image.open(IMAGES_DIR / "tela_jogo/botoes/botao_copas.png")
        imagem_botao_naipe_rodada = imagem_botao_naipe_rodada.resize((50, 50), Image.LANCZOS)
        self.img_botao_naipe_rodada = ImageTk.PhotoImage(imagem_botao_naipe_rodada)

        self.botao_naipe_rodada = self.canvas.create_image(1040, 40, image=self.img_botao_naipe_rodada)

        imagem_botao_pontuacao = Image.open(IMAGES_DIR / "tela_jogo/botoes/botao_pontuacao.png")
        imagem_botao_pontuacao = imagem_botao_pontuacao.resize((50, 50), Image.LANCZOS)
        self.img_botao_pontuacao = ImageTk.PhotoImage(imagem_botao_pontuacao)

        self.botao_pontuacao = self.canvas.create_image(1100, 40, image=self.img_botao_pontuacao)

        self.canvas.tag_bind(self.botao_pontuacao, "<Button-1>", self.click_botao_pontuacao)
        self.canvas.tag_bind(self.botao_pontuacao, "<Enter>", self.on_hover_botao_pontuacao)
        self.canvas.tag_bind(self.botao_pontuacao, "<Leave>", self.saida_botao_pontuacao)

        imagem_botao_instrucao = Image.open(IMAGES_DIR / "tela_jogo/botoes/botao_instrucao.png")
        imagem_botao_instrucao = imagem_botao_instrucao.resize((50, 50), Image.LANCZOS)
        self.img_botao_instrucao = ImageTk.PhotoImage(imagem_botao_instrucao)

        self.botao_instrucao = self.canvas.create_image(1160, 40, image=self.img_botao_instrucao)

        self.canvas.tag_bind(self.botao_instrucao, "<Button-1>", self.click_botao_instrucao)
        self.canvas.tag_bind(self.botao_instrucao, "<Enter>", self.on_hover_botao_instrucao)
        self.canvas.tag_bind(self.botao_instrucao, "<Leave>", self.saida_botao_instrucao)

    def on_hover_botao_pontuacao(self, event):
        imagem_botao_pontuacao = Image.open(IMAGES_DIR / "tela_jogo/botoes/botao_pontuacao.png")
        imagem_botao_pontuacao = imagem_botao_pontuacao.resize((60, 60), Image.LANCZOS)
        self.img_botao_pontuacao_grande = ImageTk.PhotoImage(imagem_botao_pontuacao)

        self.canvas.itemconfig(self.botao_pontuacao, image=self.img_botao_pontuacao_grande)
        self.canvas.config(cursor="hand2")

    def saida_botao_pontuacao(self, event):
        self.canvas.itemconfig(self.botao_pontuacao, image=self.img_botao_pontuacao)
        self.canvas.config(cursor="")

    def click_botao_pontuacao(self, event):
        self.tela_pontuacao.abrir_tela()

    def on_hover_botao_instrucao(self, event):
        imagem_botao_instrucao = Image.open(IMAGES_DIR / "tela_jogo/botoes/botao_instrucao.png")
        imagem_botao_instrucao = imagem_botao_instrucao.resize((60, 60), Image.LANCZOS)
        self.img_botao_instrucao_grande = ImageTk.PhotoImage(imagem_botao_instrucao)

        self.canvas.itemconfig(self.botao_instrucao, image=self.img_botao_instrucao_grande)
        self.canvas.config(cursor="hand2")

    def saida_botao_instrucao(self, event):
        self.canvas.itemconfig(self.botao_instrucao, image=self.img_botao_instrucao)
        self.canvas.config(cursor="")

    def click_botao_instrucao(self, event):
        self.tela_instrucao.abrir_tela()

    def mostrar_aviso(self, event):
        messagebox.showwarning("Aviso", "Você clicou em uma carta!")
    
    def on_hover_carta(self, event):
        self.canvas.config(cursor="hand2")
    
    def saida_carta(self, event):
        self.canvas.config(cursor="")

    def revelar_trunfo(self, trunfo: Naipe):
        pass

    def atualizar_tela_pontuacao(self):
        pass

    def resetar_informacoes_tela_jogo(self):
        pass

    def clicar_carta(self, indice: int):
        pass

    def inicializar_imagens_cartas(self):
        cartas = ["a", "2", "3", "4", "5", "6", "7", "j", "q", "k"]
        naipes = [Naipe.paus.name, Naipe.espadas.name, Naipe.ouros.name, Naipe.copas.name]

        for i in range(0, 10):
            for j in range(0, 4):
                key = f"{cartas[i]}_{naipes[j]}"
                imagem = Image.open(IMAGES_DIR/ f"tela_jogo/cartas/{cartas[i]}_{naipes[j]}.png")
                imagem = imagem.resize((82, 115), Image.LANCZOS)
                self.imagens_cartas[key] = ImageTk.PhotoImage(imagem)

    def on_hover_carta_bloqueada(self):
        pass


    @property
    def janela_principal(self) -> Tk:
        return self._janela_principal
    
    @property
    def canvas(self) -> Canvas:
        return self._canvas
    
    @property
    def interface_jogador(self):
        return self._interface_jogador
    
    @property
    def tela_instrucao(self) -> TelaInstrucao:
        return self._tela_instrucao
    
    @property
    def tela_pontuacao(self) -> TelaPontuacao:
        return self._tela_pontuacao
    
    @property
    def tela_vencedor(self) -> TelaVencedor:
        return self._tela_vencedor
    
    @property
    def label_jogador_atual(self) -> Label:
        return self._label_jogador_atual
    
    @label_jogador_atual.setter
    def label_jogador_atual(self, nova_label):
        self._label_jogador_atual = nova_label

    @property 
    def label_jogador1(self) -> Label:
        return self._label_jogador1
    
    @label_jogador1.setter
    def label_jogador1(self, nova_label):
        self._label_jogador1 = nova_label
    
    @property 
    def label_jogador2(self) -> Label:
        return self._label_jogador2
    
    @label_jogador2.setter
    def label_jogador2(self, nova_label):
        self._label_jogador2 = nova_label
    
    @property 
    def label_jogador3(self) -> Label:
        return self._label_jogador3
    
    @label_jogador3.setter
    def label_jogador3(self, nova_label):
        self._label_jogador3 = nova_label
    
    @property 
    def label_jogador4(self) -> Label:
        return self._label_jogador4
    
    @label_jogador4.setter
    def label_jogador4(self, nova_label):
        self._label_jogador4 = nova_label

    @property
    def cartas_vaza(self) -> list[Carta, int]:
        return self._cartas_vaza
    
    @cartas_vaza.setter
    def cartas_vaza(self, cartas):
        self._cartas_vaza = cartas

    @property
    def cartas_jogador(self) -> list[Carta, int]:
        return self._cartas_jogador
    
    @cartas_jogador.setter
    def cartas_jogador(self, cartas):
        self._cartas_jogador = cartas

    @property
    def imagens_cartas(self) -> dict[str, PhotoImage]:
        return self._imagens_cartas
    
    @property
    def slot_jogadores(self) -> dict[str, tuple]:
        pass 

