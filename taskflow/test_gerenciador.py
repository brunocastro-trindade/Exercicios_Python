"""Testes unitários para o módulo GerenciadorTarefas."""

import unittest
from taskflow.gerenciador import GerenciadorTarefas


class TestGerenciadorTarefas(unittest.TestCase):
    """Conjunto de testes para a classe GerenciadorTarefas."""

    def setUp(self) -> None:
        """Instancia um novo gerenciador antes de cada teste."""
        self.gerenciador = GerenciadorTarefas()

    def test_inicializacao(self) -> None:
        """Verifica se o gerenciador inicializa com lista de tarefas vazia."""
        self.assertEqual(self.gerenciador.tarefas, [])
        self.assertEqual(len(self.gerenciador.tarefas), 0)

    def test_adicionar_tarefa_sucesso(self) -> None:
        """Verifica a adição correta de uma tarefa."""
        tarefa = self.gerenciador.adicionar_tarefa(
            titulo="Estudar Python",
            descricao="Revisar POO e métodos mágicos",
        )

        self.assertEqual(tarefa["id"], 1)
        self.assertEqual(tarefa["titulo"], "Estudar Python")
        self.assertEqual(tarefa["descricao"], "Revisar POO e métodos mágicos")
        self.assertEqual(tarefa["status"], "Pendente")
        self.assertEqual(len(self.gerenciador.tarefas), 1)

    def test_adicionar_tarefas_incremento_id(self) -> None:
        """Verifica se cada tarefa recebe um ID único e incremental."""
        t1 = self.gerenciador.adicionar_tarefa("Tarefa 1")
        t2 = self.gerenciador.adicionar_tarefa("Tarefa 2")
        t3 = self.gerenciador.adicionar_tarefa("Tarefa 3")

        self.assertEqual(t1["id"], 1)
        self.assertEqual(t2["id"], 2)
        self.assertEqual(t3["id"], 3)
        self.assertEqual(len(self.gerenciador.tarefas), 3)

    def test_adicionar_tarefa_sem_descricao(self) -> None:
        """Verifica se a descrição é opcional e assume valor padrão vazio."""
        tarefa = self.gerenciador.adicionar_tarefa("Comprar café")
        self.assertEqual(tarefa["descricao"], "")

    def test_adicionar_tarefa_espacos_em_branco(self) -> None:
        """Verifica se espaços antes e depois do título e descrição são removidos."""
        tarefa = self.gerenciador.adicionar_tarefa("   Limpar mesa   ", "   gaveta 1   ")
        self.assertEqual(tarefa["titulo"], "Limpar mesa")
        self.assertEqual(tarefa["descricao"], "gaveta 1")

    def test_adicionar_tarefa_titulo_vazio(self) -> None:
        """Verifica se tentar adicionar tarefa com título vazio lança ValueError."""
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa("")

        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa("   ")

    def test_adicionar_tarefa_tipo_invalido(self) -> None:
        """Verifica se tipos inválidos para título ou descrição lançam TypeError."""
        with self.assertRaises(TypeError):
            self.gerenciador.adicionar_tarefa(123)  # type: ignore

        with self.assertRaises(TypeError):
            self.gerenciador.adicionar_tarefa("Título válido", descricao=456)  # type: ignore

    def test_listar_pendentes_vazio(self) -> None:
        """Verifica listagem de pendentes quando não há tarefas cadastradas."""
        self.assertEqual(self.gerenciador.listar_pendentes(), [])

    def test_listar_pendentes_com_tarefas(self) -> None:
        """Verifica retorno apenas de tarefas cujo status seja 'Pendente'."""
        self.gerenciador.adicionar_tarefa("Tarefa 1")
        self.gerenciador.adicionar_tarefa("Tarefa 2")
        self.gerenciador.adicionar_tarefa("Tarefa 3")

        # Modifica manualmente o status de uma tarefa para simular conclusão
        self.gerenciador.tarefas[1]["status"] = "Concluída"

        pendentes = self.gerenciador.listar_pendentes()
        self.assertEqual(len(pendentes), 2)
        self.assertEqual(pendentes[0]["titulo"], "Tarefa 1")
        self.assertEqual(pendentes[1]["titulo"], "Tarefa 3")
        for tarefa in pendentes:
            self.assertEqual(tarefa["status"], "Pendente")

    def test_listar_todas(self) -> None:
        """Verifica a recuperação de todas as tarefas cadastradas."""
        self.gerenciador.adicionar_tarefa("Tarefa A")
        self.gerenciador.adicionar_tarefa("Tarefa B")
        todas = self.gerenciador.listar_todas()
        self.assertEqual(len(todas), 2)


if __name__ == "__main__":
    unittest.main()
