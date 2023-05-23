N1 = int(input('Digite o primeiro valor: '))
N2 = int(input('Digite o Segundor valor: '))

soma = N1 + N2
mulpi = N1 * N2
divi = N1 / N2
diviint = N1 // N2
esponeciacao =  N1 ** N2

print(f'A soma é {soma}, o produto é {mulpi} e a divisão é {divi:.3f}',end=' ') #ja que o valor é quebrado, limitado a apenas três casas o "End" e para deixar os resultados na mesma linha, junto com o print de baixo 
print(f'Divisão inteira {diviint} e potência {esponeciacao}')                      #Caso queira quebrar é "\n"



