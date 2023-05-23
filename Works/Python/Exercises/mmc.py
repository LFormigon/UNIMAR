sexo = input('Sexo [F/M]: ').upper()[0]
if sexo != 'F' and sexo != 'M':
    print('Sexo Inválido!!')
else:
    altura = float(input('Altura: '))
    if sexo == 'F':
        pIdeal = 62.1*altura - 44.7
    else:
        pIdeal = 74.2*altura - 58
    print(f'Peso Ideal: {pIdeal:.2f}')