#29. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.
a = int (input ('Digite o primeiro valor: '))
b = int (input ('Digite o segundo valor: '))
c = int (input ('Digite o terceiro valor: '))

Lista = [a, b, c]
Lista.sort(reverse = True)

print(Lista)
