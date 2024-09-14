from tkinter import *
from PIL import Image, ImageTk

class TelaJogo:

    def __init__(self):
        self.janela_principal = Tk()
        self.configurar_janela()
        self.janela_principal.mainloop()

    def configurar_janela(self):
        self.janela_principal.title("Sueca")
        self.janela_principal.geometry("1200x700")
        self.janela_principal.resizable(False, False)

        largura = 1200
        altura = 700
        x = (self.janela_principal.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.janela_principal.winfo_screenheight() // 2) - (altura // 2) - 10
        self.janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")

        self.configurar_background()
        self.criar_slot_cartas()
        self.criar_area_jogador_1()
        self.criar_area_jogador_2()
        self.criar_area_jogador_3()
        self.criar_area_jogador_4()
        
    def configurar_background(self):
        largura = 1200
        altura = 700

        imagem_fundo = Image.open("images/tela_jogo/background.png")
        imagem_fundo = imagem_fundo.resize((largura, altura), Image.LANCZOS)
        
        self.imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

        self.canvas = Canvas(self.janela_principal, width=largura, height=altura)
        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo_tk)
    
    def criar_slot_cartas(self):
        imagem_slot_cartas = Image.open("images/tela_jogo/cardsslot.png")
        imagem_slot_cartas = imagem_slot_cartas.resize((1100, 153), Image.LANCZOS)
        self.imagem_slot_cartas = ImageTk.PhotoImage(imagem_slot_cartas)

        self.canvas.create_image(600, 600, anchor="center", image=self.imagem_slot_cartas)
    
    def criar_area_jogador_1(self):
        imagem_carta1 = Image.open("images/tela_jogo/cartas/a_paus.png")
        imagem_carta1 = imagem_carta1.resize((82, 115), Image.LANCZOS)
        self.imagem_carta1 = ImageTk.PhotoImage(imagem_carta1)

        imagem_carta2 = Image.open("images/tela_jogo/cartas/dama_copas.png")
        imagem_carta2 = imagem_carta2.resize((82, 115), Image.LANCZOS)
        self.imagem_carta2 = ImageTk.PhotoImage(imagem_carta2)

        nome_jogador1 = Image.open("images/tela_jogo/playertag.png")
        nome_jogador1 = nome_jogador1.resize((180, 30), Image.LANCZOS)
        self.nome_jogador1 = ImageTk.PhotoImage(nome_jogador1)

        self.canvas.create_image(180, 605, anchor="center", image=self.imagem_carta1)
        self.canvas.create_image(271, 605, anchor="center", image=self.imagem_carta2)
        self.canvas.create_image(135, 500, anchor="nw", image=self.nome_jogador1)
    
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

        
