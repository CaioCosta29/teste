import biblioteca
import os


def palavrasMaiuculas(txt): # Deixar todas as palavras maiusculas
    newTxt = ''
    
    for item in txt.split():
        item = item.capitalize()
        newTxt += item + " "
        tamanhoPalava = len(newTxt)
        textoFinal = newTxt[0:tamanhoPalava - 1]
    return textoFinal
os.system('cls')
while True:

    print("""--------MENU--------
Bem vindos a biblioteca do Caio Costa!
Se deseja entrar na area do leitor digite '1'
Se deseja na area dos livros digite '2'
Se deseja entrar na area de emprestar/devolver livro digite '3'
Se deseja encerrar o programa digite '4'""")
    escolha = input()
    os.system('cls')
    match escolha:

        case '1': #Leitor
            print("""--------LEITORES--------
Se quiser cadastrar um leitor digite '1'
Se deseja visualizar um leitor digite '2'
Se deseja visualizar todos os leitores digite '3'
Se deseja atualizar um leitor digite '4'
Se deseja deletar um leitor digite '5'""")
            escolhaLeitor = input()
            match escolhaLeitor:
                case '1': #Cadastrar/CONCLUIDO
                    
                    

                    nomeLeitor = input('Digite seu nome: ')
                    nomeLeitor = palavrasMaiuculas(nomeLeitor)

                    
                    idadeLeitor = input('Digite sua idade: ')

                    ruaLeitor = input('Sua rua: ')
                    ruaLeitor = palavrasMaiuculas(ruaLeitor)

                    numeroRuaLeitor = input('Numero da sua residencia: ')

                    bairroLeitor = input('Seu bairro: ')
                    bairroLeitor = palavrasMaiuculas(bairroLeitor)

                    
                    c = biblioteca.LeitorCRUD()
                    c.cadastrarLeitor(nomeLeitor, idadeLeitor, ruaLeitor, numeroRuaLeitor, bairroLeitor)

                case '2': #VisualizarLeitor/CONCLUIDO
                    
                    visualizarLeitorNome = input('Digite o nome do leitor: ')
                    visualizarLeitorNome = palavrasMaiuculas(visualizarLeitorNome)

                    
                    c = biblioteca.LeitorCRUD()
                    registroLeitor = c.visualizarLeitor(visualizarLeitorNome)
                    
                    
                    
                    print(f'Nome: {registroLeitor[0]}\nIdade: {registroLeitor[1]}\nRua: {registroLeitor[2]}\nNumero: {registroLeitor[3]}\nBairro: {registroLeitor[4]}')
                    
                case '3': #VisualizzarLeitores/CONCLUIDO
                    
                    c = biblioteca.LeitorCRUD()
                    registroGeralLeitor = c.visualizarLeitores()
                    
                    for leitor in registroGeralLeitor:
                        print(f"Nome: {leitor[0]}\nIdade: {leitor[1]}\nRua: {leitor[2]}\nNumero: {leitor[3]}\nBairro: {leitor[4]}\n")
                
                case '4': #Atualizar
                    id_nome = input("Digite o nome do leitor que deseja modificar: ")
                    id_nome = palavrasMaiuculas(id_nome)

                    print("Agora pode modificar")
                    nomeAtualizar = input("nome: ")
                    nomeAtualizar = palavrasMaiuculas(nomeAtualizar)
                    
                    idadeAtualizar = input("Idade: ")


                    ruaAtualizar = input('Sua rua: ')
                    ruaAtualizar = palavrasMaiuculas(ruaAtualizar)

                    numeroRuaAtualizar = input('Numero da sua residencia: ')

                    bairroAtualizar = input('Seu bairro: ')
                    bairroAtualizar = palavrasMaiuculas(bairroAtualizar)

                    
                    c = biblioteca.LeitorCRUD()
                    c.atualizarLeitor(id_nome, nomeAtualizar, idadeAtualizar, ruaAtualizar, numeroRuaAtualizar,bairroAtualizar)
                    

                case '5': #Apagar
                    nomeApagar = input("Digite o nome: ")
                    
                    c = biblioteca.LeitorCRUD()
                    c.excluirLeitor(nomeApagar)
                    
            input('Press ENTER to continue...')
            os.system('cls')
        case '2': #Livro
            print("""--------LIVROS--------
Se quiser cadastrar um livro digite '1'
Se deseja visualizar um livro digite '2'
Se deseja visualizar todos os livros digite '3'
Se deseja atualizar um livro digite '4'
Se deseja deletar um livro digite '5'""")
            escolhaLivro = input()
            match escolhaLivro:
                case '1': #Cadastrar
                    
                    livroTitulo = input('Titulo do livro: ')
                    livroTitulo = palavrasMaiuculas(livroTitulo)
                    

                    livroAutor = input('Autor do livro: ')
                    livroAutor = palavrasMaiuculas(livroAutor)
                    
                    livroGenero = input('Genero do livro: ')
                    livroGenero = palavrasMaiuculas(livroGenero)

                    livroQuantidade = input(f"Quantos '{livroTitulo}' tem? ")

                    a = biblioteca.LivroCRUD()
                    a.cadastrarLivro(livroTitulo, livroAutor, livroGenero, livroQuantidade)

                case '2': #VisualizarLivro
                    
                    verificarTitulo = input('Digite o titulo do livro: ')
                    verificarTitulo = palavrasMaiuculas(verificarTitulo)

                    verificarAutor = input('Digite o nome do autor: ')
                    verificarAutor = palavrasMaiuculas(verificarAutor)

                    a = biblioteca.LivroCRUD()
                    registroLivro = a.visualizarLivro(verificarTitulo, verificarAutor)
                    
                    print(f"Titulo: {registroLivro[0]}\nAutor: {registroLivro[1]}\nGenero: {registroLivro[2]}\nQuantidade: {registroLivro[3]}")
                    
                case '3': #VisualizarLivros
                    
                    a = biblioteca.LivroCRUD()
                    registrosGeralLivro = a.visualizarLivros()

                    for livro in registrosGeralLivro:
                        print(f"Titulo: {livro[0]}\nAutor: {livro[1]}\nGenero: {livro[2]}\nQuantidade: {livro[3]}\n")
                
                case '4': #Atualizar
                    id_title = input("Digite o titulo do livro que deseja modificar: ")
                    id_autor = input(f"Digite o nome do autor de {id_title}: ")

                    print("Agora para modificar")
                    tituloAtualizar = input("Titulo: ")
                    autorAtualizar = input("Autor: ")
                    generoAtualizar = input("Genero: ")
                    quantidadeAtualizar = input("Quantidade: ")

                    a = biblioteca.LivroCRUD()
                    a.atualizarLivro(id_title, id_autor, tituloAtualizar, autorAtualizar, generoAtualizar, quantidadeAtualizar)

                case '5': #Apagar
                    tituloExcluir = input("Titulo: ")
                    autorExcluir = input("Autor: ")

                    a = biblioteca.LivroCRUD()
                    a.excluirLivro(tituloExcluir, autorExcluir)
        
            input('Press ENTER to continue...')
            os.system('cls')
        case '3': #Emprestimo/Devolver
            print("""--------EMPRÉSTIMO--------
Digite '1' para emprestimo
Digite '2' para devolver
Digite '3' para visualizar todos os emprestimos
Digite '4' para visualizar um emprestimo especifico""")
            escolha = input()

            match escolha:
                case '1': #Emprestimo
                    emprestimoTitulo = input(('Titulo: '))
                    emprestimoTitulo = palavrasMaiuculas(emprestimoTitulo)

                    emprestimoAutor = input(("Autor: "))
                    emprestimoAutor = palavrasMaiuculas(emprestimoAutor)

                    emprestimoNome = input(("Nome: "))
                    emprestimoNome = palavrasMaiuculas(emprestimoNome)                 

                    x = biblioteca.EmprestimoCRUD()
                    x.emprestarLivro(emprestimoTitulo, emprestimoAutor, emprestimoNome)

                case '2': #Devolver
                    nomeDevolver = input("Digite o nome do leitor: ")
                    nomeDevolver = palavrasMaiuculas(nomeDevolver)

                    tituloDevolver = input("Digite o titulo: ")
                    tituloDevolver = palavrasMaiuculas(tituloDevolver)

                    autorDevolver = input("Digite o autor: ")
                    autorDevolver = palavrasMaiuculas(autorDevolver)
                    
                    x = biblioteca.EmprestimoCRUD()
                    x.devolverLivro(nomeDevolver, tituloDevolver, autorDevolver)
                
                case '3': #visualizar todos os emprestimos
                    x = biblioteca.EmprestimoCRUD()
                    registroEmprestimos = x.visualizarEmprestimos()

                    for emprestimo in registroEmprestimos:
                        print(f"Leitor: {emprestimo[0]}\nTitulo: {emprestimo[1]}\nAutor: {emprestimo[2]}\n")

                case '4': #visualizar um emprestimo
                    nomeVisualizarEmprestimo = input("Digite o nome: ")
                    nomeVisualizarEmprestimo = palavrasMaiuculas(nomeVisualizarEmprestimo)

                    tituloVisualizarEmprestimo = input("Digite o titulo: ")
                    tituloVisualizarEmprestimo = palavrasMaiuculas(tituloVisualizarEmprestimo)

                    autorVisualizarEmprestimo = input("Digite o autor: ")
                    autorVisualizarEmprestimo = palavrasMaiuculas(autorVisualizarEmprestimo)

                    x = biblioteca.EmprestimoCRUD()
                    registroEmprestimo = x.visualizarDetalhesDoLivroEmprestado(nomeVisualizarEmprestimo, tituloVisualizarEmprestimo, autorVisualizarEmprestimo)
                    os.system("cls")
                    print(f"Leitor: {registroEmprestimo[0]}\nTitulo: {registroEmprestimo[1]}\nAutor: {registroEmprestimo[2]}\n")


            input('Press ENTER to continue...')
            os.system('cls')
            
        case '4': #Parar o programa
            break