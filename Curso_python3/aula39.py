indici =   0
nome = input('Nome: ')
novo_nome = ''
while indici < len(nome):

    novo_nome = novo_nome + ('*' + nome[indici]) 
    indici += 1
print(novo_nome+'*')