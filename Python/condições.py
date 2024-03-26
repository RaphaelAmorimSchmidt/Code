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