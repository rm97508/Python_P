#38. Exibir a soma dos números inteiros positivos do intervalo de um a cem.

total = 0 

for i in range (1, 101, 1):
    total = total + i
print (f"A soma de 1 a 100 é: {total}")
