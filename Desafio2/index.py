# Solucao: loop de 1 ate o numero digitado pelo usuario e cada numero dessa contagem entra em outro loop,
# onde replica o numero i vezes. Depois, a soma da linha e calculada multiplicando o numero por ele mesmo.
# Por fim, a soma final e calculada acumulando a soma de cada linha.

number = int(input("Digite um numero: "))

finalSum = 0
for i in range(1, number + 1):
  for j in range (0, i):
    print(i, end=" ")
  print("")
  print("Soma:", (i*i))
  finalSum += i * i

print("A soma final é", finalSum)