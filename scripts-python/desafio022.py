nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Nome em Maiusculas: {}'.format(nome.upper()))
print('Nome em Minusculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras:'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

