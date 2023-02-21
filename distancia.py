x1 = int(input("Digite a coordenada x do primeiro ponto: "))
y1 = int(input("Digite a coordenada y do primeiro ponto: "))
x2 = int(input("Digite a coordenada x do segundo ponto: "))
y2 = int(input("Digite a coordenada y do segundo ponto: "))

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
if dist >= 10:
  print("longe")
else:
  print("perto")
