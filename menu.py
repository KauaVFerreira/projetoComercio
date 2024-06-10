from conexaobd import connect
from bd import *
from datetime import datetime, date
conbd = connect()

def menubd():
    print ('--------------------------------- \nEm qual tabela você irá operar?\n1- Produtos\n2- Clientes \n3- Funcionários \n4- Fornecedores \n5- Promoções \n6- Pedido \n0- Sair \n---------------------------------')

def opcaobd():
    while True:
        option = input('\nOpção: ')
        if option == '0':
            print ('\nPrograma encerrado!')
            break
        elif option == '1':
            print ('---------------------------------\nDigite: \n1- Para cadastrar produtos \n2- Para deletar produtos \n3- Para listar produtos \n4 -Para atualizar produtos \n0- Para voltar \n---------------------------------')
            while True:
                option = input('\nOpção: ')
                if option == '0':
                    print ('\nVoltando à página inicial.')
                    break
                elif option == '1':
                    nome = input ('\nDigite o nome do produto: ')
                    categoria = input('\nDigite a categoria do produto: ')
                    descricao = input ('\nDigite a descrição do produto: ')
                    quantidade = input ('\nDigite a quantidade do produto em estoque: ')
                    preco = float(input ('\nDigite o preço do produto: '))
                    fornecedor = input ('\nDigite o nome do fornecedor do produto: ') 
                    cadastrarProdutos(conbd, nome, categoria, descricao, quantidade, preco, fornecedor)
                elif option == '2':
                    nome = input ('\nDigite o nome do produto: ')
                    print('\nTem certeza que deseja *DELETAR* esse produto?\n1- sim\n2- não')
                    conf = input('\nOpção: ')
                    if conf == '1':
                        deletarProdutos(conbd, nome)
                    elif conf == '2':
                        print ('\nOperação cancelada.')
                    else:
                        print ('Você digitou uma opção inválida, a operação foi cancelada.')
                elif option == '3':    
                    listarProdutos(conbd)
                elif option == '4':
                    nome = input ('\nNome do produto: ')
                    descricao = input ('\nDescrição do produto: ')
                    preco = float(input ('\nPreço do produto: '))
                    atualizarProdutos(conbd, nome, descricao, preco, nomeAtual)
        elif option == '2':      
            print ('---------------------------------\nDigite: \n1- Para cadastrar clientes \n2- Para deletar clientes \n3- Para listar clientes \n4- Para atualizar clientes \n0- Para voltar \n---------------------------------')    
            while True:
                option = input('\nOpção: ')
                if option == '0':
                    print ('\nVoltando à página inicial.')
                    break
                elif option == '1':
                    nome = input ('\nDigite o nome do cliente: ')
                    sobrenome = input ('\nDigite o sobrenome do cliente: ')
                    endereco = input ('\nDigite o endereço do cliente: ')
                    cidade = input ('\nDigite a cidade do cliente: ')
                    codPostal = input ('\nDigite o código postal do cliente: ')
                    cadastrarClientes(conbd, nome, sobrenome, endereco, cidade, codPostal)
                elif option == '2':
                    nome = input ('\nDigite o nome do cliente: ')
                    sobrenome = input ('\nDigite o sobrenome do cliente: ')
                    print('\nTem certeza que deseja *DELETAR* esse cliente?\n1- sim\n2- não')
                    conf = input('\nOpção: ')
                    if conf == '1':
                        deletarClientes(conbd, nome, sobrenome)
                    elif conf == '2':
                        print ('\nOperação cancelada.')
                    else:
                        print ('Você digitou uma opção inválida, a operação foi cancelada.')
                elif option == '3':
                    listarClientes(conbd)
                elif option == '4':
                    IdAtual = input ('\nDigite o ID do cliente que deseja alterar: ')
                    print ('\n------Digite abaixo as informações atualizadas------ ')
                    nome = input ('\nNome do cliente: ')
                    sobrenome = input ('\nSobrenome do cliente: ')
                    endereco = input ('\nEndereço do cliente: ')
                    cidade = input ('\nCidade do cliente: ')
                    codigoPostal = input ('\nCódigo Postal do cliente: ')
                    atualizarClientes(conbd, nome, sobrenome, endereco, cidade, codigoPostal, IdAtual)
        elif option == '3':
            print ('---------------------------------\nDigite: \n1- Para cadastrar funcionários \n2- Para deletar funcionários \n3- Para listar funcionários \n4- Para atualizar funcionários \n0- Para voltar \n---------------------------------')
            while True:
                option = input('\nOpção: ')
                if option == '0':
                    print ('\nVoltando à página inicial.')
                    break
                elif option == '1':
                    nome = input ('\nDigite o nome do funcionário: ')
                    cargo = input ('\nDigite o cargo do funcionário: ')
                    departamento = input ('\nDigite o departamento do funcionário: ')
                    cadastrarFuncionarios(conbd, nome, cargo, departamento)
                elif option == '2':
                    nome = input ('\nDigite o nome do funcionário: ')
                    cargo = input('\nDigite o cargo do funcionário: ')
                    print('\nTem certeza que deseja *DELETAR* esse funcionário?\n1- sim\n2- não')
                    conf = input('\nOpção: ')
                    if conf == '1':
                        deletarFuncionarios(conbd, nome, cargo)
                    elif conf == '2':
                        print ('\nOperação cancelada.')
                    else:
                        print ('Você digitou uma opção inválida, a operação foi cancelada.') 
                elif option == '3':
                    listarFuncionarios(conbd)
                elif option == '18':
                    IdAtual = input ('\nDigite o ID do funcionário que deseja alterar: ')
                    print ('\n------Digite abaixo as informações atualizadas------ ')
                    nome = input ('\nNome do funcionário: ')
                    cargo = input ('\nCargo do funcionário: ')
                    departamento = input ('\nDepartamento do funcionário: ')
                    atualizarFuncionarios(conbd, nome, cargo, departamento, IdAtual)             
        elif option == '4':
            print ('---------------------------------\nDigite: \n1- Para cadastrar fornecedores \n2- Para deletar fornecedores \n3- Para listar fornecedores \n4- Para atualizar fornecedores \n0- Para voltar \n---------------------------------')
            while True:
                option = input('\nOpção: ')
                if option == '0':
                    print ('\nVoltando à página inicial.')
                    break
                elif option == '1':
                    nome = input ('\nDigite o nome do fornecedor: ')
                    contato = input ('\nDigite o contato do fornecedor: ')
                    endereco = input ('\nDigite o endereco do fornecedor: ')
                    cadastrarFornecedores(conbd, nome, contato, endereco)
                elif option == '2':
                    nome = input ('\nDigite o nome do fornecedor: ')
                    print('\nTem certeza que deseja *DELETAR* esse fornecedor?\n1- sim\n2- não')
                    conf = input('\nOpção: ')
                    if conf == '1':
                        deletarFornecedores(conbd, nome)
                    elif conf == '2':
                        print ('\nOperação cancelada.')
                    else:
                        print ('Você digitou uma opção inválida, a operação foi cancelada.')
                elif option == '3':
                    listarFornecedores(conbd)
                elif option == '4':
                    nomeAtual = input ('\nDigite o nome do fornecedor que deseja alterar: ')
                    print ('\n------Digite abaixo as informações atualizadas------ ')
                    nome = input ('\nNome do fornecedor: ')
                    contato = input ('\nContato do fornecedor: ')
                    endereco = input ('\nEndereco do fornecedor: ')
                    atualizarFornecedores(conbd, nome, contato, endereco, nomeAtual)
        elif option == '5':
            print ('---------------------------------\nDigite: \n1- Para cadastrar promoções \n2- Para deletar promoções \n3- Para listar promoções \n4- Para atualizar promoções \n0- Para voltar \n---------------------------------')
            while True:
                option = input('\nOpção: ')
                if option == '0':
                    print ('\nVoltando à página inicial.')
                    break
                elif option == '1':
                    nome = input ('\nDigite o nome da promoção: ')
                    descricao = input ('\nDigite a descrição da promoção: ')
                    dataInicio = input ('\nDigite a data de início da promoção (dd-mm-aaaa): ')
                    dataFim = input ('\nDigite a data de encerramento da promoção (dd-mm-aaaa): ')
                    dataInicio = datetime.strptime(dataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                    dataFim = datetime.strptime(dataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
                    cadastrarPromocoes(conbd, nome, descricao, dataInicio, dataFim)
                elif option == '2':
                    nome = input ('\nDigite o nome da promoção: ')
                    print('\nTem certeza que deseja *DELETAR* essa promoção?\n1- sim\n2- não')
                    conf = input('\nOpção: ')
                    if conf == '1':
                        deletarPromocoes(conbd, nome)
                    elif conf == '2':
                        print ('\nOperação cancelada.')
                    else:
                        print ('Você digitou uma opção inválida, a operação foi cancelada.')
                elif option == '3':
                    listarPromocoes(conbd)
                elif option == '4':
                    nomeAtual = input ('\nDigite o nome da promoção que deseja alterar: ')
                    print ('\n------Digite abaixo as informações atualizadas------ ')
                    nome = input ('\nNome da promoção: ')
                    descricao = input ('\nDescrição da promoção: ')
                    dataInicio = input ('\nData de início da promoção (dd-mm-aaaa): ')
                    dataFim = input ('\nData de encerramento da promoção (dd-mm-aaaa): ')
                    dataInicio = datetime.strptime(dataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                    dataFim = datetime.strptime(dataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
                    atualizarPromocoes(conbd, nome, descricao, dataInicio, dataFim, nomeAtual)          
        elif option == '6':
            print ('---------------------------------\nDigite: \n1- Para realizar o pedido \n2- Para avaliar um produto \n0- Para voltar \n---------------------------------')
            while True:
                option = input('\nOpção: ')
                if option == '0':
                    print ('\nVoltando à página inicial.')
                    break
                elif option == '1':
                    nome = input ('\nDigite o seu nome: ')
                    sobrenome = input ('\nDigite o seu sobrenome: ')
                    print ('\nMétodos de pagamento: \n1- Cartão de crédito \n2- Cartão de débito \n3- Boleto bancário \n4- Pix')
                    metodo = input ('\nEscolha o método de pagamento: ')
                    if metodo == '1':
                        metodo = 'Cartão de Crédito'
                    elif metodo == '2':
                        metodo = 'Cartão de Débito'
                    elif metodo == '3':
                        metodo = 'Boleto Bancário'
                    elif metodo == '4':
                        metodo = 'Pix'
                    data = date.today()
                    produto = input ('\nDigite o nome do produto que você deseja: ')
                    quantidade = int(input ('\nDigite a quantidade de produtos que você deseja: '))
                    cadastrarPedidos(conbd, nome, sobrenome, produto, quantidade, data, metodo)
                elif option == '2':
                    nome = input('\nDigite seu nome: ')
                    sobrenome = input('\nDigite seu sobrenome: ')
                    nomeProduto = input('\nDigite o nome do produto que deseja avaliar: ')
                    comentario = input('\nFaça seu comentário: ')
                    avaliacao = input('\nDe 1 a 5, digite quantas estrelas você dá a esse produto: ')
                    data = date.today()   
                    cadastrarComentario(conbd,nome,sobrenome,nomeProduto,comentario,avaliacao,data)
        