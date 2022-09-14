#24. Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).
nome = input('Digite seu nome: ').upper()
sexo = input('Digite seu sexo, F para  Feminino ou M para Masculino: ').upper()
estado = input ('Digite seu estado civil: solteiro, casado, separado, divorciado e viúvo. ').upper()

if (sexo == 'F' and estado == 'CASADA'):
    (input ('Digite a quanto tempo está casada: '))
    print ('Fim do processo!')
else: 
    print ('Fim do processo!')