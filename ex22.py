#22. Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o cálculo da respectiva área. 
# Enviar mensagem de erro se o usuário escolher uma opção inexistente. 
# Encerrar o programa somente quando selecionada a opção de finalização. 
# (Fazer esse exercício utilizando If..Else e/ou Case) 1 – Triângulo 2 – Quadrado 3 – Retângulo 4 – Círculo 5 – Fim de processo

op =  int (input("Selecione (1) para Triângulo, (2) para Quadrado, (3) para Retângulo ou (4) para o Círculo ou (5) para o Fim de processo: "))

if (op == 1):
    base = float (input ("digite o valor da base: "))
    alt = float (input ("digite o valor da altura:"))
    area = (base*alt)/2
    print(f"A area do tiangulo é {area:.2f}")

elif(op == 2): 
    aresta = float(input ("Digite o valor da aresta: "))
    area = aresta*aresta
    print (f"o valor da area do quadrado corresponde a {area:.2f}")

elif (op == 3): 
    base = float (input ("digite o valor da base: "))
    alt = float (input ("digite o valor da altura:"))
 
    area = base*alt 

    print(f"A area do retangulo é {area:.2f}")

elif (op == 4):
    raio = float (input ("digite o valor do raio do circulo: "))
    area = (3.141592653589793*raio**2)
    print(f"A area do circulo é {area:.2f}")

elif (op == 5):
    print ('Fim!')

else: 
    print('opção inexistente')