class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        if percentual < 0:
            print("O percentual de aumento não pode ser negativo.")
            return
        
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"O salário de {self.nome} foi aumentado em {percentual}%.")

    def exibir_detalhes(self):
        return f"Nome: {self.nome}\nSalário: R${self.salario:.2f}\nCargo: {self.cargo}"

# Exemplo 
if __name__ == "__main__":
    # cria uma instância da classe Funcionario com nome, salário e cargo
    funcionario = Funcionario("Deborah", 3000.00, "Analista de Sistemas")
    
    # exibe os detalhes iniciais do funcionário
    print(funcionario.exibir_detalhes())
    
    # aumenta o salário em 10%
    funcionario.aumentar_salario(10)
    
    # exibe os detalhes após o aumento
    print(funcionario.exibir_detalhes())
