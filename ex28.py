#28. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem crescente.
a = int (input ('Digite o primeiro valor: '))
b = int (input ('Digite o segundo valor: '))
c = int (input ('Digite o terceiro valor: '))

Lista = [a, b, c]
print('Essa é a lista original:', Lista)
print('Essa é a lista em ordem crescente:',sorted(Lista))


