#27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.
a = float (input ('Digite um valor: '))

if (a % 2 == 0):
    r = a + 5
    print (f'A  variável é par e somada a 5 teremos o resultado {r}')
else: 
    r = a + 8
    print (f'A  variável é impar e somada a 8 teremos o resultado {r}')
