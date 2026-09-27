"""Interface de linha de comando e demonstração do Taskflow."""

import sys
from taskflow.gerenciador import GerenciadorTarefas


def formatar_tarefa(tarefa: dict) -> str:
    """Retorna uma representação formatada da tarefa para o terminal."""
    status_emoji = "⏳" if tarefa["status"] == "Pendente" else "✅"
    descricao = tarefa["descricao"] if tarefa["descricao"] else "(sem descrição)"
    return (
        f"  [ID #{tarefa['id']:03d}] {tarefa['titulo']}\n"
        f"    Descrição: {descricao}\n"
        f"    Status:    {status_emoji} {tarefa['status']}"
    )


def exibir_lista(tarefas: list[dict], titulo_cabecalho: str) -> None:
    """Imprime uma lista de tarefas com cabeçalho formatado."""
    print("\n" + "=" * 50)
    print(f"  {titulo_cabecalho} ({len(tarefas)} tarefa(s))")
    print("=" * 50)
    if not tarefas:
        print("  Nenhuma tarefa encontrada.")
    else:
        for t in tarefas:
            print(formatar_tarefa(t))
            print("-" * 50)


def executar_demonstracao() -> None:
    """Executa um fluxo demonstrativo automatizado dos requisitos do Desafio 01."""
    print("\n" + "#" * 50)
    print("  🚀 DEMONSTRAÇÃO TASKFLOW - DESAFIO 01")
    print("#" * 50)

    gerenciador = GerenciadorTarefas()

    print("\n1. Adicionando tarefas iniciais...")
    t1 = gerenciador.adicionar_tarefa(
        titulo="Configurar ambiente de desenvolvimento",
        descricao="Instalar dependências e validar versão do Python",
    )
    print(f"   Criada: #{t1['id']} - {t1['titulo']}")

    t2 = gerenciador.adicionar_tarefa(
        titulo="Criar branch de desenvolvimento",
        descricao="Garantir que as alterações fiquem em Desafio-guiado-Python",
    )
    print(f"   Criada: #{t2['id']} - {t2['titulo']}")

    t3 = gerenciador.adicionar_tarefa(
        titulo="Implementar testes unitários",
        descricao="Cobrir inicialização, inserção e listagem de pendentes",
    )
    print(f"   Criada: #{t3['id']} - {t3['titulo']}")

    print("\n2. Tentando adicionar tarefa com título em branco (validação):")
    try:
        gerenciador.adicionar_tarefa("   ")
    except ValueError as erro:
        print(f"   [Validação capturada com sucesso] Erro: {erro}")

    print("\n3. Listando tarefas pendentes:")
    pendentes = gerenciador.listar_pendentes()
    exibir_lista(pendentes, "TAREFAS PENDENTES")

    print("\n✔ Demonstração concluída com sucesso!")


def menu_interativo() -> None:
    """Menu interativo para uso manual do gerenciador."""
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n" + "=" * 40)
        print("         TASKFLOW - MENU PRINCIPAL")
        print("=" * 40)
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Tarefas Pendentes")
        print("3. Listar Todas as Tarefas")
        print("4. Executar Demonstração Automática")
        print("0. Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título da tarefa: ").strip()
            descricao = input("Descrição (opcional): ").strip()
            try:
                tarefa = gerenciador.adicionar_tarefa(titulo, descricao)
                print(f"\n[SUCESSO] Tarefa #{tarefa['id']} cadastrada como '{tarefa['status']}'.")
            except (ValueError, TypeError) as e:
                print(f"\n[ERRO] Não foi possível adicionar: {e}")

        elif opcao == "2":
            pendentes = gerenciador.listar_pendentes()
            exibir_lista(pendentes, "TAREFAS PENDENTES")

        elif opcao == "3":
            todas = gerenciador.listar_todas()
            exibir_lista(todas, "TODAS AS TAREFAS")

        elif opcao == "4":
            executar_demonstracao()

        elif opcao == "0":
            print("\nEncerrando o Taskflow. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        executar_demonstracao()
    else:
        # Se for executado em ambiente interativo ou se passado argumento
        if len(sys.argv) > 1 and sys.argv[1] == "interactive":
            menu_interativo()
        else:
            executar_demonstracao()
