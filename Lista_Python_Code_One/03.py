from math import pi

def calcular_area_circulo(raio):
  return pi * raio ** 2

raio = 10 # Você pode solicitar esse valor ao usuário
area = calcular_area_circulo(10)

print(area)