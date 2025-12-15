import os
import json

def adicionar_tarefa(tarefa, lista):
    if not tarefa:
        print('Nenhum tarefa a ser adicionado')
        print()
        return
    lista.append(tarefa)
    print(f'{tarefa=} adicionada com sucesso.')
    print()
    return lista


def desfazer_tarefa(desfazer, lista):
    if not lista:
        print('Nenhuma tarefa para ser desfeita')
        print()
        return
    desfazer.append(lista.pop())
    return desfazer


def refazer_tarefa(refazer, lista):
    if not lista:
        print('Nenhuma tarefa para ser refeita')
        print()
        return
    refazer.append(lista.pop())
    return refazer


def listar_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para ser listada')
        print()
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def clear():
    os.system('cls')


def salvar(tarefas, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        return json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    


def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho)
    return dados
