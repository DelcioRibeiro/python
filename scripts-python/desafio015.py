dias = int(input('Quantos dias alugados? '))
km = float(input('Qauntos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de R${:.2f}'.format(pago))