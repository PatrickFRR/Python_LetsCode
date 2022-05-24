# PRIMEIRO MÉTODO
lista = [5, 3, 9, 0, 1, 2, 6, 4, 7, 8]

print('Lista inicial:', lista, '\n')

print('Quatro primeiros elementos: ', lista[:4])
print('Cinco últimos elementos: ', lista[-5:])
print('Elementos nas posições pares: ', lista[::2])
print('Elementos nas posições ímpares: ', lista[1::2])

# SEGUNDO MÉTODO
from random import randint

def gerar_lista_aleatoria():
  lista_aleatoria = []
  for i in range(10):
    lista_aleatoria.append(randint(1, 100))
  
  return lista_aleatoria

lista = gerar_lista_aleatoria()
print('\n\nLista inicial:', lista, '\n')

print('Quatro primeiros elementos: ', lista[:4])
print('Cinco últimos elementos: ', lista[-5:])
print('Elementos nas posições pares: ', lista[::2])
print('Elementos nas posições ímpares: ', lista[1::2])