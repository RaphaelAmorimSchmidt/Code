resp = 'S'
c = 0
total = 0
maior = 0
menor = 0
while(resp not in 'Nn'):
    resp = input('Você quer acrescentar um número para calcular a média? Se sim digite o número, se não digite N: ')
    if(resp.isnumeric()):
        c += 1
        resp = int(resp)
        total += resp
        if c == 1:
            maior = resp
            menor = resp
        else:
            if maior < resp:
                maior = resp
            if menor > resp:
                menor = resp
    resp = str(resp)
media = total/c
print('A média ficou em {} entre os {} elementos. O maior núemro foi {} e o menor foi {}'.format(media, c, maior, menor))
        
