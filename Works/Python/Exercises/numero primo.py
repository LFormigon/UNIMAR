N = int(input('Informe um número positivo para\nverificar se é primo : '))
primo = True
if N <= 1:
    primo = False
else:
    for d in range(2,N//2+1):
        if N % d == 0:
            primo = False
            break
if primo:
    print(f'{N} é um número primo')
else:
    print(f'{N} não é um número primo')