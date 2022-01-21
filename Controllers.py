from Dao import CategoriaDao, EstoqueDao, VendaDao
from Models import Categoria, Produtos , Estoque , Venda

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
        cat = list(filter(lambda x : x.categoria ==categoriaRemover,x))

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
            print(f'Valor da compra {valorCompra}')
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
            ==============PRODUTO [{a}]=================
            Esses Sao os Produtos Mais vendidos
            Produto .: {i['produto']}
            Produto .: {i['quantidade']}
            ''')
            a += 1

a=ControllerVenda()
a.relatorioProdutos()