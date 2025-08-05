import os  # Importa o módulo 'os' para usar comandos do sistema operacional (aqui usado para limpar a tela)

# Lista que guarda as tarefas atuais
tarefas = []

# Lista que guarda as tarefas que foram desfeitas, para possibilitar o refazer
tarefas_desfeitas = []

# Loop infinito para o programa ficar rodando até o usuário digitar "sair"
while True:
    try:
        # Mensagem para o usuário com opções de comandos e a opção de digitar uma tarefa para adicionar
        print('Escolha um comando ou digite uma tarefa para adicionar a lista')
        print('(Listar)  (Desfazer)  (Refazer) (Sair)')

        # Recebe a resposta do usuário, converte para minúsculas para facilitar comparação
        resposta = str(input('Digite: ')).lower()
        print()

        # Se o usuário quiser listar as tarefas
        if resposta == 'listar':
            # Verifica se há tarefas para mostrar
            if len(tarefas) >= 1:
                # Imprime todas as tarefas, cada uma em uma linha
                print(*tarefas, sep='\n')
                print()
            else:
                # Caso não tenha tarefas na lista
                print('Sem Tarefas')
                print()

        # Se o usuário quiser desfazer a última tarefa adicionada
        elif resposta == 'desfazer':
            # Verifica se há tarefas para desfazer
            if len(tarefas) >= 1:
                # Remove a última tarefa da lista 'tarefas' e adiciona na lista 'tarefas_desfeitas'
                tarefas_desfeitas.append(tarefas.pop())
                print()
            else:
                # Caso não tenha tarefas para desfazer
                print('Sem Tarefas para Desfazer')
                print()

        # Se o usuário quiser refazer uma tarefa desfeita
        elif resposta == 'refazer':
            # Verifica se há tarefas desfeitas para refazer
            if len(tarefas_desfeitas) >= 1:
                # Remove a última tarefa da lista 'tarefas_desfeitas' e adiciona de volta na lista 'tarefas'
                tarefas.append(tarefas_desfeitas.pop())
                print()
            else:
                # Caso não tenha tarefas para refazer
                print('Sem Tarefas Para Refazer')
                print()

        # Se o usuário digitar 'clear' para limpar a tela (funciona em sistemas Unix)
        elif resposta == 'clear':
            os.system('clear')

        # Se o usuário quiser sair do programa
        elif resposta == 'sair':
            break

        # Caso o usuário tenha digitado qualquer outra coisa, adiciona isso como uma tarefa na lista
        else:
            tarefas.append(resposta)

    # Se acontecer qualquer erro no bloco acima, exibe uma mensagem e continua o loop
    except Exception:
        print('ERRO! Tente novamente')
        continue
