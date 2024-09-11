class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Exemplo 
if __name__ == "__main__":
    # cria uma instância da classe Pessoa com nome e idade
    pessoa = Pessoa("Deborah", 18)
    
    # chama o método falar
    pessoa.falar()
