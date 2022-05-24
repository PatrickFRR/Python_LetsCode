contador = 1
soma = 0
termo = 1

while contador <= 1000:
  termo = termo / contador
  soma += termo
  contador += 1

print(soma)