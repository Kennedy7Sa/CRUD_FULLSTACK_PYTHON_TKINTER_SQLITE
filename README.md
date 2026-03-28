# 📝 To Do List FullStack com Tkinter + SQLite

Aplicação desktop desenvolvida em Python com interface gráfica utilizando Tkinter e persistência de dados com SQLite.
O projeto implementa um CRUD completo de tarefas seguindo boas práticas de organização, orientação a objetos e separação entre front-end e back-end.

---

## 🚀 Demonstração

Funcionalidades principais da aplicação:

* ✅ Criar tarefas
* 📋 Listar tarefas
* ✏️ Atualizar tarefas
* ❌ Excluir tarefas

---

## 🧠 Arquitetura do Projeto

O sistema foi estruturado em camadas, separando responsabilidades:

```
📁 projeto
 ┣ 📄 front.py        # Interface gráfica (Tkinter)
 ┣ 📄 backEnd.py      # Regras de negócio + acesso ao banco
 ┗ 📄 bd_tarefas.db   # Banco de dados SQLite
```

### 🔹 Front-end (Tkinter)

Responsável pela interface com o usuário:

* Inputs de nome e status
* Listagem de tarefas
* Interações (seleção, edição, exclusão)

### 🔹 Back-end (POO)

Responsável pelas regras de negócio:

* Classe `Tarefa`
* Métodos de CRUD
* Conexão com banco SQLite

---

## 🛠️ Tecnologias Utilizadas

* 🐍 Python 3
* 🖼️ Tkinter (Interface gráfica)
* 🗄️ SQLite (Banco de dados)
* 🧱 Programação Orientada a Objetos (POO)

---

## ⚙️ Funcionalidades Detalhadas

### ➕ Criar Tarefa

Permite adicionar uma nova tarefa com nome e status.

### 📋 Listar Tarefas

Exibe todas as tarefas cadastradas em uma lista dinâmica.

### ✏️ Atualizar Tarefa

Ao selecionar uma tarefa:

* Os dados são carregados nos campos
* O usuário pode editar e salvar novamente

### ❌ Excluir Tarefa

Remove a tarefa selecionada do banco de dados.

---

## 🔄 Fluxo da Aplicação

1. Usuário insere dados nos campos
2. Clica em **Salvar**
3. O sistema decide:

   * Se existe `id` → Atualiza
   * Se não existe → Cria nova tarefa
4. A lista é atualizada automaticamente

---

## 🧩 Modelo de Dados

Tabela `TAREFAS`:

| Campo  | Tipo    | Descrição        |
| ------ | ------- | ---------------- |
| id     | INTEGER | Chave primária   |
| nome   | TEXT    | Nome da tarefa   |
| status | TEXT    | Status da tarefa |

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
```

### 2. Acesse a pasta

```bash
cd seu-repo
```

### 3. Execute a aplicação

```bash
python front.py
```

---

## 💡 Melhorias Futuras

* 🔍 Filtro de tarefas por status
* 🎨 Interface mais moderna (ttk / customtkinter)
* 📅 Adição de data de criação
* 🧾 Exportação de tarefas (CSV/Excel)
* 🔐 Autenticação de usuário

---

## 🧑‍💻 Autor

Desenvolvido por **Kennedy Arruda**

* 💼 Desenvolvedor FullStack
* 📊 Foco em Análise de Dados
* ⚙️ Experiência com Python, Node.js e SQL

---

## 📌 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

* Praticar conceitos de CRUD
* Aplicar Programação Orientada a Objetos
* Trabalhar com banco de dados relacional
* Construir interfaces desktop com Python
* Demonstrar habilidades práticas para o mercado de tecnologia

---

## ⭐ Considerações Finais

Este projeto representa a construção de uma aplicação completa, desde a interface até a persistência de dados, seguindo boas práticas de desenvolvimento e organização de código.

Ideal como base para evolução para sistemas mais robustos e aplicações profissionais.

---
