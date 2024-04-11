from random import uniform
from math import exp, fabs
'''w1 = uniform(-1,1)
w2 = uniform(-1,1)
w3 = uniform(-1,1)
w4 = uniform(-1,1)
w5 = uniform(-1,1)
w6 = uniform(-1,1)
w7 = uniform(-1,1)
w8 = uniform(-1,1)
w9 = uniform(-1,1)'''
# pesos obtidos em uma tentativa com 100 000 loops
w1 = -4.380923872884529
w2 = 6.726153540519979
w3 = 5.751799589626786
w4 = 5.7261071728490345
w5 = 6.781455666571737
w6 = -4.4002149010847456
w7 = -12.6458077312022
w8 = 17.331082945583177
w9 = -12.643562148906941
todos_casos = [[0,0],[0,1],[1,0],[1,1]]
previsao = [0,1,1,0]

def funcao(somatorio):
  return 1/(1+ exp(-1*somatorio))

def somatorio(pesos, entradas):
  n = 0
  soma = 0
  while n < len(pesos):
    soma += (pesos[n]*entradas[n])
    n += 1  
  return soma

def neuronio(pesos, entradas):
  return funcao(somatorio(pesos, entradas))

def camada(numero_neuronios,pesos,entradas):
  saidas = list()
  for c in range(numero_neuronios):
    saidas.append(neuronio(pesos[c],entradas))
  return saidas

def derivada_sigmoide(y):
  return y * (1 - y)

def lista_derivada_sigmoide(lista):
  saidas = list()
  for c in range(len(lista)):
    saidas.append(derivada_sigmoide(lista[c]))
  return saidas

def delta_oculta(lista_derivada_sigmoide,deltaSaida,pesos):
  saidas = list()
  for c in range(len(lista_derivada_sigmoide)):
    saidas.append(lista_derivada_sigmoide[c]*pesos[c]*deltaSaida)
  return saidas

#rodada de dados
def rodada_dados(entradas, pesos_camada_oculta, pesos_camada_saida):
  saidas_das_camadas = dict()
  saida_primeira_camada_oculta = camada(3,pesos_camada_oculta,entradas) #primeira camada oculta
  valor_neuronio_saida = neuronio(pesos_camada_saida,saida_primeira_camada_oculta) # valor neuronio de saida
  saidas_das_camadas['saida_primeira_camada_oculta'] = saida_primeira_camada_oculta
  saidas_das_camadas['valor_neuronio_saida'] = valor_neuronio_saida
  return saidas_das_camadas

#calculo de erros
def calculo_erro(previsao, valor_ativacao):
  return previsao - valor_ativacao

def somarotio_erros(erros):
  s=0
  for erro in erros:
    s += fabs(erro)
  return s

#multiplicador saida camada e delta de saida
def entrada_delta(i,k):
  return i*k


for j in range(1): #para demosntrar o alcance com os pesos obtidos
  valores_saida = dict()
  erros = list()
  #bloco rodada de dados
  for caso in todos_casos:
    saidas_das_camadas = rodada_dados(caso,[[w1,w2],[w3,w4],[w5,w6]],[w7,w8,w9])
    valores_saida['{}'.format(caso)] = saidas_das_camadas

  #bloco calculo de erro
  for i in range(len(todos_casos)):
    erros.append(calculo_erro(previsao[i], valores_saida['{}'.format(todos_casos[i])]['valor_neuronio_saida']))
  print('\n')
  print('//////O erro da {} rodada é {}///////'.format( j + 1 , somarotio_erros(erros)))
  for i in range(len(todos_casos)):
    print('{} ---{} -- erro = {}'.format(todos_casos[i], valores_saida["{}".format(todos_casos[i])]['valor_neuronio_saida'], erros[i]))

  

  #bloco correção de pesos do neuronio de saida
  for i in range(len(todos_casos)):
    key = "{}".format(todos_casos[i])
    valores_saida[key]['delta_saida'] = erros[i] * derivada_sigmoide(valores_saida[str(todos_casos[i])]['valor_neuronio_saida'])

  derivada_sigmoide_lista = dict()
  for i in range(len(todos_casos)):
    key = "{}".format(todos_casos[i])
    derivada_sigmoide_lista[key] = lista_derivada_sigmoide(valores_saida[key]['saida_primeira_camada_oculta'])
    valores_saida[key]['delta_escondida'] = list()
    for i in range(len(derivada_sigmoide_lista[key])):
      match i:
        case 0:
          peso_local = w7
        case 1:
          peso_local = w8
        case 2:
          peso_local = w9

      valores_saida[key]['delta_escondida'].append(derivada_sigmoide_lista[key][i] * peso_local * valores_saida[key]['delta_saida'])

  for i in range(3): #precisa rodar o número de neuronios por camada
    
    somatorio_entrada_delta_saida = 0
    novo_peso_saida = list()
    for caso in todos_casos:
      somatorio_entrada_delta_saida += entrada_delta(valores_saida["{}".format(caso)]['saida_primeira_camada_oculta'][i], valores_saida["{}".format(caso)]['delta_saida'])
    match i:
      case 0:
        peso_local = w7
      case 1:
        peso_local = w8
      case 2:
        peso_local = w9

    novo_peso_saida = (peso_local * 1) + (somatorio_entrada_delta_saida * 0.3)

    match i:
      case 0:
        w7 = novo_peso_saida
      case 1:
        w8 = novo_peso_saida
      case 2:
        w9 = novo_peso_saida

  #bloco correção de pesos do neuronio de camada oculta
  for i in range(3): #precisa rodar o número de neuronios por camada
    somatorio_entrada_delta_oculto_1_entrada = 0
    somatorio_entrada_delta_oculto_2_entrada = 0
    novo_peso_oculto = list()
    for caso in todos_casos:
      for k in range(2):
        if k == 0:
          somatorio_entrada_delta_oculto_1_entrada += entrada_delta(caso[k],valores_saida[str(caso)]['delta_escondida'][i])
        else:
          somatorio_entrada_delta_oculto_2_entrada += entrada_delta(caso[k],valores_saida[str(caso)]['delta_escondida'][i])
    
    for k in range(2):
      match i:
        case 0:
          match k:
            case 0:
              peso_local = w1
            case 1:
              peso_local = w2
        case 1:
          match k:
            case 0:
              peso_local = w3
            case 1:
              peso_local = w4
        case 2:
          match k:
            case 0:
              peso_local = w5
            case 1:
              peso_local = w6
      if k == 0:
        novo_peso = (peso_local * 1) + (somatorio_entrada_delta_oculto_1_entrada * 0.3)
      else:
        novo_peso = (peso_local * 1) + (somatorio_entrada_delta_oculto_2_entrada * 0.3)
      match i:
        case 0:
          match k:
            case 0:
              w1 = novo_peso
            case 1:
              w2 = novo_peso
        case 1:
          match k:
            case 0:
              w3 = novo_peso
            case 1:
              w4 = novo_peso
        case 2:
          match k:
            case 0:
              w5 = novo_peso
            case 1:
              w6 = novo_peso

print("""w1 = {}
w2 = {}
w3 = {}
w4 = {}
w5 = {}
w6 = {}
w7 = {}
w8 = {}
w9 = {}""".format(w1,w2,w3,w4,w5,w6,w7,w8,w9))
