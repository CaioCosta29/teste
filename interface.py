import biblioteca


def palavrasMaiuculas(txt): # Deixar todas as palavras maiusculas
    newTxt = ''
    
    for item in txt.split():
        item = item.capitalize()
        newTxt += item + " "
        tamanhoPalava = len(newTxt)
        textoFinal = newTxt[0:tamanhoPalava - 1]
    return textoFinal

while True:


    
    escolha = input("""Bem vindos a biblioteca do Caio Costa!\nSe deseja entrar na area do leitor digite '1'\nSe deseja na area dos livros digite '2'\nSe deseja entrar na area de emprestar/devolver livro digite '3'\nSe deseja encerrar o programa digite '4'\n""")
    match escolha:
        case '1': #Leitor
             
            escolhaLeitor = input("""Se quiser cadastrar um leitor digite '1'
Se deseja visualizar um leitor digite '2'
Se deseja visualizar todos os leitores digite '3'
Se deseja atualizar um leitor digite '4'
Se deseja deletar um leitor digite '5'\n""")
            match escolhaLeitor:
                case '1': #Cadastrar/CONCLUIDO
                    
                    enderecoLeitor = list()

                    nomeLeitor = input('Digite seu nome: ')
                    nomeLeitor = palavrasMaiuculas(nomeLeitor)

                    
                    idadeLeitor = input('Digite sua idade: ')

                    ruaLeitor = input('Sua rua: ')
                    ruaLeitor = palavrasMaiuculas(ruaLeitor)

                    numeroRuaLeitor = input('Numero da sua residencia: ')

                    bairroLeitor = input('Seu bairro: ')
                    bairroLeitor = palavrasMaiuculas(bairroLeitor)

                    
                    enderecoLeitor.append(ruaLeitor)
                    enderecoLeitor.append(numeroRuaLeitor)
                    enderecoLeitor.append(bairroLeitor)
                    
                    c = biblioteca.LeitorCRUD()
                    c.cadastrarLeitor(nomeLeitor, idadeLeitor, enderecoLeitor)

                case '2': #VisualizarLeitor/CONCLUIDO
                    
                    visualizarLeitorNome = input('Digite o nome do leitor: ')
                    visualizarLeitorNome = palavrasMaiuculas(visualizarLeitorNome)

                    
                    c = biblioteca.LeitorCRUD()
                    print(c.visualizarLeitor(visualizarLeitorNome))
                
                case '3': #VisualizzarLeitores/CONCLUIDO
                    
                    c = biblioteca.LeitorCRUD()
                    print(c.visualizarLeitores())
                
                case '4': #Atualizar
                    id_nome = input("Digite o nome do leitor que deseja modificar: ")
                    id_nome = palavrasMaiuculas(id_nome)

                    nomeAtualizar = input("nome: ")
                    nomeAtualizar = palavrasMaiuculas(nomeAtualizar)
                    
                    idadeAtualizar = input("Idade: ")

                    enderecoAtualizar = []

                    ruaAtualizar = input('Sua rua: ')
                    ruaAtualizar = palavrasMaiuculas(ruaAtualizar)

                    numeroRuaAtualizar = input('Numero da sua residencia: ')

                    bairroAtualizar = input('Seu bairro: ')
                    bairroAtualizar = palavrasMaiuculas(bairroAtualizar)

                    
                    enderecoAtualizar.append(ruaAtualizar)
                    enderecoAtualizar.append(numeroRuaAtualizar)
                    enderecoAtualizar.append(bairroAtualizar)

                    

                    c = biblioteca.LeitorCRUD()
                    c.atualizarLeitor(id_nome, nomeAtualizar, idadeAtualizar, enderecoAtualizar)
                    

                case '5': #Apagar
                    nomeApagar = input("Digite o nome: ")
                    sobrenomeApagar = input("Digite o sobrenome: ") 

                    c = biblioteca.LeitorCRUD()
                    c.excluirLeitor(nomeApagar, sobrenomeApagar)
                    

        case '2': #Livro
            
            escolhaLivro = input("""Se quiser cadastrar um livro digite '1'
Se deseja visualizar um livro digite '2'
Se deseja visualizar todos os livros digite '3'
Se deseja atualizar um livro digite '4'
Se deseja deletar um livro digite '5'""")
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

                    verificarAutor = input('Digite o nome do autor')
                    verificarAutor = palavrasMaiuculas(verificarAutor)

                    a = biblioteca.LivroCRUD()
                    a.visualizarLivro(verificarTitulo, verificarAutor)
                    
                case '3': #VisualizarLivros
                    
                    a = biblioteca.LivroCRUD()
                    a.visualizarLivros()
                
                case '4': #Atualizar
                    id_title = input("Digite o titulo do livro que deseja modificar: ")
                    id_autor = input(f"Digite o nome do autor de {id_title}")

                    print("Agora para modificar")
                    tituloAtualizar = input("Titulo: ")
                    autorAtualizar = input("Autor: ")
                    generoAtualizar = input("Genero: ")
                    quantidadeAtualizar = input("Quantidade: ")

                    a = biblioteca.LivroCRUD()
                    a.atualizarLivro(id_title, id_autor, tituloAtualizar, autorAtualizar, generoAtualizar, quantidadeAtualizar)

                case '5': #Apagar
                    tituloExcluir = input("titulo: ")
                    autorExcluir = input("autor: ")

                    a = biblioteca.LivroCRUD()
                    a.excluirLivro(tituloExcluir, autorExcluir)
        case '3': #Emprestimo/Devolver
            escolha = input("Digite 1 para emprestimo\nDigite 2 para devolver:  ")

            match escolha:
                case '1': #Emprestimo
                    emprestimoTitulo = input(('Titulo: '))
                    emprestimoAutor = input(("Autor: "))
                    emprestimoNome = input(("Nome: "))
                    emprestimoSobrenome = input(("Sobrenome: "))                    

                    x = biblioteca.EmprestimoCRUD()
                    x.emprestarLivro(emprestimoTitulo, emprestimoAutor, emprestimoNome, emprestimoSobrenome)

                case '2': #Devolver
                    nomeDevolver = input("Digite o nome: ")
                    sobrenomeDevolver = input("Digite o sobrenome: ")
                    tituloDevolver = input("Digite o titulo: ")
                    autorDevolver = input("Digite o autor: ")

                    x = biblioteca.EmprestimoCRUD()
                    x.devolverLivro(nomeDevolver, sobrenomeDevolver, tituloDevolver, autorDevolver)
                
                #case '3': #visualizar
                    #x = biblioteca.EmprestimoCRUD()
                    #x.visualizarEmprestimos()


            

        case '4': #Parar o programa
            break