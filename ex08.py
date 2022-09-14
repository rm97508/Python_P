#8. Entrar via teclado, com dois valores distintos. Exibir o maior deles.
v1= float(input('Digite o primeiro:'))
v2= float (input ('Digite o segundo valor:'))
 
if v1==v2: 
    print('Os valores são iguais!')
elif v1>v2:
   print("O Primeiro valor é maior")
else:
    print("O Segundo valor é maior")