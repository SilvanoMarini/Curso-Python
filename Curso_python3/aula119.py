import os

# tarefas = []
# tarefas_desfeitas = []

# while True:
#     try:
#         print('Escolha um comando ou digite uma tarefa para adicionar a lista')
#         print('(Listar)  (Desfazer)  (Refazer) (Sair)')

#         resposta = str(input('Digite: ')).lower()
#         print()

#         if resposta == 'listar':
#             if len(tarefas) >= 1:
#                 print(*tarefas, sep='\n')
#                 print()
#             else:
#                 print('Sem Tarefas')
#                 print()

#         elif resposta == 'desfazer':
#             if len(tarefas) >= 1:
#                 tarefas_desfeitas.append(tarefas.pop())
#                 print()
#             else:
#                 print('Sem Tarefas para Desfazer')
#                 print()

#         elif resposta == 'refazer':
#             if len(tarefas_desfeitas) >= 1:
#                 tarefas.append(tarefas_desfeitas.pop())
#                 print()
#             else:
#                 print('Sem Tarefas Para Refazer')
#                 print()

#         elif resposta == 'clear':
#             os.system('clear')

#         elif resposta == 'sair':
#             break

#         else:
#             tarefas.append(resposta)
#     except Exception:
#         print('ERRO! Tente novamente')
#         continue
