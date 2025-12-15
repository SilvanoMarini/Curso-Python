import re



cpf_digitado = input('CPF: ')

# Remove qualquer caractere que não seja número (só por segurança, mesmo que não tenha símbolos)
cpf_formatado = re.sub(r'[^0-9]', '', cpf_digitado)

# Pega apenas os 9 primeiros dígitos do CPF
cpf = cpf_formatado[:9]

# Calcula a soma dos produtos dos 9 dígitos pelos multiplicadores de 10 até 2
soma_do_cpf1 = sum(int(digito) * multiplicador \
                   for multiplicador, digito in zip(range(10, 1, -1), cpf))

# Calcula o primeiro dígito verificador
primeiro_digito = (soma_do_cpf1 * 10) % 11
# Se o resultado for maior que 9, o dígito verificador é 0
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Junta os 9 dígitos com o primeiro dígito verificador
cpf_segundo_d = cpf + str(primeiro_digito)

# Calcula a soma dos produtos dos 10 dígitos (já com o primeiro dígito) pelos multiplicadores de 11 até 2
soma_do_cpf2 = sum(int(digito) * multiplicador \
                   for multiplicador, digito in zip(range(11, 1, -1), cpf_segundo_d))

# Calcula o segundo dígito verificador
segundo_digito = (soma_do_cpf2 * 10) % 11
# Se o resultado for maior que 9, o dígito verificador é 0
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# Monta o CPF completo com os dois dígitos verificadores
cpf = cpf + str(primeiro_digito) + str(segundo_digito)

# Verifica se o CPF digitado (os 9 dígitos aleatórios) + os dois verificadores calculados
# corresponde ao CPF formatado original (sem símbolos)
# Se for igual, o CPF é válido; caso contrário, é inválido
print(f'O CPF {cpf_digitado} é válido') if cpf == cpf_formatado \
    else print(f'O CPF {cpf_digitado} é invalido')

