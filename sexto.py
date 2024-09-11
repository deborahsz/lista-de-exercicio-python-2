class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

# Exemplo
if __name__ == "__main__":
    # cria uma instância da classe Produto com nome, preço e quantidade
    produto = Produto("Camiseta", 29.90, 3)
    
    # calcula e imprime o valor total do produto
    total = produto.calcular_total()
    print(f"O valor total de {produto.nome} é R${total:.2f}")
