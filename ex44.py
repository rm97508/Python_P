#44. Entrar via teclado com dez valores positivos. Consistir a digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir:
#a) O maior valor;
#b) A soma dos valores;
#c) A média aritmética dos valores;
qtd = 10 
soma = 0
for i in range (1, qtd+1, 1):
    n = int (input('digite um número:'))
    
    while ( n < 0): 
        print("Número invalido! Tente novamente")
        n = int (input('Digite um número inteiro positivo: '))

    if (i == 1):
        maior = n 
    elif (n > maior):
        maior = n 
    soma = soma + n

m = soma / qtd
print (f'O maior valor: {maior}')
print (f'A soma dos valores: {soma}')
print (f'A média aritmética dos valores: {m:.2f}')