#Cotação Dolar
cotacao_dolar = 5.00
#Entrada do usuario
dinheiro = float(input('Quanto dinheiro você tem? R$'))
#Conversão
dolares = dinheiro / cotacao_dolar
#Resultado
print(f'Com R${dinheiro} você pode comprar U${dolares}')