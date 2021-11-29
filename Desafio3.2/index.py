# Solucao: com a funcao count do python, consegui verificar quantas vezes a palavra esta contida na outra
# e quantos caracteres sao diferentes.

wordA, wordB = input(" Digite duas palavras separadas por espaço: ").split()
different = 0

if (wordA == wordB):
  print("As palavras são iguais")

else:
  if (len(wordA) == len(wordB)):

    for i in range(len(wordA)):
      if(wordA.count(wordB[i]) == 0):
        different += 1
    
    if(different == 1):
      print("As palavras tem o mesmo tamanho, mas possuem %d caracter diferente." %different)

    else:
      print("As palavras tem o mesmo tamanho, mas possuem %d caracteres diferentes." %different)

  else:
    repeatB = wordA.count(wordB)
    repeatA = wordB.count(wordA)

    if(repeatB == 0):
      print("A palavra %s não inclui a palavra %s."%(wordA, wordB))
    elif(repeatB == 1):
      print("A palavra %s inclui a palavra %s %d vez."%(wordA, wordB, repeatB))
    else:
      print("A palavra %s inclui a palavra %s %d vezes."%(wordA, wordB, repeatB))
    
    if(repeatA == 0):
      print("A palavra %s não inclui a palavra %s."%(wordB, wordA))
    elif(repeatA == 1):
      print("A palavra %s inclui a palavra %s %d vez."%(wordB, wordA, repeatA))
    else:
      print("A palavra %s inclui a palavra %s %d vezes."%(wordB, wordA, repeatA))