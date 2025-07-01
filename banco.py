menu = """
    1 - Depósito
    2 - Saque
    3 - Extrato

    0 - Sair
"""
saldo = 0
depositos = "Depositos: \n"
saques = "Saques: \n"

contador_de_saques = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_SAQUES_VALOR = 500

opcao = -1
while(opcao != 0):
    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    if(opcao in range(0,4)):
        print("Acessando funcionalidade ...")
    else:
        print("Opcão inválida, tente novamente.")
        continue

    if(opcao == 1):
        print("\nDepósito")
        deposito_temporario = float(input("Digite o valor que deseja depositar:"))
        
        if(deposito_temporario <= 0):
            print("Valor de depósito inválido.")
        else:
            print("Depositando valor...")

            depositos += f"+ R${deposito_temporario}\n"
            saldo += deposito_temporario

            print("Deposito efetuado com sucesso.")

    if(opcao == 2):
        print(f"\nSaldo: {saldo}")
        print(f"Quantidade de saques disponiveis: {LIMITE_SAQUES_DIARIOS-contador_de_saques}")
        saque_temporario = float(input("Digite o valor que deseja sacar: "))

        if(saque_temporario <= 0):
            print("Valor de saque inválido.")
            continue
        elif(saque_temporario > saldo):
            print("Valor de saque maior que saldo disponível.")
            continue
        elif(contador_de_saques >= LIMITE_SAQUES_DIARIOS):
            print("Limite de saque diário atingido.")
            continue
        elif(saque_temporario > LIMITE_SAQUES_VALOR):
            print("Valor ultrapassa limite de saque.")
            continue
        else:
            print("Efetuando saque...")
            saques += f"- R${saque_temporario}\n"
            saldo -= saque_temporario
            contador_de_saques += 1
            print("Saque realizado com sucesso.")

    if(opcao == 3):
        print(f"""
Extrato
Saldo: R${saldo}
{depositos}
{saques}
        """)
    if(opcao == 0):
        print("Obrigado por utilizar nosso serviço tenha um bom dia!")
    
    