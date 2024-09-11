class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

# exemplo
if __name__ == "__main__":
    # cria uma instância da classe Carro com marca, modelo e ano
    meu_carro = Carro("Toyota", "Corolla", 2020)
    
    # obtém e imprime os detalhes do carro
    informacoes = meu_carro.detalhes()
    print(informacoes)
