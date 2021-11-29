# Solucao: lista com os nomes dos numeros na posicao referente ao algarismo
# e a cada digito do numero escolhido pelo usuario retorna o nome do digito

def NumberName(integer):
  numberList = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
  return numberList[integer]

number = input("Digite um numero: ")
names = ""

for i in number:
  names += NumberName(int(i)) + " "

print("Os numeros por extenso são", names)
