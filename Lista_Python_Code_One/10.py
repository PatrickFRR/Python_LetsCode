duracao_da_nota = {
  'W': 1,
  'H': 1/2,
  'Q': 1/4,
  'E': 1/8,
  'S': 1/16,
  'T': 1/32,
  'X': 1/64
}

composicao = '/HH/QQQQ/XXXTXTEQH/W/HW/'

# O método .strip() elimina o caracter que você colocar entre os parênteses, caso ele esteja no início ou no final da string
# O método .split() divide a string no caractere especificado entre os parênteses, gerando uma lista como resultado
compassos = composicao.strip('/').split('/')

qtd_corretos = 0
incorretos = []

for compasso in compassos:
  duracao_compasso = 0
  for nota in compasso:
    duracao_compasso += duracao_da_nota[nota]
  
  if duracao_compasso == 1:
    qtd_corretos += 1
  else:
    incorretos.append(compasso)

print('Qtd. de Corretos:', qtd_corretos)
if len(incorretos) > 0:
  print('Incorretos:', incorretos)