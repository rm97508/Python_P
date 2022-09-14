v1= float(input('Digite o primeiro:'))
v2= float (input ('Digite o segundo valor:'))
v3= float(input ('Digite o terceiro valor:'))
 
if v1+v2>v3 and v3+v2>v1 and v1+v3>v2: 
    print('Os valores indicados formam um triangulo')
    if v1==v2==v3: 
        print('Esse triangulo é eqüilátero')
    elif v1!=v3!=v2:
        print("Esse triangulo é escaleno ")
    else:
        print("Esse triangulo é isósceles")
else:
    print("Esse não é um triangulo")