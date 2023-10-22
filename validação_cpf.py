#validação de CPF
cpf_cliente = "" #Aqui vai o cpf do cliente 
nove_digitos = cpf_cliente[:9] #contagem até nono digito
if len(cpf_cliente) != 11 : print("Cpf não atingiu quantidade de números.") #checagem tamanho 
#calculando o primeiro digito
contagem_regressiva_1 = 10 #contagem regressiva do 10
resultado_1 = 0  
for numero_1 in nove_digitos:
    resultado_1 += int(numero_1) * contagem_regressiva_1
    contagem_regressiva_1 -= 1
digito_1 = (resultado_1*10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
#calculando o segundo digito
dez_digito = nove_digitos + str(digito_1)
contagem_regressiva_2 = 11
resultado_2 = 0
for numero_2 in dez_digito:
    resultado_2 += int(numero_2) * contagem_regressiva_2
    contagem_regressiva_2 -= 1 
digito_2 = resultado_2*10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 
cpf_formatado = f"{nove_digitos}{digito_1}{digito_2}"
if cpf_formatado == cpf_cliente:
    print(f"{cpf_formatado} é valido")
else: 
    print(f"{cpf_formatado} é invalido")
