#38. Exibir a soma dos números inteiros positivos do intervalo de um a cem. 
#for i in range (1, 101, 1):
   # total = total + i
#print (f"A soma de 1 a 100 é: {total}")
i = 0
total = 0
while (i <= 99):
    i = i + 1
    total = i + total
print (f"A soma de 1 a 100 é: {total}")