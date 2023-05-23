from random import randint

valorAp = float(input('Valor da aposta >> R$ '))
na = int(input('Número entre 1 e 36 >> '))
if na < 1 or na > 36:
    print('Número inválido!!')
else:
    ns = randint(1,36)
    print(f'Número sorteado >> {ns}')
    if na == ns:
        print(f'Acertou o número, ganhou R$ {valorAp*5:.2f}')
    elif (na-1) // 12 == (ns-1) // 12:
        print(f'Acertou a dúzia, ganhou R$ {valorAp*3:.2f}')
    elif na%2 == ns%2:
        print(f'Acertou a paridade, ganhou R$ {valorAp*2:.2f}')
    else:
        print('Perdeu o valor apostado')