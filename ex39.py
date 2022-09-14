#39. Exibir os trinta primeiros valores da série de Fibonacci. A série: 1, 1, 2, 3, 5, 8, ...
print ('*'*25)
print('Série de Fibonacci')
print ('*'*25) 
n = 30 
t1 = 1 
t2 = 1
print(f'{t1}->{t2}', end='')
cont = 3
while (cont <= n):
    t3 = t1 + t2
    print (f'->{t3}', end='')
    t1 = t2 
    t2 = t3
    cont +=1
print('_Fim!')
   
    
    
    