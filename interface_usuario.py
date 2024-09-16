from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class InterfaceUsuario:

    def __init__(self):
        self.janela_principal = Tk()

        self.configurar_tela_inicial()

        self.janela_principal.mainloop()

    def configurar_tela_inicial(self):
        largura = 1200
        altura = 700
        
        self.janela_principal.title("Sueca")
        self.janela_principal.geometry("1200x700")
        self.janela_principal.resizable(False, False)

        imagem_fundo = Image.open("images/tela_inicial/background.png")
        imagem_fundo = imagem_fundo.resize((largura, altura), Image.LANCZOS)
        
        self.imagem_fundo_inicial = ImageTk.PhotoImage(imagem_fundo)

        self.canvas = Canvas(self.janela_principal, width=largura, height=altura)
        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo_inicial)
       
        x = (self.janela_principal.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.janela_principal.winfo_screenheight() // 2) - (altura // 2) - 10
        self.janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")

        imagem_botao = Image.open("images/tela_inicial/botao_jogar.png")
        imagem_botao = imagem_botao.resize((200, 80), Image.LANCZOS)
        self.imagem_botao = ImageTk.PhotoImage(imagem_botao)

        self.botao_jogar = self.canvas.create_image(600, 450, anchor="center", image=self.imagem_botao)

        self.canvas.tag_bind(self.botao_jogar, "<Button-1>", self.iniciar_jogo)
        self.canvas.tag_bind(self.botao_jogar, "<Enter>", self.on_hover_botao_jogar)
        self.canvas.tag_bind(self.botao_jogar, "<Leave>", self.saida_botao_jogar)

    def iniciar_jogo(self, event):
        self.configurar_janela_jogo()

    def on_hover_botao_jogar(self, event):
        imagem_botao = Image.open("images/tela_inicial/botao_jogar.png")
        imagem_botao = imagem_botao.resize((210, 85), Image.LANCZOS)
        self.imagem_botao_grande = ImageTk.PhotoImage(imagem_botao)

        self.canvas.itemconfig(self.botao_jogar, image=self.imagem_botao_grande)

    def saida_botao_jogar(self, event):
        self.canvas.itemconfig(self.botao_jogar, image=self.imagem_botao)

    def configurar_janela_jogo(self):
        self.canvas.delete("all")

        self.configurar_background()
        self.criar_area_jogador_1()
        self.criar_area_jogador_2()
        self.criar_area_jogador_3()
        self.criar_area_jogador_4()
        self.criar_area_de_jogo()
        self.criar_frame_jogador_atual()
        self.criar_botoes_menu()
        
    def configurar_background(self):
        imagem_fundo = Image.open("images/tela_jogo/background.png")
        imagem_fundo = imagem_fundo.resize((1200, 700), Image.LANCZOS)
        
        self.imagem_fundo_jogo = ImageTk.PhotoImage(imagem_fundo)

        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo_jogo)
    
    def criar_area_jogador_1(self):
        imagem_slot_cartas = Image.open("images/tela_jogo/cardsslot.png")
        imagem_slot_cartas = imagem_slot_cartas.resize((1100, 153), Image.LANCZOS)
        self.imagem_slot_cartas = ImageTk.PhotoImage(imagem_slot_cartas)

        imagem_carta1 = Image.open("images/tela_jogo/cartas/a_paus.png")
        imagem_carta1 = imagem_carta1.resize((82, 115), Image.LANCZOS)
        self.imagem_carta1 = ImageTk.PhotoImage(imagem_carta1)

        imagem_carta2 = Image.open("images/tela_jogo/cartas/a_espadas.png")
        imagem_carta2 = imagem_carta2.resize((82, 115), Image.LANCZOS)
        self.imagem_carta2 = ImageTk.PhotoImage(imagem_carta2)

        nome_jogador1 = Image.open("images/tela_jogo/playertag.png")
        nome_jogador1 = nome_jogador1.resize((180, 30), Image.LANCZOS)
        self.nome_jogador1 = ImageTk.PhotoImage(nome_jogador1)

        self.canvas.create_image(600, 600, anchor="center", image=self.imagem_slot_cartas)
        self.carta1 = self.canvas.create_image(180, 605, anchor="center", image=self.imagem_carta1)
        self.carta2 = self.canvas.create_image(271, 605, anchor="center", image=self.imagem_carta2)
        self.canvas.create_image(135, 500, anchor="nw", image=self.nome_jogador1)

        self.canvas.tag_bind(self.carta1, "<Button-1>", self.mostrar_aviso)
        self.canvas.tag_bind(self.carta2, "<Button-1>", self.mostrar_aviso)
    
    def criar_area_jogador_2(self):
        bolo_cartas = Image.open("images/tela_jogo/cardsstack.png")
        bolo_cartas = bolo_cartas.resize((167 , 115), Image.LANCZOS)
        bolo_cartas = bolo_cartas.rotate(90, expand=True)
        self.bolo_cartas_jogador_2 = ImageTk.PhotoImage(bolo_cartas)

        nome_jogador2 = Image.open("images/tela_jogo/playertag.png")
        nome_jogador2 = nome_jogador2.resize((180, 30), Image.LANCZOS)
        self.nome_jogador2 = ImageTk.PhotoImage(nome_jogador2)

        self.canvas.create_image(1100, 350, anchor="center", image=self.bolo_cartas_jogador_2)
        self.canvas.create_image(1190, 228, anchor="ne", image=self.nome_jogador2)
    
    def criar_area_jogador_3(self):
        bolo_cartas = Image.open("images/tela_jogo/cardsstack.png")
        bolo_cartas = bolo_cartas.resize((167 , 115), Image.LANCZOS)
        self.bolo_cartas_jogador_3 = ImageTk.PhotoImage(bolo_cartas)

        nome_jogador3 = Image.open("images/tela_jogo/playertag.png")
        nome_jogador3 = nome_jogador3.resize((180, 30), Image.LANCZOS)
        self.nome_jogador3 = ImageTk.PhotoImage(nome_jogador3)

        self.canvas.create_image(600, 100, anchor="center", image=self.bolo_cartas_jogador_3)
        self.canvas.create_image(600, 185, anchor="center", image=self.nome_jogador3)
    
    def criar_area_jogador_4(self):
        bolo_cartas = Image.open("images/tela_jogo/cardsstack.png")
        bolo_cartas = bolo_cartas.resize((167 , 115), Image.LANCZOS)
        bolo_cartas = bolo_cartas.rotate(90, expand=True)
        self.bolo_cartas_jogador_4 = ImageTk.PhotoImage(bolo_cartas)

        nome_jogador4 = Image.open("images/tela_jogo/playertag.png")
        nome_jogador4 = nome_jogador4.resize((180, 30), Image.LANCZOS)
        self.nome_jogador4 = ImageTk.PhotoImage(nome_jogador4)

        self.canvas.create_image(100, 350, anchor="center", image=self.bolo_cartas_jogador_4)
        self.canvas.create_image(10, 228, anchor="nw", image=self.nome_jogador4)

    def criar_frame_jogador_atual(self):
        frame_jogador_atual = Image.open("images/tela_jogo/actualplayer.png")
        frame_jogador_atual = frame_jogador_atual.resize((350, 30), Image.LANCZOS)
        self.frame_jogador_atual = ImageTk.PhotoImage(frame_jogador_atual)

        self.canvas.create_image(10, 15, anchor="nw", image=self.frame_jogador_atual)
        
    def criar_area_de_jogo(self):
        slot_carta_jogador1 = Image.open("images/tela_jogo/singlecardslot.png")
        slot_carta_jogador1 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador1 = ImageTk.PhotoImage(slot_carta_jogador1)

        carta_jogador1 = Image.open("images/tela_jogo/cartas/a_copas.png")
        carta_jogador1 = carta_jogador1.resize((82, 115), Image.LANCZOS)
        self.carta_jogador1 = ImageTk.PhotoImage(carta_jogador1)

        slot_carta_jogador2 = Image.open("images/tela_jogo/singlecardslot.png")
        slot_carta_jogador2 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador2 = ImageTk.PhotoImage(slot_carta_jogador2)

        carta_jogador2 = Image.open("images/tela_jogo/cartas/dama_copas.png")
        carta_jogador2 = carta_jogador2.resize((82, 115), Image.LANCZOS)
        self.carta_jogador2 = ImageTk.PhotoImage(carta_jogador2)

        slot_carta_jogador3 = Image.open("images/tela_jogo/singlecardslot.png")
        slot_carta_jogador3 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador3 = ImageTk.PhotoImage(slot_carta_jogador3)

        slot_carta_jogador4 = Image.open("images/tela_jogo/singlecardslot.png")
        slot_carta_jogador4 = slot_carta_jogador1.resize((96, 125), Image.LANCZOS)
        self.slot_carta_jogador4 = ImageTk.PhotoImage(slot_carta_jogador4)

        self.canvas.create_image(600, 465, anchor="center", image=self.slot_carta_jogador1)
        self.canvas.create_image(597, 465, anchor="center", image=self.carta_jogador1)

        self.canvas.create_image(750, 350, anchor="center", image=self.slot_carta_jogador2)
        self.canvas.create_image(747, 350, anchor="center", image=self.carta_jogador2)

        self.canvas.create_image(600, 275, anchor="center", image=self.slot_carta_jogador3)

        self.canvas.create_image(450, 350, anchor="center", image=self.slot_carta_jogador4)
    
    def criar_botoes_menu(self):
        imagem_botao_naipe_rodada = Image.open("images/tela_jogo/botoes/botao_copas.png")
        imagem_botao_naipe_rodada = imagem_botao_naipe_rodada.resize((50, 50), Image.LANCZOS)
        self.img_botao_naipe_rodada = ImageTk.PhotoImage(imagem_botao_naipe_rodada)

        self.botao_naipe_rodada = self.canvas.create_image(980, 40, image=self.img_botao_naipe_rodada)

        imagem_botao_pontuacao = Image.open("images/tela_jogo/botoes/botao_pontuacao.png")
        imagem_botao_pontuacao = imagem_botao_pontuacao.resize((50, 50), Image.LANCZOS)
        self.img_botao_pontuacao = ImageTk.PhotoImage(imagem_botao_pontuacao)

        self.botao_pontuacao = self.canvas.create_image(1040, 40, image=self.img_botao_pontuacao)

        self.canvas.tag_bind(self.botao_pontuacao, "<Button-1>", self.click_botao_pontuacao)
        self.canvas.tag_bind(self.botao_pontuacao, "<Enter>", self.on_hover_botao_pontuacao)
        self.canvas.tag_bind(self.botao_pontuacao, "<Leave>", self.saida_botao_pontuacao)

        imagem_botao_regras = Image.open("images/tela_jogo/botoes/botao_regras.png")
        imagem_botao_regras = imagem_botao_regras.resize((50, 50), Image.LANCZOS)
        self.img_botao_regras = ImageTk.PhotoImage(imagem_botao_regras)

        self.botao_regras = self.canvas.create_image(1100, 40, image=self.img_botao_regras)

        self.canvas.tag_bind(self.botao_regras, "<Button-1>", self.click_botao_regras)
        self.canvas.tag_bind(self.botao_regras, "<Enter>", self.on_hover_botao_regras)
        self.canvas.tag_bind(self.botao_regras, "<Leave>", self.saida_botao_regras)

        imagem_botao_fechar = Image.open("images/tela_jogo/botoes/botao_fechar.png")
        imagem_botao_fechar = imagem_botao_fechar.resize((50, 50), Image.LANCZOS)
        self.img_botao_fechar = ImageTk.PhotoImage(imagem_botao_fechar)

        self.botao_fechar = self.canvas.create_image(1160, 40, image=self.img_botao_fechar)

        self.canvas.tag_bind(self.botao_fechar, "<Button-1>", self.click_botao_fechar)
        self.canvas.tag_bind(self.botao_fechar, "<Enter>", self.on_hover_botao_fechar)
        self.canvas.tag_bind(self.botao_fechar, "<Leave>", self.saida_botao_fechar)

    def on_hover_botao_pontuacao(self, event):
        imagem_botao_pontuacao = Image.open("images/tela_jogo/botoes/botao_pontuacao.png")
        imagem_botao_pontuacao = imagem_botao_pontuacao.resize((60, 60), Image.LANCZOS)
        self.img_botao_pontuacao_grande = ImageTk.PhotoImage(imagem_botao_pontuacao)

        self.canvas.itemconfig(self.botao_pontuacao, image=self.img_botao_pontuacao_grande)

    def saida_botao_pontuacao(self, event):
        self.canvas.itemconfig(self.botao_pontuacao, image=self.img_botao_pontuacao)

    def click_botao_pontuacao(self, event):
        pass

    def on_hover_botao_regras(self, event):
        imagem_botao_regras = Image.open("images/tela_jogo/botoes/botao_regras.png")
        imagem_botao_regras = imagem_botao_regras.resize((60, 60), Image.LANCZOS)
        self.img_botao_regras_grande = ImageTk.PhotoImage(imagem_botao_regras)

        self.canvas.itemconfig(self.botao_regras, image=self.img_botao_regras_grande)

    def saida_botao_regras(self, event):
        self.canvas.itemconfig(self.botao_regras, image=self.img_botao_regras)

    def click_botao_regras(self, event):
        pass

    def on_hover_botao_fechar(self, event):
        imagem_botao_fechar = Image.open("images/tela_jogo/botoes/botao_fechar.png")
        imagem_botao_fechar = imagem_botao_fechar.resize((60, 60), Image.LANCZOS)
        self.img_botao_fechar_grande = ImageTk.PhotoImage(imagem_botao_fechar)

        self.canvas.itemconfig(self.botao_fechar, image=self.img_botao_fechar_grande)

    def saida_botao_fechar(self, event):
        self.canvas.itemconfig(self.botao_fechar, image=self.img_botao_fechar)

    def click_botao_fechar(self, event):
        pass

    def mostrar_aviso(self, event):
        messagebox.showwarning("Aviso", "Você clicou em uma carta!")