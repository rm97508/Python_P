#42. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, 
# mas menor que cinqüenta. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente.
#1/2 2/3 3/4 4/5 

n = float(input('Digite um número inteiro menor que 50: '))
while (n > 49 or n < 0): 
    print("Número invalido! Tente novamente")
    n = float (input('Digite um número inteiro menor que 50: '))

a = 1 
b = 2
count = 2
total = a/b

while (count <= n):
    r = a/b
    print(f'{a}\ {b} ={r:.2f}')
    a = b
    b = b+1
    r = a/b
    total = r + total
    count +=1
print (f'{a}\ {b}={r:.2f}')

print (f"A soma da sequência é: {total:.2f}")

