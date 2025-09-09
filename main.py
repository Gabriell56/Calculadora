import tkinter as tk
from interfaces.inter_principal import Inter_Principal

# root: container base, todos elementos visuais -> moldura
# app: objeto da classe, organizar widgets -> controles

if __name__ == "__main__":
    root = tk.Tk()
    app = Inter_Principal(root)
    root.mainloop()