#45. Entrar via teclado com “N” valores quaisquer. O valor “N” (que representa a quantidade de números) será digitado, deverá ser positivo, 
# mas menor que vinte. Caso a quantidade não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. 
# Após a digitação dos “N” valores, exibir:
#a) O maior valor;
#b) O menor valor;
#c) A soma dos valores;
#d) A média aritmética dos valores;
#e) A porcentagem de valores que são positivos;
#f) A porcentagem de valores negativos;

w = int(input("Digite a quantidade de valores que você deseja: "))

while (w < 0 or w > 20):
    print("Valor inválido!")
    n = int(input("Digite a quantidade de valores que você deseja: "))

nmenor = 1000000000000
soma = 0 
c = 0
nm = 0
pos = 0
neg = 0
porcen = 0

while (c < w):
    c = c + 1
    n = int(input("Digite um valor: "))
    if (nm < n):
        nm = n 
    elif (nmenor > n):
        nmenor = n
    soma = soma + n 
    media = soma / w 
    if (n < 0):
        neg = neg + 1
    else:
        pos = pos + 1
porcenNEG = (neg*100) / w
porcenPOS = (pos*100) / w
print("O maior valor digitado foi: {}".format(nm))
print("O menor valor digitado foi: {}".format(nmenor))
print("A soma de todos os valores é: {}".format(soma))
print("A média aritmética desses valores é: {:.2f}".format(media))
print("A porcentagem de valores positivos é: {}%".format(porcenPOS))
print("A porcentagem de valores negativos é: {}%".format(porcenNEG))
