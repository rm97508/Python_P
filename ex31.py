#31. Criar uma rotina de entrada que aceite somente um valor positivo.
num = float(input("Digite um valor positivo: "))

while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter: "))

print ("Número válido!")