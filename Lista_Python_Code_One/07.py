from math import sqrt

# PRIMEIRO MÉTODO

x1 = float(input('Coordenada x do primeiro ponto: '))
y1 = float(input('Coordenada y do primeiro ponto: '))
x2 = float(input('Coordenada x do segundo ponto: '))
y2 = float(input('Coordenada y do segundo ponto: '))

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('Distância entre os pontos =', distancia)

# -------------------------------------------------------------------------
# SEGUNDO MÉTODO

x1, y1 = map(float, input('Coordenadas do ponto 1 (separadas por espaços): ').split())
x2, y2 = map(float, input('Coordenadas do ponto 2 (separadas por espaços): ').split())

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('Distância entre os pontos =', distancia)