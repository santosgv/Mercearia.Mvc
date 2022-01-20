from Dao import CategoriaDao
from Models import Categoria

class ControllerCategoria:
    def CadastrarCatergoria(self, novaCategoria):
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

        if len(categoria) ==0 :
            print('Categoria vazia')
            return 0

        for i in categoria:
            print(f'Caregoria : {i.categoria}')



