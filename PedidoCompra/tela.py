import tkinter as tk 


janela = tk.Tk() 
janela.title("Solicitação de compra") 
janela.geometry("500x700")
label = tk.Label(janela,text="Solicitação de compras")

label.pack(pady=20)
janela.mainloop()


