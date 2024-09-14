from tkinter import *
from PIL import Image, ImageTk

class TelaJogo:

    def __init__(self):
        self.janela_principal = Tk()
        self.configurar_janela()
        self.janela_principal.mainloop()

    def configurar_janela(self):
        self.janela_principal.title("Sueca")
        self.janela_principal.geometry("1080x600")
        self.janela_principal.resizable(False, False)

        altura = 600
        largura = 1080
        x = (self.janela_principal.winfo_screenwidth()//2)-(largura//2)
        y = (self.janela_principal.winfo_screenheight()//2)-(altura//2)
        self.janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")

        label_fundo = Label(self.janela_principal, image = self.imagem_fundo) 
        label_fundo.place(x=0, y=0, relheight=1, relwidth=1) 