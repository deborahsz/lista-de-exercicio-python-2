class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

# Exemplo
if __name__ == "__main__":
    # cria uma instância da classe ContaBancaria com titular "João" e saldo inicial de 100.0
    conta = ContaBancaria("João", 100.0)
    
    # consulta o saldo inicial
    print(conta.consultar_saldo())
    
    # deposita um valor
    conta.depositar(50.0)
    
    # tenta sacar um valor
    conta.sacar(30.0)
    
    # tenta sacar um valor maior que o saldo
    conta.sacar(150.0)
    
    # consulta o saldo final
    print(conta.consultar_saldo())
