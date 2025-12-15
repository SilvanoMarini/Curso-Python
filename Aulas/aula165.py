from datetime import datetime
from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y'

data_inicial = datetime.strptime('20/12/2020', fmt)

data_final = data_inicial + relativedelta(years=5)

delta = relativedelta(data_final, data_inicial)

meses_totais = delta.years * 12 + delta.months

valor_emprestimo = 1000000 

valor_parcela = valor_emprestimo / meses_totais

datas_de_vencimento = [
    (data_inicial + relativedelta(months=1)) + relativedelta(months=meses)
    for meses in range(meses_totais)
    ]


print(f'Data inicial do empréstimo {data_inicial.strftime(fmt)}. Primeira parcela em 30 dias')
print(f'Data final do empréstimo {data_final.strftime(fmt)}')

cont = 1
for data in datas_de_vencimento:
    if cont == 60:
        valor_parcela -= 0.2
    print(f'{cont:2}° parcela de R${valor_parcela:.2f} vence em {data.strftime(fmt)}')
    cont += 1

