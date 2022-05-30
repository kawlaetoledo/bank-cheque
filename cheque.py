Contas = {'cod' : [], 'saldo' : [], 'tr' : []}
Trans = {'cod' : [], 'tipo' : [], 'origem' : [], 'destino' : [], 'valor' : []}
Clientes = {'cod' : [], 'nome' : [], 'tel' : [],'cpf' : [], 'ccorrente' : []}
numClientes = 0

ok = True
while ok:

    # Menu Inicio ---------------------------------------------------------------------------------------------//
    print ("")
    print ("1 - Cliente")
    print ("2 - Transaçao")
    print ("3 - Sair")

    menuop = input("Digite o numero da opçao desejada: ")
    
    # Fecha Programa -----------------------------------------------------------------------------------------//
    if menuop == '3':
        ok = False

    # Menu Cliente ------------------------------------------------------------------------------------------//
    if menuop == '1':

        ok1 = True
        while ok1:

            print("")
            print("1 - Inserir novo cliente")
            print("2 - Consultar dados de um cliente")
            print("3 - Atualizar cadastro de um cliente")
            print("4 - Remover um clientes")
            print("5 - Imprimir lista de clientes")
            print("6 - Voltar")

            menuCliente = input ("\nDigite o numero da opçao desejada: ")

            ## Sair do menu cliente ----------------------------------------------------------------------//
            if menuCliente == '6':
                ok1 = False

            ## 1 - Inserir novo cliente ------------------------------------------------------------------//
            if menuCliente == '1':

                if numClientes < 50:
                    
                    cod = input ("\nInforme o codigo do cliente: ")
                    nome = input ("Informe o nome do cliente: ")
                    tel = input ("Informe o telefone do cliente: ")
                    ccorrente = input ("Informe o numero da conta corrente do cliente: ")
                    cpf = input ("Informe o numero do seu CPF: ")
                    adicionarcheque = input ("\nInforme o número do cheque: ")
                    adicionarcheque = input ("\nInforme a data de emissão do cheque: ")
                    adicionarcheque = input ("\nInforme a data de vencimento do cheque: ")
                    adicionarcheque = input ("\nInforme a data de deposito do cheque: ")
                    adicionarcheque = input ("\nInforme observação do cheque: ")
                    adicionarcheque = input ("Informe o valor do cheque que queira adicionar: ")
                    adicionarcheque = float(adicionarcheque)
                    
                    
                    Clientes['cod'].append(cod)
                    Clientes['nome'].append(nome)
                    Clientes['tel'].append(tel)
                    Clientes['cpf'].append(cpf)
                    Clientes['ccorrente'].append(ccorrente)
                    Contas['cod'].append(ccorrente)
                    Contas['saldo'].append(adicionarcheque)

                    
                    numClientes = numClientes + 1

                else:
                    print("\nNumero maximo de clientes atingido!!")

            ## 2 - Consultar dados de um cliente -------------------------------------------------------//
            if menuCliente == '2':
                
                consultar = input ("\nInforme o codigo do cliente: ")
                consultarV = consultar in Clientes['cod']
                
                if consultarV == True:
                    
                    pos = Clientes['cod'].index(consultar)
                    print("Codigo \t Nome \t Telefone \t CPF \t\t Conta \t Saldo")
                    print("{0} \t {1} \t {2} \t {3} \t {4} \t {5}".format(Clientes['cod'][pos],Clientes['nome'][pos],Clientes['tel'][pos],Clientes['cpf'][pos],Clientes['ccorrente'][pos],Contas['saldo'][pos]))

                else:
                    print("Codigo invalido!!!")

            ## 3 - Atualizar cadastro de um cliente --------------------------------------------------//
            if menuCliente == '3':
                
                consultar = input ("\nInforme o codigo do cliente: ")
                consultarV = consultar in Clientes['cod']
                
                if consultarV == True:
                    
                    #newcodigo = input ("\nInforme o novo codigo do cliente: ")
                    newnome = input ("Informe o novo nome do cliente: ")
                    newtel = input ("Informe o novo telefone do cliente: ")
                    newcpf = input ("Informe o novo CPF do cliente: ")
                    #newcc = input ("Informe o novo numero da conta corrente do cliente: ")
                    
                    pos = Clientes['cod'].index(consultar)
                    
                    #Clientes['cod'][pos] = newcodigo
                    Clientes['nome'][pos] = newnome
                    Clientes['tel'][pos] = newtel
                    Clientes['cpf'][pos] = newcpf
                    #Clientes['cc'][pos] = newcc

                    print("\nDados atualizados!!!\n")

                else:
                    print("Codigo invalido!!!")


            ## 4 - Remover um clientes -------------------------------------------------------------//
            if menuCliente == '4':
                
                consultar = input ("\nInforme o codigo do cliente: ")
                consultarV = consultar in Clientes['cod']
                
                if consultarV == True:
                    
                    pos = Clientes['cod'].index(consultar)
                    Clientes['cod'].pop(pos)
                    Clientes['nome'].pop(pos)
                    Clientes['tel'].pop(pos)
                    Clientes['cpf'].append(pos)
                    Clientes['ccorrente'].pop(pos)
                    Contas['cod'].pop(pos)
                    Contas['saldo'].pop(pos)

                    numClientes = numClientes - 1

                    print("Removido com sucesso")

                else:
                    print("Codigo invalido!!!")

                    
            ## 5 - Imprimir lista de clientes -----------------------------------------------------//
            if menuCliente == '5':
                
                print("Codigo \t Nome \t Telefone \t CPF \t\t Conta \t Saldo")
                print()
                
                for i in range(numClientes):              
                    
                    print("{0} \t {1} \t {2} \t {3} \t {4} \t {5}".format(Clientes['cod'][i],Clientes['nome'][i],Clientes['tel'][i],Clientes['cpf'][i],Clientes['ccorrente'][i], Contas['saldo'][i]))


    # FIM do Menu Cliente --------------------------------------------------------------------------//

    # Menu Transaçao -------------------------------------------------------------------------------//
    if menuop == '2':
        
        ok2 = True
        while ok2:

            print("")
            print("1 - Deposito")
            print("2 - Saque")
            print("3 - Excluir cheque")
            print("4 - Voltar")

            opmenu = input("\nDigite o numero da opçao desejada: ")
            
            if opmenu == '4':
                ok2 = False


            if opmenu == '1':

                consultar = input ("\nInforme o número da conta corrente em que deseja realizar o deposito do cheque: ")
                consultarV = consultar in Contas['cod']
                
                if consultarV == True:
                    
                    pos = Contas['cod'].index(consultar)
                    adicionarcheque = input ("\nInforme a data de emissão do cheque: ")
                    adicionarcheque = input ("\nInforme a data de vencimento do cheque: ")
                    adicionarcheque = input ("\nInforme a data de deposito do cheque: ")
                    adicionarcheque = input ("\nInforme observação do cheque: ")
                    adicionarcheque = input ("\nInforme o valor do cheque para ser depositado: ")
                    adicionarcheque = float(adicionarcheque)
                    valor = Contas['saldo'][pos]
                    valor = valor + adicionarcheque
                    Contas['saldo'][pos] = valor

                else:
                    input ("Conta nao existe!!")


                ### Lista de trans


            if opmenu == '2':

                consultar = input ("\nInforme o número da conta corrente em que deseja realizar o saque: ")
                consultarV = consultar in Contas['cod']
                
                if consultarV == True:
                    
                    pos = Contas['cod'].index(consultar)
                    fazsaque = input ("\nInforme o valor para saque: ")
                    fazsaque = float(fazsaque)
                    valor = Contas['saldo'][pos]
                    valor = valor - fazsaque
                    Contas['saldo'][pos] = valor

                    

                    
                                           
                else:
                    input ("Conta nao existe!!")

            if opmenu == '3':

                consultar = input ("\nInforme o número da conta corrente em que deseja excluir o cheque: ")
                consultarV = consultar in Contas['cod']
                
                if consultarV == True:
                    
                    pos = Contas['cod'].index(consultar)
                    excluicheque = input ("\nInforme o número do cheque: ")
                    excluicheque = input ("\nInforme o valor do cheque: ")
                    excluicheque = float(excluicheque)
                    valor = Contas['saldo'][pos]
                    valor = valor - excluicheque
                    Contas['saldo'][pos] = valor
                   
                                           
                else:
                    input ("Conta nao existe!!")

print ("Finalizando...")
