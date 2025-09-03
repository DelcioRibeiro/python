from random import randint
computador = randint(0, 5) #Faz o pc sortear um numero.
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei ? ')) # Jogador tenta advinhar.
if jogador == computador:
    print('PARABENS! Você conseguiu me venceu!')
else:
    print('GANHEI! Eu pensei no numnero {} e não no {}'.format(computador, jogador))
