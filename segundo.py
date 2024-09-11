class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

# exemplo 
if __name__ == "__main__":
    # cria uma instância da classe Livro com título e autor
    meu_livro = Livro("1984", "George Orwell")
    
    # obtém e imprime os detalhes do livro
    informacoes = meu_livro.detalhes()
    print(informacoes)
