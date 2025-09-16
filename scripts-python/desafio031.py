distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta preste a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 1.30
else:
    preco = distancia * 1.00
print('E o preço da sua viagem será de R${:.2f}'.format(preco))