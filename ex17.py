#17. Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a digitação, 
# exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

peso = float (input ('Por favor, digite o valor do seu peso (massa): '))
alt = float (input('Agora digite o valor da sua altura: '))
sex = input('Agora digite F para feminino ou M para masculino: ').upper()

imc= peso/alt**2

if (sex == 'M'):
    if (imc < 20):
        print(f'Seu Indice de Massa Corporal é: {imc:.2f} e você está abaixo do peso!')
    elif (imc >= 25):
        print(f'Cuidado, Indice de Massa Corporal é: {imc:.2f} e você está acima do peso!')   
    else: 
        print(f'Seu Indice de Massa Corporal é: {imc:.2f} e você está com no peso ideal!')       
else: 

    if (imc < 19):
        print(f'Seu Indice de Massa Corporal é: {imc:.2f} e você está abaixo do peso!')
    elif (imc >= 24):
        print(f'Cuidado, Indice de Massa Corporal é: {imc:.2f} e você está acima do peso!')   
    else: 
        print(f'Seu Indice de Massa Corporal é: {imc:.2f} e você está com no peso ideal!')
