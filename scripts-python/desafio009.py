n = int(input('Digite um numero:'))
print(f'\nTabuada do {n}:\n')
for i in range(1, 11):
    r = n * i
    print(f'{n} x {i} = {r}')