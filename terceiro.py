class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# exemplo 
if __name__ == "__main__":
    # cria uma instância da classe Retangulo com base 10 e altura 5
    meu_retangulo = Retangulo(10, 5)
    
    # calcula e imprime a área do retângulo
    area = meu_retangulo.calcular_area()
    print(f"A área do retângulo com base {meu_retangulo.base} e altura {meu_retangulo.altura} é {area}")
