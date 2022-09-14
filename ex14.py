#14. Entrar com o peso e a altura de uma determinada pessoa.
#  Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².
peso = float (input ('Por favor, digite o valor do seu peso (massa): '))
alt = float (input('Agora digite o valor da sua altura: '))

c= peso/alt**2

if (c < 19):
    print(f'Seu Indice de Massa Corporal é: {c:.2f} e você está abaixo do peso!')
elif (c > 24):
    print(f'Cuidado, Indice de Massa Corporal é: {c:.2f} e você está acima do peso!')   
else: 
    print(f'Seu Indice de Massa Corporal é: {c:.2f} e você está com no peso ideal!')
     