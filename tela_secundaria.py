from abc import ABC, abstractmethod
from tkinter import *
import tkinter as tk

class TelaSecundaria(ABC):

    def __init__(self):
        self.tela = tk.Toplevel()
        self.canvas = Canvas(self.tela)
        
        self.tela.withdraw()
        self.configurar_tela()

        self.tela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    @abstractmethod
    def configurar_tela(self):
        pass

    def abrir_tela(self):
        self.tela.deiconify()
    
    def fechar_janela(self):
        self.tela.withdraw()
    