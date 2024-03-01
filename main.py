#so pode fazer 3 saques por dia
# cada saque deve ser menor ou igual a 500
# se nao tiver saldo printar sem saldo
# formato R$ xxxx.xx

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


"""

saldo = 1700
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    print(menu)
    opcao = input()


    if opcao == 'd':
        print('Depositar\n')
        deposito = float(input('Valor a ser depositado: '))
        saldo = saldo + deposito
        print(f'\nSaldo atualizado: R$ {saldo}')

    elif opcao == 's':

        print('sacar\n')

        saque = float(input('Valor a ser retirado: '))

        if saldo == 0 or saque > saldo:
            print('Não possui saldo suficiente para realizar esta transação')

        elif numero_saques > LIMITE_SAQUES:
            print('Limite diario de saques atingido')

        else:
            numero_saques = numero_saques + 1
            saldo = saldo - saque
            print(f'valor retirado com sucesso, seu novo saldo é de R$ {saldo}')

    elif opcao == 'e':
        print('\n==============================EXTRATO==============================')
        print(f'\nVoce ainda pode fazer mais {LIMITE_SAQUES - numero_saques} saques')
        print(f'\nSeu Saldo atual é de R$ {saldo}')
        print('\n===================================================================')

    elif opcao == 'q':
        print('Saindo do Banco')
        break

    else:
        print('Opção inserida invalida!')
