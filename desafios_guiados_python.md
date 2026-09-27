# Mentoria Python: Do Iniciante ao Avançado

Bem-vindo ao seu ambiente de treinamento. Como seu dev sênior, meu objetivo não é te dar as respostas prontas, mas sim te guiar para que você desenvolva a lógica de programação, boas práticas e arquitetura de software por conta própria.

## 🛠️ Regras de Versionamento (GitHub)

Para mantermos o padrão de mercado e a organização do seu repositório, **nenhum código deste treinamento deve ser commitado diretamente na branch `main`**. 

Siga este fluxo rigorosamente:
1. Abra o seu terminal no repositório do projeto.
2. Certifique-se de estar com a `main` atualizada: `git pull origin main`
3. Crie e mude para a nova branch obrigatória:
   `git checkout -b Desafio-guiado-Python`
4. Todo o código dos desafios deverá ser comitado nesta branch.

## 🧠 Metodologia de Trabalho

1. **Apresentação:** Eu apresento o escopo do desafio, os requisitos e algumas dicas iniciais.
2. **Desenvolvimento:** Você escreve o código na sua branch e envia os trechos aqui.
3. **Code Review:** Eu analiso seu código. Se houver erros ou pontos de melhoria de performance/segurança, vou apontar onde estão e fazer perguntas para que você descubra como resolver.
4. **Aprovação:** Assim que o código estiver sólido, validamos o desafio e avançamos para o próximo nível.

---

## 🚀 Desafio 01: A Base do TASKFLOW (Classes e Dicionários)

Como você já tem uma boa base em estruturas de dados e classes, vamos aplicar isso no escopo do seu projeto real.

**Objetivo:** Criar a estrutura inicial de um gerenciador de tarefas em memória.

### Requisitos do Sistema:
1. Crie uma classe chamada `GerenciadorTarefas`.
2. A classe deve ter um método construtor (`__init__`) que inicialize uma lista vazia para armazenar as tarefas.
3. Crie um método `adicionar_tarefa(titulo, descricao)`. Cada tarefa deve ser um **dicionário** contendo:
   - `id` (pode ser um número incremental ou um UUID)
   - `titulo`
   - `descricao`
   - `status` (deve começar por padrão como "Pendente")
4. Crie um método `listar_pendentes()` que retorne ou imprima apenas as tarefas cujo status seja "Pendente".

### 💡 Dicas do Sênior:
* Pense bem em como você vai gerar e controlar o `id` de cada tarefa para que não existam duas tarefas com o mesmo ID. Um atributo de classe ou o uso da biblioteca `uuid` podem ser boas opções.
* Lembre-se de tratar a entrada de dados. E se o usuário tentar adicionar uma tarefa sem título? 
* Tente manter o código limpo, documentado (use docstrings) e legível.

**Status atual:** Aguardando a primeira versão do seu código.