class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

# Exemplo
if __name__ == "__main__":
    # cria uma instância da classe Aluno com nome e uma lista de notas
    aluno = Aluno("Deborah", [7.5, 8.0, 6.5, 9.0])
    
    # calcula e imprime a média das notas do aluno
    media = aluno.calcular_media()
    print(f"A média das notas de {aluno.nome} é {media:.2f}")
