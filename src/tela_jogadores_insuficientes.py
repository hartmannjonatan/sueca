from tela_secundaria import TelaSecundaria
from PIL import Image, ImageTk

from images import IMAGES_DIR


class TelaJogadoresInsuficientes(TelaSecundaria):

    def __init__(self):
        super().__init__()
        self.configurar_tela
    
    def configurar_tela(self):
        self.tela.title("Aviso")
        self.tela.resizable(False, False)

        self.canvas.config(width=400, height=200)

        x = (self.tela.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.tela.winfo_screenheight() // 2) - (200 // 2) - 10
        self.tela.geometry(f"400x200+{x}+{y}")

        imagem_fundo = Image.open(IMAGES_DIR / "tela_jogadores_insuficientes/imagem_fundo.png")
        imagem_fundo = imagem_fundo.resize((400, 200))
        self.imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
        
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagem_fundo)