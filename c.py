salario = float(input('Digite o salário: R$ '))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f'\nSalário inicial: R$ {salario:.2f}')
print(f'Percentual de aumento: {percentual}%')
print(f'Valor do aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')