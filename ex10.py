#10. Entrar com dois valores quaisquer. Exibir o maior deles, se existir, 
# caso contrário, enviar mensagem avisando que os números são idênticos.
v1= float(input('Digite o primeiro:'))
v2= float (input ('Digite o segundo valor:'))
 
if v1==v2: 
    print('Os valores são iguais!')
elif v1>v2:
   print("O Primeiro valor é maior")
else:
    print("O Segundo valor é maior")