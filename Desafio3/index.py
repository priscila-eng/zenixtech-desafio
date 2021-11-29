# Solucao: Primeiro e feito uma matriz, onde as linhas sao preenchidas por asterisco,
# de acordo com a lista de inteiros digitado pelo usuario. Depois e feito um loop.
# com o objetivo de organizar os astericos em linhas que forma o grafico, ou seja, 
# cada inteiro, representa uma coluna do grafico. Por fim, o grafico e impresso no terminal.

numberList = input(" Digite uma lista de inteiros separados por espaço: ")
numbers = numberList.split(" ")
caractersList = []
caractersList2 = []

for i in numbers:
  for j in range (0, int(i)):
    caractersList2.append("*")
  caractersList.append(caractersList2)
  caractersList2 = []

caracterList_empty = [False for caracter in caractersList]
empty_value = ' '
graphicList = []

while not all(caracterList_empty):
  row = []
  for i, item in enumerate(caractersList):
    if item:
      value = item.pop(0)
      row.append(str(value))
    else:
      caracterList_empty[i] = True
      row.append(empty_value)
  graphicList.append(row)

graphicList.reverse()
for i in graphicList:
  print(*i, sep=" ")


