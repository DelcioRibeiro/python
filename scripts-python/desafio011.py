largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print(f'A parede tem {area}m² de area.')
print(f'Você vai precisar de {tinta} litros de tinta para pintar-la.')