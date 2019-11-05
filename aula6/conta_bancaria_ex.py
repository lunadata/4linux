#Conta Bancária
#Criar classe Conta Bancária
##Agencia  ## Conta ## Titular ## Saldo #

## Os comportamentos esperados de uma conta são: 
    ## Saque <- Validar se tem dinheiro
    ## Depósito
    ## Ver saldo

class Conta():
    def __init__(self):
        self.agencia = '001'
        self.conta = 'Certão'
        self.titular = 'Maria Bonita Lampião'
        self.saldo = 500
                
    def sacar(self, valor):
        if self.saldo >= 0:
            
            self.saldo -= valor
            
            return self.saldo
            print(self.saldo)
            
            
    def deposito(self, valor):
        if valor < 0:
            print('Deposite um valor maior que 0')
        else:
            self.saldo += valor
            return self.saldo
            
    def verSaldo(self):
        print(self.saldo)
    
    def setSaldo(self, valor):
        self.__saldo += valor
    
    def transferencia(self, valor, conta):
        if valor > self.saldo:
            return 'Saldo insuficiente'
        
        else: 
            self.saldo -= valor
            conta.Setsaldo(valor)
          


