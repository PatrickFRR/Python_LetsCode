# SOLUÇÃO MAIS LONGA

mora_perto = input('Mora perto da vítima? ').lower()
trabalhou_com = input('Já trabalhou com a vítima? ').lower()
telefonou_para = input('Telefonou para a vítima? ').lower()
esteve_no_local = input('Esteve no local do crime? ').lower()
devia_para = input('Devia para a vítima? ').lower()

pontuacao_total = 0

if mora_perto == 'sim':
  pontuacao_total += 1
if trabalhou_com == 'sim':
  pontuacao_total += 1
if telefonou_para == 'sim':
  pontuacao_total += 1
if esteve_no_local == 'sim':
  pontuacao_total += 1
if devia_para == 'sim':
  pontuacao_total += 1

if pontuacao_total == 5:
  print('Assassino! 😱')
elif pontuacao_total >= 3:
  print('Cúmplice 😨')
elif pontuacao_total == 2:
  print('Suspeito 🧐')
else:
  print('Liberado 🙌')


# -----------------------------------------------------------------------

# SOLUÇÃO MAIS COMPACTA

# Ler as respostas já convertendo para booleano (comparando com o 'sim')
mora_perto = input('Mora perto da vítima? ').lower() == 'sim'
trabalhou_com = input('Já trabalhou com a vítima? ').lower() == 'sim'
telefonou_para = input('Telefonou para a vítima? ').lower() == 'sim'
esteve_no_local = input('Esteve no local do crime? ').lower() == 'sim'
devia_para = input('Devia para a vítima? ').lower() == 'sim'

# Ao somar booleanos, True será equivalente ao inteiro 1, e False será equivalente ao inteiro 0
pontuacao_total = mora_perto + trabalhou_com + telefonou_para + esteve_no_local + devia_para

if pontuacao_total == 5:
  print('Assassino! 😱')
elif pontuacao_total >= 3:
  print('Cúmplice 😨')
elif pontuacao_total == 2:
  print('Suspeito 🧐')
else:
  print('Liberado 🙌')