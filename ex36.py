#36. Entrar via teclado com um valor (X) qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. Solicitar o intervalo que o programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor (B), deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o segundo. Após a validação dos dados, exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.
char = "*"
print (char*20)
print('Tabuada com WHILE')
print (char*20) 

num = int(input("Digite um numero para obter a tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))

print ('Agora digite o intervalo que deseja ser calculado (Ex: 1 ao 10):  ')

a = int (input('Digite o menor valor: '))
b = int (input('Digite o maior valor: '))

while (b < a):
    print('O valor digitado é menor que o primeiro! Tente novamente!')
    b = int (input('Digite o maior valor: '))

 
while(b >= a):
    r = num * b
    print(f'{num} X {b} = {r}')
    print (char*20)
    b = b-1