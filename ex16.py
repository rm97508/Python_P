#16. Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. 
# Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos. c² = a² + b²
h = float(input('Digite o valor da hipotenusa: '))
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))

h2 = h**2
c3 = c1**2+c2**2

if (c3 == h2):
    print ('Esse é um triangulo retangulo!')
else:
    print (' Ops! Não é um triangulo retangulo!')


