resp = 'S'
c = 0
total = 0
while(resp not in 'Nn'):
    resp = input('Você quer acrescentar um número para calcular a média? Se sim digite o número, se não digite N: ')
    if(resp.isnumeric()):
        c += 1
        total += int(resp)
media = total/c
print('A média ficou em {} entre os {} elementos.'.format(media, c))
        
