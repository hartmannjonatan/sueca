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
        y = (self.janela_principal.winfo_screenheight() // 2) - (altura // 2)
        self.janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")

        self.configurar_background()
        self.criar_slot_cartas()

        
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
        imagem_slot_cartas = imagem_slot_cartas.resize((1100, 200), Image.LANCZOS)
        self.imagem_slot_cartas = ImageTk.PhotoImage(imagem_slot_cartas)

        self.canvas.create_image(600, 600, anchor="center", image=self.imagem_slot_cartas)
        
