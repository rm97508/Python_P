#7. Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao pagamento da 
# somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

D1 = float(input('Digite o primeiro valor: '))
D2 = float(input('Digite o segundo valor : '))
D3 = float(input('Digite o terceiro valor : '))
D4 = float(input('Digite o quarto valor : '))
D5 = float (input('Digite o quinto valor: '))
 
S = D1+D2+D3+D4+D5

print (f'O valor total é R${S:.2f}')

P = float(input('Digite o primeiro valor do pagamento: '))

t = P-S

print(f"O valor do troco é R${t:.2f}")
