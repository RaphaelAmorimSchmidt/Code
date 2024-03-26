import emoji
import random
nome = str(input('Qual é o seu nome? '))
if nome == 'Raphael':
    print('Olá Raphael! Bom dia')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular')
else:
    print('Bom dia!')
print('-*'*15)
valor = float(input('Olá Qual o valor da casa para qual deseja o empréstimo? '))
salario = float(input('E seu salário? '))
anos = float(input('Em quanto anos pretende pagar? '))
prestacao = valor/(anos*12)
aprovacao = salario*0.3 >= prestacao
print(prestacao)
print(salario*0.3)
print(aprovacao)
if aprovacao:
    print('Parabéns seu empréstimo foi aprovado no valor de R${:.2f} ao mês'.format(prestacao))
else:
    print('Infelizmente seu empréstimo foi recusado')
print('-*'*15)
print('-*'*15)
print('Vamos jogar JoKenPô!!!!')
print('Escolha uma das três opções:')
print(emoji.emojize('1 - para pedra :raised_fist:'))
print('2 - para tesoura ✌')
print('3 - para papel 🖐')
escolha = int(input( 'Qual você quer: '))
if escolha == 1:
    emoesc = '✊'
elif escolha == 2:
    emoesc = '✌'
else:
    emoesc = '🖐'
pcescolha = random.randint(1,4)
if pcescolha == 1:
    emopcesc = '✊'
elif pcescolha == 2:
    emopcesc = '✌'
else:
    emopcesc = '🖐'

if escolha == pcescolha:
    print('Empate!!!!')
elif (escolha == 1 and pcescolha == 2) or (escolha == 2 and pcescolha == 3) or (escolha == 3 and pcescolha == 1):
    print('Parabéns você ganhou!!!!!')
else:
    print('Você perdeu!!!!!')
print(emoji.emojize('{} {}'.format(emoesc,emopcesc)))