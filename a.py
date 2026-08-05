menu = 'Menu \n 1. Insira um numero \n 2. Sair'

while True:
    print(menu)
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        try:
            num = int(input('Digite um número: '))
    
            if num < 2:
                primo = False
            elif num == 2:
                primo = True
            elif num % 2 == 0:
                primo = False
            else:
                primo = True
                for i in range(3, int(num**0.5) + 1, 2):
                    if num % i == 0:
                        primo = False
                        break
            
            if primo:
                print(f'O número {num} é primo')
            else:
                print(f'O número {num} não é primo')
        
        except ValueError:
            print('Digite apenas números inteiros')
    
    elif opcao == '2':
        print('Saindo...')
        break
    
    else:
        print('Escolha 1 ou 2')
    
    print()