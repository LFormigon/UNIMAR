numero = int(input('Informe o Primeiro Valor: '))
if numero <= 999:
    centena = int(numero / 100)
    dezena = int((numero - centena*100)/10)
    unidade = int(numero - ((centena * 100) + (dezena * 10)))

    print(f'O Valor da Centena {centena}')
    print(f'O Valor da Centena {dezena}')
    print(f'O Valor da Centena {unidade}')

    if centena < dezena < unidade:
        print('É Ascendente.')
    else:
        print('Não é Ascendente')