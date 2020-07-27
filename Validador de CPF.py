v1 = []
dados1 = 0
cont1 = 10
digito1 = 0
v2 = []
dados2 = 0
cont2 = 11
digito2 = 0
cpf = str(input('Digite o CPF'))
# conferindo primeiro digito
for numero in range(0, 9):
    dados1 = int(cpf[numero]) * cont1
    v1.append(dados1)
    cont1 = cont1 - 1
print(v1)
if 11 - (sum(v1) % 11) > 9:
    digito1 = 0
    print(f'If digito1 {digito1}')
else:
    digito1 = 11 - (sum(v1) % 11)
    print(f'else digito1 {digito1}')
# conferindo segundo digito
for numero in range(0, 9):
    dados2 = int(cpf[numero]) * cont2
    v2.append(dados2)
    cont2 = cont2 - 1
v2.append(digito1 * cont2)
print(v2)
if 11 - (sum(v2) % 11) > 9:
    digito2 = 0
    print(f'If digito2 {digito2}')
else:
    digito2 = 11 - (sum(v2) % 11)
    print(f'else digito2 {digito2}')
# conferindo novo cpf gerado com o original
novocpf = cpf[0:9] + str(digito1) + str(digito2)
if novocpf == cpf:
    print('Valido')
else:
    print('Invalido')