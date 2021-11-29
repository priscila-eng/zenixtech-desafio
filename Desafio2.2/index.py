# Solucao: verifica se um numero e primo, fazendo divisoes sucessivas dos numeros inferior a ele.
# Se houver 2 divisoes com resto 0 (1 e ele mesmo), o numero e classificado como primo.
# Caso contrario e acumulado os divisores onde o resto e 0 e apresenta a lista.

number = int(input("Digite um numero: "))

dividersList = []
for i in range(1, number + 1):
  if (number%i == 0):
    dividersList.append(i)

if (len(dividersList) == 2):
  print("O numero %d é primo." % number)
else:
  dividersList.pop(len(dividersList) - 1)
  print("O número %d não é primo." % number)
  print("E seus divisores são", dividersList)
