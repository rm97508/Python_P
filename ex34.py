#34. Exibir a tabuada do número cinco no intervalo de um a dez.
char = "*"
print (char*20)
print('Tabuada com WHILE')
print (char*20)

num = int(input("Digite o numero 5 para obter a tabuada: "))
print (char*40)

while(num != 5):
    print("Não pode numero diferente de 5!")
    num = int(input("Digite o numero 5 para obter a tabuada: "))
 
x = 1

while(x < 11):
    r = num * x
    print(f'{num} X {x} = {r}')
    x = x + 1


     
    
    