print('Olá Mundo!\n')
print('Esse é o meu programa!')
nome = "Raphael Amorim Schmidt"
idade = 34
print("meu nome é "+nome+" e minha idade é",idade)
print('*'*15)
numero1 = int(input("primeiro número: "))
numero2 = int(input("segundo número: "))
soma = numero1 + numero2
print( 'a soma entre {} e {} é {}'.format( numero1, numero2, soma ) )
print ('-'*15)
algo = input("Digite algo: ")
print('O digitado só tem numeros? {}\nO digitado só tem letras? {}\nO digitado está maiusculo? {} '.format(str(algo.isnumeric()), str(algo.isalpha()), str(algo.isupper())))
print('-'*15)
print(5**3)
print(5/2)
print(5//2)
print(5%2)
print('-'*15)
nome = "Raphael"
print('prazer em te conhecer {:=^20}!'.format(nome), end='')
print('divisão de 10 por 3 é {:.4f}'.format(10/3))