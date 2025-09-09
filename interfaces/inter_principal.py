import tkinter as tk

from historico import historico
from interfaces.inter_historico import Inter_Historico

from var import cor_fundo, cor_texto, fonte

class Inter_Principal():
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("450x550")
        self.master.configure(bg=cor_fundo)
        self.historico = historico  # salvar histórico durante o uso
        
        
        # adaptando tamanho, layout responsivo
        for linha in range(5):  # == range(0, 5)
            self.master.grid_rowconfigure(linha, weight=1)
        
        for coluna in range(4): # 0 1 2 3 
            self.master.grid_columnconfigure(coluna, weight=1)
        
        
        # row/column: onde começa
        # comlumnspan: quantos colunas pode ocupar, ideal para elementos maiores
        # sticky: onde vai se prender quando aumentar resolução, nsew se prende a tudo
        frame_visor = tk.Frame(master, bg=cor_fundo)
        frame_visor.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            sticky="nsew",
            pady=5
        )
        frame_visor.grid_columnconfigure(0, weight=1)
        
        self.visor = tk.Entry(
            frame_visor,
            font=fonte,
            textvariable='0',
            width= 30,
            borderwidth=2,
            relief="solid",
            justify="right"
        )
        # ipady: espaçamento interno, aumenta elemento
        self.visor.grid(
            row=0, 
            column=0, 
            sticky="nsew", 
            padx=10, 
            pady=0, 
            ipady=5
        )
        
        
        frame_botoes_calculadora = tk.Frame(master, bg=cor_fundo)
        frame_botoes_calculadora.grid(row=1, column=0)
        
        botoes = [
            ['C', 'DEL', '+/-', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '=']
        ]
        
        # enumerate foi usado pois ele já vem como se fosse um rank
        # ex: 1 C, 2 DEL, ...
        
        for linha_index, linha in enumerate(botoes):
            for coluna_index, texto in enumerate(linha):
                botao = tk.Button(
                    frame_botoes_calculadora, 
                    font=fonte,
                    text=texto, 
                    width=5, 
                    height=2,
                    command=lambda t=texto: self.clickar(t)
                )
                botao.grid(
                    row=linha_index, 
                    column=coluna_index, 
                    padx=5, 
                    pady=5
                )
    
        frame_historico = tk.Frame(self.master, bg=cor_fundo)
        frame_historico.grid(row=0, column=4)
        
        self.botao_historico = tk.Button(
            frame_historico,
            bg=cor_fundo,
            fg=cor_texto,
            font=fonte,
            text="Histórico",
            width=8,
            height=2,
            command=self.janela_historico
        )
        self.botao_historico.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=5,
            ipady=5
        )
        
    # eval: transforma string em expressão Python e calcula
    # visor.delete(inicio, fim)
    # visor.insert(posição, texto) 
    
    def clickar(self, valor):
        if valor == "=":
            
            try:
                expressao = self.visor.get()
                resultado = str(eval(expressao))
                self.historico.append(f"{expressao} = {resultado}")
                self.visor.delete(0, tk.END)
                self.visor.insert(0, resultado)
                
            except Exception as e:
                self.visor.delete(0, tk.END)
                self.visor.insert(0, "Erro")
                
        elif valor == "C":
            self.visor.delete(0, tk.END)
            
        elif valor == "DEL":
            expressao = self.visor.get()
            self.visor.delete(0, tk.END)
            self.visor.insert(0, expressao[:-1])  # apaga último caractere
            
        elif valor == "+/-":
            expressao = self.visor.get()
            
            if expressao:
                try:
                    numero = float(expressao)
                    numero *= -1
                    self.visor.delete(0, tk.END)
                    
                    if numero.is_integer:
                        self.visor.insert(0, str(int(numero)))
                    else:
                        self.visor.insert(0, str(numero))
                
                except ValueError():
                    pass
            
        else:
            self.visor.insert(tk.END, valor)
            
    
    # def teclado(self, event):
    #     tecla = event.char
        
    #     if tecla.isdigit() or tecla in "+-*/().%":
    #         self.clickar(tecla)        
    
            
    def janela_historico(self):
        Inter_Historico()