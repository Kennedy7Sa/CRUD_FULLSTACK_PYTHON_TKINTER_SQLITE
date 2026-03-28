import tkinter as tk
from tkinter import messagebox
import backEnd as bk

id_selecionado = None


# ---------------- FUNÇÕES ---------------- #

def limparCampos():
    nome_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)


def carregarTarefas():
    lista_tarefas.delete(0, tk.END)

    tarefas = bk.Tarefa.listar()

    for t in tarefas:
        lista_tarefas.insert(
            tk.END,
            f"{t['id']} - {t['nome']} ({t['status']})"
        )


def selecionarTarefa(event):
    global id_selecionado

    selecionado = lista_tarefas.get(tk.ACTIVE)

    if selecionado:
        partes = selecionado.split(" - ")

        id_selecionado = int(partes[0])

        nome_status = partes[1]

        nome = nome_status.split(" (")[0]
        status = nome_status.split("(")[1].replace(")", "")

        limparCampos()

        nome_entry.insert(0, nome)
        status_entry.insert(0, status)


def salvar():
    global id_selecionado

    nome = nome_entry.get()
    status = status_entry.get()

    if not nome or not status:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    tarefa = bk.Tarefa({
        'id': id_selecionado,
        'nome': nome,
        'status': status
    })

    tarefa.salvar()

    messagebox.showinfo("Sucesso", "Tarefa salva!")

    id_selecionado = None
    limparCampos()
    carregarTarefas()


def deletar():
    global id_selecionado

    selecionado = lista_tarefas.get(tk.ACTIVE)

    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione uma tarefa!")
        return

    id_tarefa = int(selecionado.split(" - ")[0])

    tarefa = bk.Tarefa({'id': id_tarefa})
    tarefa.excluir()

    id_selecionado = None
    limparCampos()
    carregarTarefas()


# ---------------- INTERFACE ---------------- #

janela = tk.Tk()
janela.title("To Do List - FullStack")

# Nome
tk.Label(janela, text="Nome da tarefa").grid(row=0, column=0, padx=10, pady=5)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

# Status
tk.Label(janela, text="Status da tarefa").grid(row=1, column=0, padx=10, pady=5)
status_entry = tk.Entry(janela)
status_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão salvar
tk.Button(janela, text="Salvar", command=salvar)\
    .grid(row=2, columnspan=2, pady=5)

# Lista
lista_tarefas = tk.Listbox(janela, width=40)
lista_tarefas.grid(row=3, columnspan=2, padx=10, pady=10)

lista_tarefas.bind("<<ListboxSelect>>", selecionarTarefa)

# Botão deletar
tk.Button(janela, text="Deletar", command=deletar)\
    .grid(row=4, columnspan=2, pady=5)

carregarTarefas()

janela.mainloop()