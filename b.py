salario = float(input('Digite o salario: '))
aumento = ''
porcentagem = ''
valoraument = ''

if salario < 281:
    aumento = salario * 1.20
    porcentagem = ('20%')
    valoraument = salario * 0.20

elif 280 < salario < 701:
    aumento = salario * 1.15
    porcentagem = ('15%')
    valoraument = salario * 0.15

elif 700 < salario < 1501:
    aumento = salario * 1.10
    porcentagem = ('10%')
    valoraument = salario * 0.10

else:
    aumento = salario * 1.05
    porcentagem = ('5%')
    valoraument = salario * 0.05

print(f'\nsalario inicial: {salario} ')
print(f'percentual de aumento aplicado: {porcentagem}')
print(f'valor do aumento: {valoraument}')
print(f'salario pos aumento: {aumento}')
