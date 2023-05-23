'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

soma = valor1 + valor2
print(f'o valor da soma entre {valor1} e {valor2} é: {soma}')
'''

#Treinando IS validações
'''
v = input('digite o valor: ')
print(v.isnumeric()) #validação se é um numero
print(v.isspace()) #Validação se só tem espaços
print(v.isalpha()) #Validação se é letra
print(v.isupper()) #Validação se todas as letras estão em caixa alta
print(v.islower()) #Validação se todas as letras estão em Minuscula
print(v.isalnum()) #Validação se contém letras e numeros
'''

#Desafio 03 Qual o tipo Primitivo ?

T = input('Digite o valor ')

print(type(T))
A = (T.isnumeric())
B = (T.isalpha())

if A == True:
    print('contém numero')
else:
    print('não contém numero')

if B == True:
    print('contém Letra')
else:
    print('não contém Letra')
