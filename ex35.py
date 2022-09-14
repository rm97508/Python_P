#35. Entrar via teclado com um valor qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. Após a digitação, 
# exibir a tabuada do valor solicitado, no intervalo de um a dez
char = "*"
print (char*20)
print('Tabuada com WHILE')
print (char*20) 

num = int(input("Digite um numero para obter a tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))
 
i = 1
 
while(i < 11):
    r = num * i
    print(f'{num} X {i} = {r}')
    print (char*20)
    i = i + 1