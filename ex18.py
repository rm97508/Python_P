#18. A partir dos valores da aceleração (a em m/s2), 
# da velocidade inicial (v0 em m/s) e do tempo de percurso (t em s). Calcular e exibir a 
# velocidade final de automóvel em km/h. Exibir mensagem de acordo com a tabela: Fórmula para o cálculo da velocidade em m/s: V = v0 + a. t
a = float(input('Digite o valor da aceleração(m/s²): '))
t = float(input('Digite o valor do tempo(s): '))
v = float(input('Digite o valor da velocidade(m/s): '))

vf = v+a*t
c = vf*3.6

if ( c <= 40 ): 
    print(f'Veículo está a {c:.2f}, muito lento!')
elif ( 40 < c and c <= 60): 
    print(f'Veículo está a {c:.2f}, velocidade permitida!')
elif (60 < c and c <= 80): 
    print(f'Veículo está a {c:.2f}, velocidade de cruzeiro!')
elif (80 < c and c <= 120): 
    print(f'Veículo está a {c:.2f}, veículo está rápido!')
else: 
    print(f'Veículo está a {c:.2f}, muito rápido!')