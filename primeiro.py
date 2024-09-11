import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)

if __name__ == "__main__":
    
    meu_circulo = Circulo(5)
    
    area = meu_circulo.calcular_area()
    print(f"A área do círculo com raio {meu_circulo.raio} é {area:.2f}")
