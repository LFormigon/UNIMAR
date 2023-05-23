idade = int(input('Informe a idade: '))
if 0 <= idade <= 10:
    print('Criança')
else:
    if 11 <= idade <= 17:
        print('Adolescente')
    else:
        if 18 <= idade <= 59:
            print('Adulto')
        else:
            print('Terceira Idade')