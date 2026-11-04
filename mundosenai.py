import tkinter as tk
from tkinter import messagebox


estoque = {}

def adicionar_item():
    nome_item = entry_nome.get().strip()
    qtd_texto = entry_qtd.get().strip()
    
    
    if not nome_item:
        messagebox.showwarning("Aviso", "Por favor, digite o nome do item!")
        return

   
    try:
        quantidade = int(qtd_texto)
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "A quantidade deve ser um número inteiro maior que 0!")
        return

    
    if nome_item in estoque:
        estoque[nome_item] += quantidade
    else:
        estoque[nome_item] = quantity = quantidade

   
    atualizar_lista_visual()
    
    
    entry_nome.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    entry_nome.focus()

def atualizar_lista_visual():
    
    lista_itens.delete(1.0, tk.END)
    
    
    for item, qtd in estoque.items():
        lista_itens.insert(tk.END, f"• {item}: {qtd} unidades\n")


janela = tk.Tk()
janela.title("Gerenciador de Estoque")
janela.geometry("400x450")
janela.configure(padx=20, pady=20)


lbl_nome = tk.Label(janela, text="Nome do Item:", font=("Arial", 11, "bold"))
lbl_nome.pack(anchor="w", pady=(0, 2))

entry_nome = tk.Entry(janela, font=("Arial", 11))
entry_nome.pack(fill="x", pady=(0, 10))

lbl_qtd = tk.Label(janela, text="Quantidade:", font=("Arial", 11, "bold"))
lbl_qtd.pack(anchor="w", pady=(0, 2))

entry_qtd = tk.Entry(janela, font=("Arial", 11))
entry_qtd.pack(fill="x", pady=(0, 15))


btn_adicionar = tk.Button(janela, text="Adicionar ao Estoque", font=("Arial", 11, "bold"), 
                           bg="#4CAF50", fg="white", command=adicionar_item, cursor="hand2")
btn_adicionar.pack(fill="x", pady=(0, 20))

lbl_resultado = tk.Label(janela, text="Itens Cadastrados:", font=("Arial", 11, "bold"))
lbl_resultado.pack(anchor="w", pady=(0, 5))


frame_lista = tk.Frame(janela)
frame_lista.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

lista_itens = tk.Text(frame_lista, font=("Arial", 11), yscrollcommand=scrollbar.set, height=10)
lista_itens.pack(side="left", fill="both", expand=True)
scrollbar.config(command=lista_itens.yview)


janela.mainloop()