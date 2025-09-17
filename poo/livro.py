class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_informacoes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}"

    def lendo_livro(self):
        return f"Lendo o livro: {self.titulo} de {self.autor}"                                                           


livro1 = Livro("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005)
livro2 = Livro("Percy Jackson e o Mar de Monstros", "Rick Riordan", 2006)
livro3 = Livro("Percy Jackson e a Maldição do Titã", "Rick Riordan", 2007)

print(livro1.exibir_informacoes())  