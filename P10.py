import tkinter as tk
from tkinter import messagebox, filedialog
import csv

materias = []
notas = []

def adicionar_dado():
    materia = entrada_materia.get()
    try:
        nota = float(entrada_nota.get())
        if materia and 0 <= nota <= 10:
            materias.append(materia)
            notas.append(nota)
            lista_dados.insert(tk.END, f"{materia}: {nota}")
            entrada_materia.delete(0, tk.END)
            entrada_nota.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Nota deve estar entre 0 e 10.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para a nota.")

def limpar_dados():
    materias.clear()
    notas.clear()
    lista_dados.delete(0, tk.END)
    messagebox.showinfo("Limpo", "Dados removidos com sucesso.")

def exportar_csv():
    if materias and notas:
        caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if caminho:
            with open(caminho, "w", newline='') as f:
                escritor = csv.writer(f)
                escritor.writerow(["Matéria", "Nota"])
                for m, n in zip(materias, notas):
                    escritor.writerow([m, n])
            messagebox.showinfo("Exportado", f"Dados salvos em {caminho}")
    else:
        messagebox.showwarning("Aviso", "Nenhum dado para exportar.")

# Interface
janela = tk.Tk()
janela.title("Registro de Notas")
janela.geometry("400x450")

# Frame de entrada
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Matéria:").grid(row=0, column=0)
entrada_materia = tk.Entry(frame_entrada)
entrada_materia.grid(row=0, column=1)

tk.Label(frame_entrada, text="Nota (0-10):").grid(row=1, column=0)
entrada_nota = tk.Entry(frame_entrada)
entrada_nota.grid(row=1, column=1)

tk.Button(janela, text="Adicionar", command=adicionar_dado, width=20).pack(pady=5)

# Lista dos dados adicionados
tk.Label(janela, text="Dados inseridos:").pack()
lista_dados = tk.Listbox(janela, width=40, height=10)
lista_dados.pack()

# Botões de ação
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Limpar Dados", command=limpar_dados, width=18).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Exportar para CSV", command=exportar_csv, width=18).grid(row=0, column=1, padx=5)

janela.mainloop()
