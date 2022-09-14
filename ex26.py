#26. Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.
a = int (input ('Digite um valor: ')) 
if (a < 0):
    t = a*3
    print (f'Esse número é negativo, portanto, seu triplo é {t}.')
else: 
    t = a*2
    print (f'Esse número é positivo, portanto, seu dobro é {t}.')