import math
angulo = float(input('Digite o valor do angulo em graus: '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print('O seno de {:.2f}: {:.2f}'.format(angulo, seno))
print('O cosseno de {:.2f}: {:.2f}'.format(angulo, cosseno))
print('A tangente de {:.2f}: {:.2f}'.format(angulo, tangente))