#30. Elabore um algoritmo que calcule o que deve ser pago por um produto, 
# considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual a  condição de pagamento escolhida e 
# efetuar o cálculo adequado e exibir o valor a ser pago no final. Código Condição de pagamento
#1 	À vista em dinheiro ou cheque, recebe 10% de desconto
#2 	À vista no cartão de crédito, recebe 15% de desconto
#3 	Em duas vezes, preço normal de etiqueta sem juros
#4 	Em quatro vezes, preço normal de etiqueta mais juros de 10%
a = float (input ('Seja bem-vindo! Insira o valor da compra: '))
char = '_'
print(char * 80)
print(f'{char * 5}Condição de pagamento{char * 54}')
print(f'{char * 5} 1. À vista em dinheiro ou cheque, recebe 10% de desconto {char * 17}')
print(f'{char * 5} 2. À vista no cartão de crédito, recebe 15% de desconto{char * 19}')
print(f'{char * 5} 3. Em duas vezes, preço normal de etiqueta sem juros {char * 21}')
print(f'{char * 5} 4. Em quatro vezes, preço normal de etiqueta mais juros de 10% {char *11}')
print(char * 80)
op = int(input('Digite a operaçao desejada 1,2,3,4: '))
print(char * 70)

if (op == 1):
    r = a*0.9
    print(f"O preço a ser pago é: R${r:.2f}")

elif(op == 2): 
    r = a*0.85
    print(f"O preço a ser pago é: R${r:.2f}")

elif (op == 3): 
    r = a/2
    print(f"O preço a ser pago será de 2x de R${r:.2f}")

elif (op == 4):
    r = (a*1.1)/4
    print(f"O preço a ser pago será de 4x de R${r:.2f}")


else: 
    print('Ops! opção inexistente, tente novamente!')

print(char * 70)