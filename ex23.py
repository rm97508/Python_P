#23. Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
char = ' ♥'
print (char*69)
a = float (input ('Digite o primeiro valor: '))
print (char*69)
b = float (input ('Digite o segundo valor: '))
print (char*69)
c = float (input ('Digite o terceiro valor: '))
print (char*69)
r = a+b
if (a+b<c):
    print (f'A soma de {a} + {b} é igual a {r}, portanto, menor que o terceiro {c}.')
elif (a+b==c):
    print(f'A soma de {a} + {b} é igual a {r}, portanto, igual ao valor {c}.')
else:
    print (f'A soma de {a} + {b} é igual a {r}, portanto, maior que o valor {c}.')