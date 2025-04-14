menu = """
#### Opções ####
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
extrato = '\n' + ' Extrato '.center(20, '#') + '\n'

while True:
    print(menu)
    print(f'Saldo: R${saldo:.2f}')
    print('Número de saques: ' + str(numero_saques))
    opcao = input('Selecione uma opção: ')

    if opcao == 'd':
        deposito = float(input('Digite o valor do depósito: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito:  R${deposito:.2f}\n'
        else:
            print('Valor negativo')
        
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            saque = float(input('Digite o valor do saque: '))
            if saque > 0:
                if saque <= (saldo):
                    if saque <= limite:
                        saldo -= saque
                        extrato += f'Saque:    -R${saque:.2f}\n'
                        numero_saques += 1
                    else:
                        print(f'O valor do saque ultrapassa o limite')
                else:
                    print(f'Saldo Insuficiente: {saldo}')
            else:
                print('Valor negativo')
        else:
            print('Limite de saques diário ultrapassado')

    elif opcao == 'e':
        print(extrato + '####################')
        
    elif opcao == 'q':
        break

    else:
        print('Selecione uma opção válida')
