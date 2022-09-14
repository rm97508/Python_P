#6. Entrar via teclado com o valor da cotação do dólar e uma 
# certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$).
c = float (input("digite o valor da cotação do dia: "))
d = float (input('digite o valor do dollar que deseja converter: '))
r = c*d
print(f'O valor em reais corresponde a: R$ {r:.2f}')