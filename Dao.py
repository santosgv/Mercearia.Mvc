from Models import Categoria, Venda , Produtos , Estoque, Fornecedor, Pessoa , Funcionario

class CategoriaDao:
    @classmethod
    def salvar(cls, categoria):
        with open('Categoria.txt','a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Categoria.txt', 'r') as arq:
            cls.categoria= arq.readlines()
        cls.categoria = list( map(lambda x:x.replace('\n',''), cls.categoria))

        cat=[]

        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

class VendaDao:
    @classmethod
    def salvar(cls, venda : Venda):
        with open('Venda.txt' , 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|" +
                           venda.itensVendidos.preco + "|"+
                           venda.itensVendidos.categoria + "|" +
                           venda.vendedor + "|" +
                           venda.comprador + "|" +
                           str(venda.quantidadeVendida) + "|" +
                           venda.data)

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Venda.txt', 'r') as arq:
            cls.venda=arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend=[]

        for i in cls.venda:
            vend.append(Venda(Produtos( i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend

class EstoqueDao:
    @classmethod
    def salvar(cls, produto : Produtos , quantidade):
        with open('Estoque.txt' , 'a') as arq:
            arq.writelines(produto.nome + "|" +
                           produto.preco + "|" +
                           produto.categoria + "|" +
                           str(quantidade))

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Estoque.txt', 'r') as arq:
            cls.estoque=arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        estoq=[]

        if len(cls.estoque) > 0:
            for i in cls.estoque:
                estoq.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))

        return estoq

class FornecedorDao:
    @classmethod
    def salvar(cls, fornecedor : Fornecedor):
        with open('Fornecedor.txt' , 'a') as arq:
            arq.writelines(fornecedor.nome + "|" +
                           fornecedor.cnpj + "|" +
                           fornecedor.telefone + "|" +
                           fornecedor.categoria)

            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open('Fornecedor.txt', 'r') as arq:
            cls.fornecedor=arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forneced=[]

        for i in cls.fornecedor:
            forneced.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forneced

class PessoaDao:
    @classmethod
    def salvar(cls, pessoa :Pessoa):
        with open('Clientes.txt' , 'a') as arq:
            arq.writelines(pessoa.nome + "|" +
                           pessoa.telefone + "|" +
                           pessoa.cpf + "|" +
                           pessoa.email + "|" +
                           pessoa.endereco)

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Clientes.txt', 'r') as arq:
            cls.clientes=arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes=[]

        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return clientes

class FuncionarioDao:
    @classmethod
    def salvar(cls, funcionario :Funcionario):
        with open('Funcionarios.txt' , 'a') as arq:
            arq.writelines(funcionario.clt + "|" +
                           funcionario.nome + "|" +
                           funcionario.telefone + "|" +
                           funcionario.cpf + "|" +
                           funcionario.email + "|" +
                           funcionario.endereco)

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Funcionarios.txt', 'r') as arq:
            cls.funcionarios=arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcionarios=[]

        for i in cls.funcionarios:
            funcionarios.append(Funcionario(i[0], i[1], i[2] , i[3] , i[4], i[5]))

        return funcionarios