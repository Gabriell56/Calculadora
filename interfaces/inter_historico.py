import tkinter as tk
from historico import historico

from var import cor_fundo, cor_texto, fonte

class Inter_Historico():
    def __init__(self):
        self.janela = tk.Toplevel()
        self.janela.title("Histórico")
        self.janela.geometry("200x100")
        self.janela.configure(bg=cor_fundo)
        
        self.historico_label = tk.Button(
            self.janela,
            bg=cor_fundo,
            fg=cor_texto,
            font=fonte,
            text="\n".join(historico[-3:])
        )
        # fill: qual direção widget vai se expandir
        # expand: se widget pode disputar espaço extra, caso TRUE, aumenta e compete com aqueles que são TRUE também
        self.historico_label.pack(fill="both", expand=True)
        
        self.janela.bind("<FocusIn>", lambda e: self.atualizar())
        
    def atualizar(self):
        # config == configure
        self.historico_label.config(text="\n".join(historico[-3:]))