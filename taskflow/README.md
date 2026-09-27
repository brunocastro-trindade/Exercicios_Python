# 📌 Taskflow — Gerenciador de Tarefas

Implementação do **Desafio 01: A Base do TASKFLOW (Classes e Dicionários)** do programa de mentoria Python.

---

## 🎯 Objetivo

Construir a base em memória de um sistema de gerenciamento de tarefas utilizando Programação Orientada a Objetos (POO), dicionários e boas práticas de desenvolvimento (validações, tipagem estática e testes unitários).

---

## 🗂️ Estrutura de Arquivos

```text
taskflow/
├── __init__.py           # Exportação do pacote e classe GerenciadorTarefas
├── gerenciador.py        # Classe GerenciadorTarefas com a lógica central
├── main.py               # Script de demonstração e menu CLI interativo
├── test_gerenciador.py   # Testes unitários com unittest (10 cenários cobertos)
└── README.md             # Esta documentação
```

---

## ⚙️ Requisitos Atendidos

| Requisito | Status | Implementação |
|---|---|---|
| **1. Classe `GerenciadorTarefas`** | Concluído | Localizada em [`gerenciador.py`](gerenciador.py) |
| **2. Construtor com lista vazia** | Concluído | `self.tarefas = []` e contador interno de identificadores `self._contador_id = 0` |
| **3. Método `adicionar_tarefa(titulo, descricao)`** | Concluído | Retorna e armazena dicionário com `id`, `titulo`, `descricao` e `status="Pendente"`. Inclui validação contra títulos vazios ou apenas espaços em branco |
| **4. Método `listar_pendentes()`** | Concluído | Filtra por `status == "Pendente"` sem mutar a lista original |

---

## 🚀 Como Executar

### 1. Executar Demonstração

```bash
python3 -m taskflow.main
```

### 2. Executar Menu Interativo

```bash
python3 taskflow/main.py interactive
```

### 3. Executar Testes Unitários

```bash
python3 -m unittest taskflow/test_gerenciador.py
```
