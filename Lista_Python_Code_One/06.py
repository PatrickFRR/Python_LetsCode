# PRIMEIRO MÉTODO

def somar_elementos(lista):
  soma = 0
  for elemento in lista:
    soma += elemento

  return soma

lista_de_exemplo = [4, 6, 7, 5, 3]
resultado = somar_elementos(lista_de_exemplo)

print('Soma dos elementos da lista =', resultado)



# -------------------------------------------------------------
# MÉTODO DESONESTO 🤣🤣🤣🤣🤣

def somar_elementos(lista):
  return sum(lista)

lista_de_exemplo = [4, 6, 7, 5, 3]
resultado = somar_elementos(lista_de_exemplo)

print('Soma dos elementos da lista =', resultado)