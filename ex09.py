#9. Entrar via teclado, com dois valores distintos. Exibir o menor deles. 
v1= float(input('Digite o primeiro:'))
v2= float (input ('Digite o segundo valor:'))
 
if v1==v2: 
    print('Os valores são iguais!')
elif v1<v2:
   print("O Primeiro valor é menor")
else:
    print("O Segundo valor é menor")