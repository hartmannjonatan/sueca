from abc import ABC, abstractmethod
from tkinter import *
import tkinter as tk


class TelaSecundaria(ABC):

    def __init__(self):
        self._tela = tk.Toplevel()
        self._canvas = Canvas(self.tela)
        
        self.tela.withdraw()

        self.tela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    @abstractmethod
    def configurar_tela(self):
        pass

    def abrir_tela(self):
        self.tela.deiconify()
    
    def fechar_tela(self):
        self.tela.withdraw()

    @property
    def tela(self):
        return self._tela
    
    @property
    def canvas(self):
        return self._canvas
    