primeiro = int(input('Informe um número inteiro: '))
segundo = int(input('Informe outro número inteiro: '))
terceiro = int(input('Informe um número real: '))

# a
print('\nLETRA (a)')
dobro_do_primeiro = primeiro * 2
metade_do_segundo = segundo / 2
print('(2 x N1) * (N2 / 2) =', dobro_do_primeiro * metade_do_segundo)

# b
print('\nLETRA (b)')
triplo_do_primeiro = primeiro * 3
print('(3 x N1) + N3 =', triplo_do_primeiro + terceiro)

# c
print('\nLETRA (c)')
print('N3^3 =', terceiro ** 3)