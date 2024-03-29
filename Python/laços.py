import time
for c in range(3, 0,-1):
  print('olá mundo!!!')
  time.sleep(1)
  print(c)

s=0
for c in range(0, 4):
  n = int(input('Digite um número: '))
  s += n
print('o Somatório dos números é {}'.format(s))
s=0
for c in range(1, 10):
  if c%3 == 0:
    s += c
print('a soma é {}'.format(s))
s = 0
for c in range(1, 501):
  if c%3 == 0:
    s += c
print('a soma é {}'.format(s))

pa=[]
ni = int(input('Digite o primeiro número da pa: '))
ra = int(input('Digite a sua razão: '))
for c in range(0, 10):
  nn = ni + (ra * c)
  pa.append(nn)
print(pa)

palin = str(input('Digite o seu possível palíndromo: ')).replace(' ','')
tp = len(palin)
mtp = len(palin)//2
resposta = False
for c in range(0, mtp):
  if palin[c] == palin[tp-1-c]:
    resposta = True
  else:
    resposta = False
    break
  print('inicio {}'.format(palin[c]))
  print('fim {}'.format(palin[tp-1-c]))
if resposta:
  resposta = ''
else:
  resposta = 'não '
print('A frase dada {}é um palindromo'.format(resposta))

soma = 0
ihv = 0
nhv = ''
cmj = 0
for c in range(0, 4):
  nome = str(input('Digite o nome de uma pessoa: '))
  sexo = str(input('Digite h para homem e m para mulher: '))
  idade = int(input('Digite a idade: '))
  soma += idade
  if sexo == 'h':
    if ihv < idade:
      nhv = nome
      ihv = idade
  else:
    if idade < 20:
      cmj +=1
media = soma/4
print('A média de idades deu {}. o Homem mais velho é {} com {} anos. A lista tem {} mulheres com menos de 20 anos'.format(media, nhv, ihv, cmj))

n = 1
while n != 0:
  n = int(input('Digite um valor'))
print('Fim')

while True:
  n = int(input('Digite um Valor: '))
  if n == 0:
    break
print('O Fim!!!!')