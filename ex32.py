#32. Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.
a = int (input('Digite o menor valor: '))
b = int (input('Digite o maior valor: '))

while (b<a):
    print('O valor digitado é menor que o primeiro! Tente novamente!')
    b = int (input('Digite o maior valor: '))

print ('Valores válidos!')