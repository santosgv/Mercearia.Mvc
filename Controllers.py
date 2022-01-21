from Dao import CategoriaDao, EstoqueDao
from Models import Categoria, Produtos , Estoque

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
            est= list(filter(lambda x:x.produto.nome == nomeAltera, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0 :
                    pass ## to aqui
                else:
                    print('Produto ja Cadastrado')
            else:
                print('O produto que deseja alterar nao existe')
        else:
            print('A categoria que deseja alterar nao existe')