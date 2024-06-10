def acharIDProduto(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
    valores = (Nome,)
    Id_Produto = mycursor.execute(sql,valores)
    Id_Produto = mycursor.fetchone()[0]
    return Id_Produto

def acharIDCliente(conbd, Nome, Sobrenome):
    mycursor = conbd.cursor()
    sql = 'SELECT ID_Cliente FROM clientes WHERE Nome = %s AND Sobrenome = %s'
    valores = (Nome, Sobrenome)
    Id_Cliente = mycursor.execute(sql,valores)
    Id_Cliente = mycursor.fetchone()[0]
    return Id_Cliente

def cadastrarProdutos(conbd, Nome ,Categoria ,Descricao, Quantidade, Preco, Fornecedor):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO categoriasprodutos(Nome, Descricao) VALUES (%s, %s)'
    valores = (Nome, Categoria)
    mycursor.execute(sql,valores)
    Id_Categoria = mycursor.lastrowid
    sql = 'SELECT ID_Fornecedor FROM fornecedores WHERE Nome = %s'
    valor = (Fornecedor,)
    Id_Fornecedor = mycursor.execute(sql, valor)
    Id_Fornecedor = mycursor.fetchone()[0]
    sql = 'INSERT INTO produtos(Nome, Descricao, Preco, ID_Categoria, ID_Fornecedor) VALUES (%s, %s, %s, %s, %s)'
    valores = (Nome, Descricao, Preco, Id_Categoria, Id_Fornecedor)
    mycursor.execute(sql,valores)
    Id_Produto = mycursor.lastrowid
    sql = 'INSERT INTO estoque(ID_Produto, Quantidade) VALUES (%s, %s)'
    valores = (Id_Produto, Quantidade)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nProduto cadastrado com sucesso!')
    mycursor.close()

def cadastrarClientes (conbd,Nome,Sobrenome,Endereco,Cidade,CodigoPostal):
    mycursor =  conbd.cursor()
    sql = 'INSERT INTO clientes(Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s)'
    valores = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nCliente cadastrado com sucesso!')
    mycursor.close()

def cadastrarFuncionarios(conbd, Nome, Cargo, Departamento):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO funcionarios(Nome, Cargo, Departamento) VALUES (%s, %s, %s)'
    valores = (Nome, Cargo, Departamento)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nFuncionário cadastrado com sucesso!')
    mycursor.close()

def cadastrarFornecedores(conbd, Nome ,Contato ,Endereco):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO fornecedores(Nome, Contato, Endereco) VALUES (%s, %s, %s)'
    valores = (Nome, Contato, Endereco)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nFornecedor cadastrado com sucesso!')
    mycursor.close()
    
def cadastrarPromocoes(conbd, Nome, Descricao, DataInicio, DataFim):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO promocoes(Nome, Descricao, DataInicio, DataFim) VALUES (%s, %s, %s, %s)'
    valores = (Nome, Descricao, DataInicio, DataFim)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nPromoção cadastrada com sucesso!')
    mycursor.close()

def deletarProdutos(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM produtos WHERE Nome = %s'
    valores = (Nome,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nProduto deletado com sucesso!')
    mycursor.close()
    
    
def deletarClientes(conbd, Nome, Sobrenome):
    mycursor = conbd.cursor()
    Id_Cliente = acharIDCliente(conbd, Nome, Sobrenome)
    sql = 'DELETE FROM clientes WHERE ID_Cliente = %s'
    valores = (Id_Cliente,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nCliente deletado com sucesso!')
    mycursor.close()

def deletarFuncionarios(conbd, Nome, Cargo):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM funcionarios WHERE Nome = %s AND Cargo = %s'
    valores = (Nome, Cargo, )
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nFuncionário deletado com sucesso!')
    mycursor.close()
    
def deletarFornecedores(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM fornecedores WHERE Nome = %s'
    valores = (Nome,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nFornecedor deletado com sucesso!')
    mycursor.close()

def deletarPromocoes(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM promocoes WHERE Nome = %s'
    valores = (Nome,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nPromoção deletada com sucesso!')
    mycursor.close()
    
def listarProdutos(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM produtos'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()
    
def listarClientes(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM clientes'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()

def listarFuncionarios(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM funcionarios'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()
    
def listarFornecedores(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM fornecedores'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()
    
def listarPromocoes(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM promocoes'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()
    
def atualizarProdutos(conbd, Nome, Descricao, Preco, NomeAtual):
    mycursor = conbd.cursor()
    sql = 'UPDATE produtos set Nome = %s, Descricao = %s, Preco = %s WHERE Nome = %s'
    valores = (Nome, Descricao, Preco, NomeAtual)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nProduto atualizado com sucesso!')
    mycursor.close()
    
def atualizarClientes(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal, IdAtual):
    mycursor = conbd.cursor()
    sql = 'UPDATE clientes set Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE ID_Cliente = %s'
    valores = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal, IdAtual)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nCliente atualizado com sucesso!')
    mycursor.close()
    
def atualizarFuncionarios(conbd, Nome, Cargo, Departamento, IdAtual):
    mycursor = conbd.cursor()
    sql = 'UPDATE funcionarios set Nome = %s, Cargo = %s, Departamento = %s WHERE ID_Funcionario = %s'
    valores = (Nome, Cargo, Departamento, IdAtual)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nFuncionário atualizado com sucesso!')
    mycursor.close()

def atualizarFornecedores(conbd, Nome, Contato, Endereco, NomeAtual):
    mycursor = conbd.cursor()
    sql = 'UPDATE fornecedores set Nome = %s, Contato = %s, Endereco = %s WHERE Nome = %s'
    valores = (Nome, Contato, Endereco, NomeAtual)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nFornecedor atualizado com sucesso!')
    mycursor.close()

def atualizarPromocoes(conbd, Nome, Descricao, DataInicio, DataFim, NomeAtual):
    mycursor = conbd.cursor()
    sql = 'UPDATE promocoes set Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE Nome = %s'
    valores = (Nome, Descricao, DataInicio, DataFim, NomeAtual)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nPromoção atualizada com sucesso!')
    mycursor.close() 

def cadastrarPedidos(conbd,  Nome, Sobrenome, NomeProduto, Quantidade, Data_Pedido, MetodoPagamento):
    mycursor = conbd.cursor()
    Id_Cliente = acharIDCliente(conbd, Nome, Sobrenome)
    Id_Produto = acharIDProduto(conbd, NomeProduto)
    sql = 'SELECT Preco FROM produtos WHERE Nome = %s'
    valores = (NomeProduto,)
    Total = mycursor.execute(sql,valores)
    Total = float(mycursor.fetchone()[0])
    Total = float(Total*Quantidade)
    sql = 'INSERT INTO pedidos(Data_Pedido, ID_Cliente, Total) VALUES (%s, %s, %s)'
    valores = (Data_Pedido, Id_Cliente, Total)
    mycursor.execute(sql,valores)
    Id_Pedido = mycursor.lastrowid
    sql = 'INSERT INTO detalhespedido(ID_Pedido, ID_Produto, Quantidade) VALUES (%s, %s, %s)'
    valores = (Id_Pedido, Id_Produto, Quantidade)
    mycursor.execute(sql,valores)
    sql = 'INSERT INTO vendas(Data, ID_Cliente, MetodoPagamento, Total, ID_Pedido) VALUES(%s, %s, %s, %s, %s)'
    valores = (Data_Pedido, Id_Cliente, MetodoPagamento, Total, Id_Pedido)
    mycursor.execute(sql,valores)
    Id_Venda = mycursor.lastrowid
    sql = 'UPDATE estoque SET Quantidade = Quantidade-%s WHERE ID_Produto = %s'
    valores = (Quantidade, Id_Produto)
    mycursor.execute(sql,valores)
    sql = 'INSERT INTO pagamentos(ID_Venda, Data, Valor) VALUES(%s, %s, %s)'
    valores = (Id_Venda, Data_Pedido, Total)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nValor do pedido: R$', Total)
    print ('\nPedido realizado com sucesso!')
    mycursor.close()

def cadastrarComentario(conbd, Nome, Sobrenome, NomeProduto, Comentario, Avaliacao, Data):
    mycursor = conbd.cursor()
    Id_Produto = acharIDProduto(conbd, NomeProduto)
    Id_Cliente = acharIDCliente(conbd, Nome, Sobrenome)
    sql = 'INSERT INTO comentariosavaliacoes(ID_Produto, ID_Cliente, Comentario, Avaliacao, Data) VALUES(%s, %s, %s, %s, %s)'
    valores = (Id_Produto, Id_Cliente, Comentario, Avaliacao, Data)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('\nComentário cadastrado com sucesso!')
    mycursor.close()