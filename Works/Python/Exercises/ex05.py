# Exercicio Mostrando o seu tipo Primitivo e todas as funções possiveis delas.

V = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(V)}')
print(f'Só tem espaços? {(V.isspace())}')
print(f'É numerico ? {(V.isnumeric())}')
print(f'É alfabético ? {(V.isalpha())}')
print(f'É alfanumerico? {V.isalpha()}')
print(f'Está em maiscula {V.isupper()}')
print(f'Está em minuscula {V.islower()}')
print(f'Está capitalizada {V.isalnum()}') #Tem letras Maiscula e Mínuscula

