#import math
import random
import emoji
from math import sqrt, floor
num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raiz inteira de {} é {}'.format(num,floor(raiz)))
print(emoji.emojize('olá mundo :globe_showing_americas:', language='alias'))
print('-'*15)
alu1 = input('Difgite o nome do 1 aluno:')
alu2 = input('Difgite o nome do 2 aluno:')
alu3 = input('Difgite o nome do 3 aluno:')
alu4 = input('Difgite o nome do 4 aluno:')
seq = [ alu1, alu2, alu3, alu4]
random.shuffle(seq)
print(seq, seq[0])
print('o {} será quem apagará o quadro'.format(seq[0]))
print('-'*15)

