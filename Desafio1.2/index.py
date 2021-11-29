# Solucao: condicoes para diferentes combinacoes dos retangulos de acordo com o plano cartesiano,
# observando a transformacao do eixo x e y.

def PrintArea(base, height):
  return print("Há intersecção e a área da intersecção é %d." %(base*height))


x1, y1 = input("Insira a coordenada superior do retangulo 1 separadas por espaço: ").split()
x2, y2 = input("Insira a coordenada inferior do retangulo 1 separadas por espaço: ").split()
x3, y3 = input("Insira a coordenada superior do retangulo 2 separadas por espaço: ").split()
x4, y4 = input("Insira a coordenada inferior do retangulo 2 separadas por espaço: ").split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x3 = int(x3)
y3 = int(y3)
x4 = int(x4)
y4 = int(y4)

# Verifica se o y1 esta contido no y3 e se y4 e maior ou igual que y2
if(y3 > y1 & y1 > y4 & y4 >= y2):
  height = y1 - y4

  # Verifica se o y2 está contido no outro retangulo
  if(x1 < x3 & x3 < x2 & x2 < x4):
    base = x2 - x3
  
  # Verifica se o y1 e o y2 estao fora do eixo x do outro retangulo
  elif(x1 < x3 & x3 < x4 & x4 < x2):
    base = x4 - x3
  
  # Verifica se o eixo x sao iguais
  elif((x1 == x3) & (x2 == x4)):
    base = x2 - x1
  
  PrintArea(base, height)

# Verifica se o y3 esta contido no y1 e se y2 esta contido no y4
elif(y1 > y3 & y3 > y2 & y2 > y4):
  height = y3 - y2

  # Verifica se o y1 esta contido no eixo x do outro retangulo
  if(x3 < x1 & x1 < x4 & x4 < x2):
    base = x4 - x1
  
  # Verifica se o y1 e o y2 estao contidos no eixo x do outro retangulo
  elif(x3 < x1 & x1 < x2 & x2 < x4):
    base = x2 - x1
  
  # Verifica se o y1 e o y2 estao fora do eixo x do outro retangulo
  elif(x1 < x3 & x3 < x4 & x4 < x2):
    base = x4 - x3
  
  PrintArea(base, height)

# Verifica se o lado superior ou inferior coincidem
elif(y1 >= y3 & y3 > y4 & y4 >= y2):
  height = y3 - y4

  # Verifica se o y2 esta contido no outro retangulo
  if(x1 < x3 & x3 < x2 & x2 < x4):
    base = x2 - x3

  # Verifica se o y1 e o y2 estao fora do eixo x do outro retangulo
  elif(x1 < x3 & x3 < x4 & x4 < x2):
    base = x4 - x3
  
  # Verifica se o y1 e o y2 estao contidos no eixo x ou x2 igual a x4
  elif(x3 < x1 & x1 < x2 & x2 <= x4):
    base = x2 - x1

  # Verifica se o y1 esta contido no eixo x do outro retangulo
  elif(x3 < x1 & x1 < x4 & x4 < x2):
    base = x4 - x1
  
  PrintArea(base, height)

# Verifica se um retangulo esta totalmente contido no outro
elif(y3 > y1 & y1 > y2 & y2 > y4):
  height = y1 - y2

  # Verifica se o y1 e o y2 estao fora do eixo x do outro retangulo
  if(x1 < x3 & x3 < x4 & x4 < x2):
    base = x4 - x3
  
  # Verifica se o y1 e o y2 estao contidos no eixo x do outro retangulo
  elif(x3 < x1 & x1 < x2 & x2 < x4):
    base = x2 - x1
  
  PrintArea(base, height)

# Verifica se os retangulos sao do mesmo tamanho
elif ((y2 == y4) & (y1 == y3)):
  height = y2 - y1

  # Verifica se o eixo x são iguais
  if((x1 == x3) & (x2 == x4)):
    base = x2 - x1
  PrintArea(base, height)
else:
  print("Não há intersecção")

  

