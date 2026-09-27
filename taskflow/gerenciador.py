"""Módulo do Gerenciador de Tarefas do Taskflow.

Implementação do Desafio 01: A Base do TASKFLOW (Classes e Dicionários).
"""

from typing import Any, Dict, List


class GerenciadorTarefas:
    """Gerenciador de tarefas em memória.

    Atributos:
        tarefas (List[Dict[str, Any]]): Lista contendo os dicionários de cada tarefa.
    """

    def __init__(self) -> None:
        """Inicializa o gerenciador com uma lista vazia e contador de ID."""
        self.tarefas: List[Dict[str, Any]] = []
        self._contador_id: int = 0

    def adicionar_tarefa(self, titulo: str, descricao: str = "") -> Dict[str, Any]:
        """Adiciona uma nova tarefa à lista do gerenciador.

        Args:
            titulo (str): O título resumido da tarefa. Não pode ser vazio.
            descricao (str, optional): Detalhes da tarefa. Padrão é "".

        Returns:
            Dict[str, Any]: O dicionário representando a tarefa recém-criada.

        Raises:
            ValueError: Se o título for vazio, composto apenas por espaços ou não for string.
            TypeError: Se a descrição não for uma string.
        """
        if not isinstance(titulo, str):
            raise TypeError("O título da tarefa deve ser uma string.")

        titulo_limpo = titulo.strip()
        if not titulo_limpo:
            raise ValueError("O título da tarefa não pode ser vazio.")

        if not isinstance(descricao, str):
            raise TypeError("A descrição da tarefa deve ser uma string.")

        self._contador_id += 1
        nova_tarefa: Dict[str, Any] = {
            "id": self._contador_id,
            "titulo": titulo_limpo,
            "descricao": descricao.strip(),
            "status": "Pendente",
        }

        self.tarefas.append(nova_tarefa)
        return nova_tarefa

    def listar_pendentes(self) -> List[Dict[str, Any]]:
        """Filtra e retorna apenas as tarefas com status 'Pendente'.

        Returns:
            List[Dict[str, Any]]: Lista de dicionários das tarefas pendentes.
        """
        return [tarefa for tarefa in self.tarefas if tarefa.get("status") == "Pendente"]

    def listar_todas(self) -> List[Dict[str, Any]]:
        """Retorna uma cópia da lista com todas as tarefas cadastradas.

        Returns:
            List[Dict[str, Any]]: Lista de todas as tarefas.
        """
        return list(self.tarefas)
