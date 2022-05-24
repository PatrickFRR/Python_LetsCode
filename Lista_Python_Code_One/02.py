numero = float(input('Informe um número: '))

if numero < 0 or numero > 100:
  print('Fora de intervalo')
elif numero <= 25:
  print('[0, 25]')
elif numero <= 50:
  print('(25, 50]')
elif numero <= 75:
  print('(50,75]')
else:
  print('(75,100]')