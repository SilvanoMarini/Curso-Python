from aula119modulo import *

CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_desfeitas = []

while True:

    print('Escolha um comando ou digite uma tarefa para adicionar a lista')
    print('(Listar)  (Desfazer)  (Refazer) (Sair)')

    resposta = str(input('Digite: ')).capitalize()
    print()

    comandos = {
        'Listar': lambda: listar_tarefas(tarefas),
        'Desfazer': lambda: desfazer_tarefa(tarefas_desfeitas, tarefas),
        'Refazer': lambda: refazer_tarefa(tarefas, tarefas_desfeitas),
        'Clear': lambda: clear(),
        'Adicionar': lambda: adicionar_tarefa(resposta, tarefas)
    }

    comando = comandos.get(resposta) if comandos.get(resposta) is not None else \
        comandos['Adicionar']
    comando()
    print()
    salvar(tarefas, CAMINHO_ARQUIVO)

    # if resposta == 'listar':
    #     listar_tarefas(tarefas)

    # elif resposta == 'desfazer':
    #     desfazer_tarefa(tarefas_desfeitas, tarefas)
    #     print()


    # elif resposta == 'refazer':
    #     refazer_lista(tarefas, tarefas_desfeitas)
    #     print()

    # elif resposta == 'sair':
    #     break

    # else:
    #     resposta = resposta.capitalize()
    #     adicionar_tarefa(resposta, tarefas)

