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
        self.historico = historico 
        
        
        for linha in range(5):  
            self.master.grid_rowconfigure(linha, weight=1)
        
        for coluna in range(4):  
            self.master.grid_columnconfigure(coluna, weight=1)
        
        
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
            self.visor.insert(0, expressao[:-1]) 
            
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
            
    def janela_historico(self):
        Inter_Historico()