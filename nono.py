class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Exemplo 
if __name__ == "__main__":
    # cria uma instância da classe Triangulo com os comprimentos dos lados
    meu_triangulo = Triangulo(3, 4, 5)
    
    # calcula e imprime o perímetro do triângulo
    perimetro = meu_triangulo.calcular_perimetro()
    print(f"O perímetro do triângulo é {perimetro}")
