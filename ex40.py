#40. Exibir os vinte primeiros valores da série de Bergamaschi. A série: 1, 1, 1, 3, 5, 9, 17, ...
print ('*'*25)
print('Série de Bergamaschi')
print ('*'*25) 
n = 20 
t1 = 1 
t2 = 1
t3 = 1
print(f'{t1}_{t2}', end='')
cont = 3
while (cont <= n):
    t4 = t1 + t2 + t3
    print (f'_{t4}', end='')
    t1 = t2 
    t2 = t3
    t3 = t4
    cont +=1
print('_Fim!')
