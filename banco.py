def saque (*,saldo :float,saques :str,limite :int,numero_saques :int,limite_saques :int):
    verificador = -1
    while (verificador != 0):
        print(f"\nSaldo: {saldo}")
        print(f"Quantidade de saques disponiveis: {limite_saques-numero_saques}")
        saque_temporario = float(input("Digite o valor que deseja sacar: "))

        if(saque_temporario <= 0):
            print("Valor de saque inválido.")
            continue
        elif(saque_temporario > saldo):
            print("Valor de saque maior que saldo disponível.")
            continue
        elif(numero_saques >= limite_saques):
            print("Limite de saque diário atingido.")
            break
        elif(saque_temporario > limite):
            print("Valor ultrapassa limite de saque.")
            continue
        else:
            print("Efetuando saque...")
            saques += f"- R${saque_temporario}\n"
            saldo -= saque_temporario
            numero_saques += 1
            verificador = 0
            print("Saque realizado com sucesso.")
    return saldo, saques, numero_saques

def deposito (saldo :float ,depositos :str,/):
    verificador = -1
    while(verificador != 0):
        print("\nDepósito")
        deposito_temporario = float(input("Digite o valor que deseja depositar:"))
                
        if(deposito_temporario <= 0):
            print("Valor de depósito inválido.")
        else:
            print("Depositando valor...")

            depositos += f"+ R${deposito_temporario}\n"
            saldo += deposito_temporario
            verificador = 0

            print("Deposito efetuado com sucesso.")

    return saldo, depositos

def exibir_extrato (saldo :int,/,*,depositos :str,saques :str):
    print(f"""
Extrato
Saldo: R${saldo:.2f}
{depositos}
{saques}
        """)

def criar_usuario (cpf :int):
    usuario = {}
    usuario["nome"] = input("Digite o seu nome: ")
    usuario["data_de_nascimento"] = input("Digite a data de nascimento, no seguinte formato DD/MM/AAAA: ")
    usuario["cpf"] = cpf
    usuario["endereço"] = input("Digite o endereço seguindo o seguinte modelo (logradouro, numero - bairro - cidade/sigla estado): ")

    # nome, data de nascimento, cpf(unico e sem pontos) e endereço(logradouro, numero - bairro - cidade/sigla estado)
    # usuario = { nome = "rafael", data_de_nascimento = "12/02/1987", cpf = 12345678900, endereco = "String com endere;o"}
    return usuario

def criar_conta (usuario :dict,numero_da_conta :int):
    conta = {}
    conta["agencia"] = "0001"
    conta["numero_da_conta"] = numero_da_conta
    conta["usuario"] = usuario
    conta["saldo"] = 0
    conta["saques"] = "Saques: \n"
    conta["depositos"] = "Depositos: \n"
    conta["limite"] = 500
    conta["limite_saques"] = 3
    conta["numero_de_saques"] = 0
    # agência(fixo: "0001"), número da conta(sequencial iniciando em 1) e usuário(usuário pode ter mais de uma conta, mas uma conta so pode ter 1 usuário)
    # conta = {agencia = 0001, numero_da_conta = 1, usuario, saldo = 0, saques = "Saques: \n", depositos = "Depositos: \n", limite_de_saque = 500, quantidade_limite_de_saques = 3, numero_de_saques = 0}

    return conta

def menu_da_conta (conta):
    menu = f"""
    Conta {conta["numero_da_conta"]} de {conta["usuario"]["nome"]}:

    1 - Depósito
    2 - Saque
    3 - Extrato

    0 - Retornar ao Inicio
    """
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
            conta["saldo"], conta["depositos"] = deposito(conta["saldo"],conta["depositos"])
        if(opcao == 2):
            conta["saldo"], conta["saques"], conta["numero_de_saques"] = saque(saldo=conta["saldo"], saques=conta["saques"], limite=conta["limite"], numero_saques=conta["numero_de_saques"],limite_saques=conta["limite_saques"])
        if(opcao == 3):
            exibir_extrato(conta["saldo"],depositos=conta["depositos"],saques=conta["saques"])
        if(opcao == 0):
            print("Obrigado por utilizar nosso serviço tenha um bom dia!")
        
def listar_contas (contas :list):
    print("Contas: ")
    for conta in contas:
        print(f"    {conta["numero_da_conta"]} - Conta {conta["numero_da_conta"]}")
    print("\n0 - Voltar") 

menu_inicial = """
    1 - Entrar com um usuário existente
    2 - Criar um novo usuário
    3 - Criar uma nova conta

    0 - Sair
"""
opcao = -1
dict_de_usuarios = {} # dict Chave = CPF e Valor = Todos os dados daquele CPF, incluindo o próprio CPF
dict_de_contas = {} # dict Chave = CPF e Valor = Lista com todas as contas daquele CPF

while (opcao != 0):
    print(menu_inicial)
    opcao = int(input("Digite a opçao desejada: "))

    if(opcao == 1):
        cpf_temporario = input("Digite o cpf do usuário: ")
        cpf_temporario = int(cpf_temporario.strip().replace(".","").replace("-",""))

        if(cpf_temporario in dict_de_usuarios and cpf_temporario in dict_de_contas): # caso en que um usuário tem uma conta
            listar_contas(dict_de_contas[cpf_temporario])

            opcao_de_conta = -1
            while(opcao_de_conta != 0):
                opcao_de_conta = int(input("Digite qual conta deseja utilizar: "))
                print(opcao_de_conta)
                print(list(range(1,len(dict_de_contas[cpf_temporario])+1)))
                if(opcao_de_conta in range(1,len(dict_de_contas[cpf_temporario])+1)):
                    print("Acessando conta ...")
                    menu_da_conta(dict_de_contas[cpf_temporario][opcao_de_conta-1])
                    opcao_de_conta = 0
                elif(opcao_de_conta == 0):
                    print("Voltando...")
                else:
                    print("Opcão inválida, tente novamente.")
        elif(cpf_temporario in dict_de_usuarios and cpf_temporario not in dict_de_contas): # caso em que um usuário não criou uma conta
            print("Usuário sem conta, tente novamente após criar uma nova conta.")
        else: # caso em que não foi encontrado usuário
            print("Usuário não encontrado, tente novamente após o cadastro.")

    if(opcao == 2):
        cpf_temporario = input("Digite o cpf do usuário: ")
        cpf_temporario = int(cpf_temporario.strip().replace(".","").replace("-",""))

        if(cpf_temporario in dict_de_usuarios):
            print("Usuário já cadastrado.")
        else:
            dict_de_usuarios[cpf_temporario] = criar_usuario(cpf_temporario)
            print("Usuário cadastrado com sucesso.")

    if(opcao == 3):
        cpf_temporario = input("Digite o cpf do usuário: ")
        cpf_temporario = int(cpf_temporario.strip().replace(".","").replace("-",""))

        if(cpf_temporario not in dict_de_contas and cpf_temporario in dict_de_usuarios): # caso em que usuário não tem conta
            dict_de_contas[cpf_temporario] = [criar_conta(dict_de_usuarios[cpf_temporario], 1)]
            print("Conta criada com sucesso.")
        elif(cpf_temporario in dict_de_contas and cpf_temporario in dict_de_usuarios): # caso em que usuário já possui uma conta
            quantidade_de_contas = len(dict_de_contas[cpf_temporario])
            lista_de_contas = list(dict_de_contas[cpf_temporario]).copy()
            lista_de_contas.append(criar_conta(dict_de_usuarios[cpf_temporario],quantidade_de_contas+1))
            dict_de_contas[cpf_temporario] = lista_de_contas
            print("Conta criada com sucesso.")
        else: # caso em que usuário não está cadastrado
            print("Usuário não cadastrado, tente novamente depois do cadastro.")
            
    if(opcao == 0):
        print("Saindo do aplicativo ...")