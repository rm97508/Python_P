# Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla.
char = "*"
print (char*20)
print('Tabuada com WHILE')
print (char*20) 

num = 1
while (num <= 20):
    i = 1
    while(i < 11):
        r = num * i
        print(f'{num} X {i} = {r}')
        i = i + 1 
    print (char*20)     
    input ('Aperte enter para continuar: ')
    num = num + 1
    print (char*20) 
if (num >= 20):
    print("Fim!")


