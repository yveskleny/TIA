class Livro:
    def __init__(self, id_livro, titulo, autor):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
    

class Membro:
    def __init(self, nome, id_membro, livros_emprestados):
        self.nome = nome
        self.id_membro = id_membro
        self.livros_emprestados = livros_emprestados
    

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.registro_membros = []
        self.livros_emprestados = []
    

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)
    

    def registrar_membro(self, membro):
        if membro not in self.registro_membros:
            self.registro_membros.append(membro)
        else:
            print("Membro já cadastrado!")


    def emprestar_livro(self, id_livro, id_membro):
        for livro in self.catalogo:
            if livro.id_livro == id_livro:
                print(f"Livro: {livro}. Reservado para: {id_membro}")
                self.livros_emprestados.append((id_livro, id_membro))
                return
        print("Livro não encotrado em nosso catálogo")


    def devolver_livro(self, id_livro, id_membro):
        if (id_livro, id_membro) in self.livros_emprestados:
            self.livros_emprestados.pop((id_livro, id_membro))
            print("Livro devolvido com sucesso.")
        else:
            print("Id do livro ou membro informado de maneira incorreta.")



