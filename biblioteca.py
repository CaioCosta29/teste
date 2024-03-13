class LivroCRUD:
    def cadastrarLivro(self, titulo, autor, genero, quantidade):

        with open("cadastro_livro.txt", "a") as cad:
            cad.write(f"{titulo}&&{autor}&&{genero}&&{quantidade}\n")

    def cadastrarLivros(self, livros):
        with open("cadastro_livro.txt", "w") as cad:
            cad.write("")

        for livro in livros:
            self.cadastrarLivro(livro[0], livro[1], livro[2], livro[3])

    def visualizarLivros(self):
        result = []
        with open("cadastro_livro.txt", "r") as cad:
            livros = cad.readlines()
            for livro in livros:
                result.append(livro.split("&&"))
            
            return result
        
    def visualizarLivro(self, titulo, autor):
       livros = self.visualizarLivros()

       for linha in livros:
           #livroSeparado = linha.split("&&")
           if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
               return linha
    
    def atualizarLivro(self, id_title, id_autor, title, autor, genero, quantidade): #problem aqui
        livros = self.visualizarLivros()
        print(livros)
        for linha in livros:
            print(linha)
            if f"{id_title}, {id_autor}" in f"{linha[0]}, {linha[1]}":
                linha[0] = title
                linha[1] = autor
                linha[2] = genero
                linha[3] = quantidade
        
        self.cadastrarLivros(livros)

    def excluirLivro(self, titulo, autor):
        livros = self.visualizarLivros()

        for linha in livros:
            if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
                livros.remove(linha)
        
        self.cadastrarLivros(livros)

class LeitorCRUD:    
    def cadastrarLeitor(self, nome="", idade=0, endereco=""): #concluido
        with open("cadastro_leitor.txt", "a") as cad:
            cad.write(f"{nome}&&{idade}&&{endereco}\n")

    def cadastrarLeitores(self, leitores=[]): #concluido
        with open("cadastro_leitor.txt", "w") as cad:
            cad.write("")
        
        for leitor in leitores:
            print(leitor[0])
            print(leitor[1])
            print(leitor[2])
            self.cadastrarLeitor(leitor[0], leitor[1], leitor[2])

    def visualizarLeitores(self): #concluido
        result = []
        with open("cadastro_leitor.txt", "r") as cad:
            leitores = cad.readlines()
            for leitor in leitores:
                result.append(leitor.split("&&"))   
        return result

    def visualizarLeitor(self, nome): #concluido
        leitores = self.visualizarLeitores()
        
        for linha in leitores:
            #leitorSeparado = linha.split()
            if f"{nome}" in linha[0]:
                
                return linha

    def atualizarLeitor(self, id_nome, nome, idade, endereco): #problema aqui
        leitores = self.visualizarLeitores()
        
        for linha in leitores:
            if f"{id_nome}" in linha[0]:
                linha[0] = nome
                linha[1] = idade
                linha[2] = endereco
                
            
        
        self.cadastrarLeitores(leitores)

    def excluirLeitor(self, nome, sobrenome):
        leitores = self.visualizarLeitores()
        
        for linha in leitores:
            if f"{nome} {sobrenome}" in linha[0]:
                leitores.remove(linha)
        
        self.cadastrarLeitores(leitores)


class EmprestimoCRUD:
    def __init__(self):
        self.leitorControle = LeitorCRUD()
        self.livroControle = LivroCRUD()
        


    def emprestarLivro(self, titulo, autor, nome, sobrenome):
        livros = self.livroControle.visualizarLivros()
        leitores = self.leitorControle.visualizarLeitores()


        verificarLeitor = False
        verificarLivro = False


        for item in leitores:
            if f"{nome} {sobrenome}" in item:
                
                verificarLeitor = True

        for indice in livros:
            if f"{titulo}, {autor}" in f"{indice[0]}, {indice[1]}":
                
                verificarLivro = True

        if verificarLivro == True and verificarLeitor == True:
            for linha in livros:
                if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
                    linha[3] = int(linha[3]) - 1
                    
            

            self.livroControle.cadastrarLivros(livros)

            with open("emprestimo_livro.txt", "a") as cad:
                cad.write(f"{nome} {sobrenome}&&{titulo}&&{autor}\n")


    def cadastrarEmprestimo(self, nomeCompleto, titulo, autor):
        with open("emprestimo_livro.txt", "a") as cad:
            cad.write(f"{nomeCompleto}&&{titulo}&&{autor}")

        
    def cadastrarEmprestimos(self, emprestimos=[]):
        with open("emprestimo_livro.txt", "w") as cad:
            cad.write("")
            
            for emprestimo in emprestimos:
                self.cadastrarEmprestimo(emprestimo[0], emprestimo[1], emprestimo[2])
    
    def visualizarEmprestimos(self):
        result = []
        with open("emprestimo_livro.txt", "r") as cad:
            listaEmprestimo = cad.readlines()
            for emprestimo in listaEmprestimo:
                result.append(emprestimo.split("&&"))
            return result
        

    def devolverLivro(self, nome, sobrenome, titulo, autor):
        livros = self.livroControle.visualizarLivros()


        listaEmprestimo = self.visualizarEmprestimos()
        print(listaEmprestimo)
        

        for item in listaEmprestimo: #excluir do arquivo txt
            
            if f"{nome} {sobrenome}" in f"{item[0]}" and f"{titulo}" in f"{item[1]}":
                print(listaEmprestimo)
                listaEmprestimo.remove(item)
                print(listaEmprestimo)

                self.cadastrarEmprestimos(listaEmprestimo)

                
                for linha in livros:
                    print(linha)
                    if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
                        
                        linha[3] = int(linha[3]) + 1

                self.livroControle.cadastrarLivros(livros)
                

        
    def visualizarDetalhesDoLivroEmprestado(self, nome, sobrenome, titulo):
        emprestimo = self.visualizarEmprestimos()

        for linha in emprestimo:
            #emprestimoSeparado = linha.split("&&")
            if f"{nome} {sobrenome}" in linha[0]:
                return linha