from Dao import CategoriaDao, EstoqueDao, VendaDao , FornecedorDao, FuncionarioDao, PessoaDao
from Models import Categoria, Produtos , Estoque , Venda , Fornecedor, Funcionario ,Pessoa
from datetime import datetime

class ControllerCategoria:
    def cadastrarCatergoria(self, novaCategoria):
        existe = False
        x = CategoriaDao.ler()
        for i in x:
            if i.categoria ==novaCategoria:
                existe = True

        if not existe:
            CategoriaDao.salvar(novaCategoria)
            print('Categoria Cadastrada com sucesso !!!')
        else:
            print('Ja existe uma caregoria com este nome cadastrado')

    def removerCategoria(self, categoriaRemover):
        x = CategoriaDao.ler()
        cat = list(filter(lambda x : x.categoria == categoriaRemover,x))

        if len(cat) <=0:
            print('A categoria nao existe')

        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')

            with open('Categoria.txt','w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')


    def alterarCategoria(self, caregoriaAlterar, categoriaAlterada):
        x = CategoriaDao.ler()

        cat = list(filter(lambda  x : x.categoria == caregoriaAlterar, x))
        if len(cat) > 0:
            cat1= list(filter(lambda x:x.categoria ==categoriaAlterada,x))
            if len(cat1) == 0:
                x= list(map(lambda x : Categoria(categoriaAlterada) if (x.categoria == caregoriaAlterar) else(x),x))
                print('Alterado com sucesso')
            else:
                print('A categoria para qual deseja alterar ja existe')
        else:
            print('A categoria que deseja alterar nao existe')

        with open('Categoria.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categoria= CategoriaDao.ler()

        if len(categoria) == 0 :
            print('Categoria vazia')
            return 0

        for i in categoria:
            print(f'Caregoria : {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco,categoria, quantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()

        cat=list(filter(lambda  x:x.categoria == categoria,y))
        est = list(filter(lambda x:x.produto.nome == nome, x))

        if len(cat) > 0:
            if len(est) ==0:
                produto = Produtos(nome , preco,categoria)
                EstoqueDao.salvar(produto ,quantidade)
                print('Produto salvo com sucesso')
            else:
                print('Produto ja existe em estoque')
        else:
            print('Categoria inexistente')

    def removerProduto(self, nome):
        x = EstoqueDao.ler()

        est= list(filter(lambda x:x.produto.nome == nome,x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto removido com Sucesso')
        else:
            print('O produto que deseja Remover nao existe')

        with open('Estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" +
                               i.produto.preco + "|" +
                               i.produto.categoria + "|" +
                               str(i.quantidade))

                arq.writelines('\n')

    def alterarProduto(self, nomeAltera, novoNome , novoPreco ,novaCategoria ,novaQuantidade):
        x=EstoqueDao.ler()
        y=CategoriaDao.ler()
        h=list(filter(lambda x:x.categoria ==novaCategoria , y))
        if len(h) > 0:
            est = list(filter(lambda x:x.produto.nome == nomeAltera, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0 :
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco , novaCategoria), novaQuantidade) if(x.produto.nome == nomeAltera) else(x),x))
                    print('Produto alterado com sucesso')
                else:
                    print('Produto ja Cadastrado')
            else:
                print('O produto que deseja alterar nao existe')
        else:
            print('A categoria que deseja alterar nao existe')

        with open('Estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" +
                               i.produto.preco + "|" +
                               i.produto.categoria + "|" +
                               str(i.quantidade))

                arq.writelines('\n')

    def mostraEstoque(self):
        estoque= EstoqueDao.ler()

        if len(estoque) == 0:
            print('Estoque vazio')

        else:
            for i in estoque:
                print(f'''
                    =========== Produto ===========
                    Nome       .: {i.produto.nome}
                    Preco      .: {i.produto.preco}
                    Caregoria  .: {i.produto.categoria}
                    Quantidade .: {i.quantidade}
                    ===============================
                ''')

class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor , comprador , quantidadeVenda):
        '''

        :param nomeProduto: Nome do Produto
        :param vendedor: Nome do Vendedo
        :param comprador: Nome do Comprador
        :param quantidadeVenda: QUantidade Vendida

        :return: 1 Produto nao existe
        :return: 2  Sem quantidade no estoque
        :return: 3 Produto cadaastrado com Sucesso
        '''
        x= EstoqueDao.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x :
            if existe == False:
                if i.produto.nome ==nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVenda:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int (quantidadeVenda)

                        vendido= Venda(Produtos(i.produto.nome , i.produto.preco , i.produto.categoria ), vendedor, comprador, quantidadeVenda)

                        valorCompra = (int(i.produto.preco) * int(quantidadeVenda) )

                        VendaDao.salvar(vendido)

            temp.append([Produtos(i.produto.nome , i.produto.preco , i.produto.categoria),i.quantidade])

        arq= open('Estoque.txt', 'w')
        arq.write("")
        for i in temp:
            with open('Estoque.txt','a') as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco +"|" + i[0].categoria + "|" + str(i[1]))
                arq.writelines('\n')
        if existe == False:
            print('Produto nao existe')
            return 1
        elif not quantidade:
            print('A quantidade vendida nao contem no estoque')
            return 2
        else:
            return 3, valorCompra

    def relatorioProdutos(self):
        vendas =VendaDao.ler()
        produto = []
        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade= i.quantidadeVendida
            tamanho = list(filter(lambda  x: x['produto'] == nome , produto))
            if len(tamanho) > 0 :
                produto = list(map(lambda x:{'produto':nome ,'quantidade': int(x['quantidade'])+ int(quantidade)}
                                   if (x['produto']==nome) else(x),produto))
            else:
                produto.append({'produto': nome , 'quantidade': int(quantidade)})

        ordenado=sorted(produto,key=lambda  k: k['quantidade'],reverse=True)
        a=1
        for i in ordenado:
            print(f'''
            ============= PRODUTO [{a}] ================
            Esse Sao os Produtos Mais vendidos
            Produto .: {i['produto']}
            Produto .: {i['quantidade']}
            ''')
            a += 1

    def mostrarVenda(self, dataInicio, dataFim):
        vendas = VendaDao.ler()
        datainicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataFim1 = datetime.strptime(dataFim, '%d/%m/%Y')

        vendasSelecionada=list(filter(lambda x:datetime.strptime(x.data,"%d/%m/%Y") >= datainicio1 and datetime.strptime(x.data,"%d/%m/%Y") <= dataFim1, vendas))

        count = 1
        total = 0
        for i in vendasSelecionada:
            print(f'''
            ============= Vendas [{count}] =============
            Nome .............: {i.itensVendidos.nome}
            Data .............: {i.data}
            Quantidade .......: {i.quantidadeVendida}
            Comprador ........: {i.comprador}
            Vendedor .........: {i.vendedor}
            ''')
            total +=int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            count += 1

        print(f'Quantidade Total Vendido {total}')

class ControllerFornecedor:

    def cadastrarFornecedor(self,nome ,cnpj ,telefone, categoria):
        '''

        :param nome: Nome do Fornecedor
        :param cnpj: CNPJ do fornecedor
        :param telefone: Telefone do Fornecedor
        :param categoria: Categoria referente ao cadastrado no sistema
        :return: 1 para erro ao cadastrar
        :return: 2 Cadastro realizado com sucesso
        '''
        x = FornecedorDao.ler()
        listacnpj =list(filter(lambda x:x.cnpj == cnpj, x))
        listatelefone= list(filter(lambda x:x.telefone == telefone, x))

        if len(listacnpj) > 0:
            print('O CNPJ ja existe no sistema')
            return 1
        elif len(listatelefone) > 0:
            print('O telefone ja existe no sistema')
            return 1
        else:
            if len(cnpj) ==14 and len(telefone) <=11 and len(telefone) > 10:
                FornecedorDao.salvar(Fornecedor(nome ,cnpj ,telefone, categoria))
                print('Cadastrado com Sucesso')
                return 2
            else:
                print('Digite um CNPJ ou telefone Valido')
                return 1

    def removerFornecedor(self,cnpj):
        x =FornecedorDao.ler()
        fornecedor=list(filter(lambda x:x.cnpj == cnpj,x))

        if len(fornecedor) > 0:
            for i in range(len(x)):
                if x[i].cnpj == cnpj:
                    del x[i]
                    print('Fornecedor removido com Sucesso')
                    break
        else:
            print('Nao foi encontrado Fornecedor Com este CNPJ')

        with open('Fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" +
                               i.cnpj + "|" +
                               i.telefone + "|" +
                               i.categoria)

                arq.writelines('\n')

    def alterarFornecedor(self,novoNome,cnpjAlterar,novoCnpj,novoTelefone,novaCategoria):
        x = FornecedorDao.ler()
        alteraFornecerdo = list(filter(lambda x:x.cnpj == cnpjAlterar, x))

        if len(alteraFornecerdo) > 0:
            alteraTelefone = list(filter(lambda  x: x.cnpj == novoCnpj,x ))
            if len(alteraTelefone) == 0:
                x = list(map(lambda x: Fornecedor(novoNome,novoCnpj,novoTelefone,novaCategoria) if (x.cnpj == cnpjAlterar) else (x), x))
                print('Alterado com sucesso')
            else:
                print('O Telefone ja existete em nossa base')
        else:
            print('CNPJ do fornecedor nao encontrado')

        with open('Fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" +
                               i.cnpj + "|" +
                               i.telefone + "|" +
                               i.categoria)

                arq.writelines('\n')

    def mostrarFornecedor(self):
        fornecedor = FornecedorDao.ler()

        if len(fornecedor) == 0:
            print('A lista de fornecedo esta vazia')
        else:
            for i in fornecedor:
                print(f'''
                =========== Fornecedor ==============
                Fornecedor .....: {i.nome}
                CNPJ  ..........: {i.cnpj}
                TELEFONE .......: {i.telefone}
                Categoria ......: {i.categoria}
                =====================================
                ''')

class ControllerPessoa:
    def cadastrarPessoa(self, nome ,telefone,cpf,email, endereco):
        x = PessoaDao.ler()
        pessoa = list(filter(lambda x:x.cpf == cpf,x))

        if len(pessoa) > 0 :
            print('Ja existe uma pessoa com este CPF cadastrado no sistema')
        else:
            if len(cpf) < 11 :
                print('Digite um CPF valido ')

            elif len(telefone) < 9:
                print('Digite um telefone Valido')
            else:
                PessoaDao.salvar(Pessoa(nome,telefone,cpf,email, endereco))
                print('Pessoa Salva com sucesso')

    def removerPessoa(self,cpfremover):
        x =PessoaDao.ler()
        pessoa = list(filter(lambda x : x.cpf == cpfremover, x))

        if len(pessoa) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpfremover:
                    del x[i]
                    print('Removido com Sucesso')
                    break
        else:
            print('Nao foi Encontrado um Cliente com este CPF')

        with open('Clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" +
                               i.telefone + "|" +
                               i.cpf + "|" +
                               i.email + "|" +
                               i.endereco)

                arq.writelines('\n')

    def alterarPessoa(self,nomeAlterar,novoNome,novoTelefone,novoCpf,novoEmail,novoEndereco):
        x = PessoaDao.ler()
        alteraPessoa = list(filter(lambda x:x.nome == nomeAlterar, x))

        if len(alteraPessoa) > 0:
            x = list(map(lambda x: Pessoa(novoNome,novoTelefone,novoCpf,novoEmail,novoEndereco) if (x.nome == nomeAlterar) else (x), x))
            print('Alterado com sucesso')
        else:
            print('Nome do Cliente nao encontrado')

        with open('Clientes.txt', 'w') as arq:
            for i in x:
                for i in x:
                    arq.writelines(i.nome + "|" +
                                   i.telefone + "|" +
                                   i.cpf + "|" +
                                   i.email + "|" +
                                   i.endereco)

                    arq.writelines('\n')

    def mostraPessoa(self):
        pessoa =PessoaDao.ler()

        if len(pessoa) ==0:
            print('Sem CLientes Cadastrados')
        else:
            for i in pessoa:
                print(f'''
                =========== CLientes ==============
                Nome .............: {i.nome}
                Telefone .........: {i.telefone}
                CPF ..............: {i.cpf}
                Email ............: {i.email}
                Endereco .........: {i.endereco}
                ===================================
                ''')

class ControllerFuncionario:
    def cadastrarFuncionario(self ,clt,nome,telefone,cpf,email,endereco):
        x= FuncionarioDao.ler()

        funcionario = list(filter(lambda x: x.cpf == cpf, x))

        if len(funcionario) > 0 :
            print('Ja existe uma pessoa com este CPF cadastrado no sistema')
        else:
            if len(cpf) < 11 :
                print('Digite um CPF valido ')

            elif len(telefone) < 9:
                print('Digite um telefone Valido')
            else:
                FuncionarioDao.salvar(Funcionario(clt,nome,telefone,cpf,email, endereco))
                print('Pessoa Salva com sucesso')

    def removerFuncionario(self,cpfremover):

        x =FuncionarioDao.ler()
        funcionario = list(filter(lambda x : x.cpf == cpfremover, x))

        if len(funcionario) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpfremover:
                    del x[i]
                    print('Removido com Sucesso')
                    break
        else:
            print('Nao foi Encontrado um Funcionario com este CPF')

        with open('Funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" +
                               i.nome + "|" +
                               i.telefone + "|" +
                               i.cpf + "|" +
                               i.email + "|" +
                               i.endereco)

                arq.writelines('\n')

    def alterarFuncionario(self,cltAltera,novaClt,novoNome,novoTelefone,novoCpf,novoEmail,novoEndereco):
        x = FuncionarioDao.ler()
        alteraFuncionario = list(filter(lambda x:x.clt == cltAltera, x))

        if len(alteraFuncionario) > 0:
            x = list(map(lambda x: Funcionario(novaClt,novoNome,novoTelefone,novoCpf,novoEmail,novoEndereco) if (x.clt == cltAltera) else (x), x))
            print('Alterado com sucesso')
        else:
            print('a CLT do Funcionario nao encontrado')

        with open('Funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" +
                               i.nome + "|" +
                               i.telefone + "|" +
                               i.cpf + "|" +
                               i.email + "|" +
                               i.endereco)

                arq.writelines('\n')

    def mostrarFuncionario(self):
        funcionario = FuncionarioDao.ler()

        if len(funcionario) == 0:
            print('A Lista de Funcionario esta vazia')
        else:
            for i in funcionario:
                print(f'''
                    =========== Funcionario ==============
                    Nome ...........: {i.nome}
                    Telefone .......: {i.telefone}
                    CPF ............: {i.cpf}
                    Email ..........: {i.email}
                    Endereco .......: {i.endereco}
                    ======================================
                    ''')