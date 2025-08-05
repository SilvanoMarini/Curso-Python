import re
import random

# Gera uma lista com 9 números aleatórios entre 0 e 9 (os primeiros 9 dígitos do CPF)
cpf_aleatorio = [random.randint(0, 9) for numero in range(9)]

# Concatena os números da lista em uma string (ex: ['1', '2', '3'] → "123")
cpf_digitado = ''.join(map(str, cpf_aleatorio))

# Remove qualquer caractere que não seja número (nesse caso não há, mas é uma segurança extra)
cpf_formatado = re.sub(r'[^0-9]', '', cpf_digitado)

# Pega apenas os 9 primeiros dígitos do CPF (sem os dígitos verificadores ainda)
cpf = cpf_formatado[:9]

# Calcula a soma dos produtos dos dígitos pelos multiplicadores de 10 até 2
soma_do_cpf1 = sum(int(digito) * multiplicador \
                   for multiplicador, digito in zip(range(10, 1, -1), cpf))

# Calcula o primeiro dígito verificador
primeiro_digito = (soma_do_cpf1 * 10) % 11
# Se o resultado for maior que 9, o dígito verificador é 0
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Adiciona o primeiro dígito ao CPF para calcular o segundo dígito verificador
cpf_segundo_d = cpf + str(primeiro_digito)

# Calcula a soma dos produtos dos dígitos (agora com 10 dígitos) pelos multiplicadores de 11 até 2
soma_do_cpf2 = sum(int(digito) * multiplicador \
                   for multiplicador, digito in zip(range(11, 1, -1), cpf_segundo_d))

# Calcula o segundo dígito verificador
segundo_digito = (soma_do_cpf2 * 10) % 11
# Se o resultado for maior que 9, o dígito verificador é 0
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# Junta os 9 dígitos + primeiro dígito verificador + segundo dígito verificador
cpf = cpf + str(primeiro_digito) + str(segundo_digito)

# Exibe o CPF completo gerado (válido)
print(cpf)

