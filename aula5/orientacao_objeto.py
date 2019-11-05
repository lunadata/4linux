#Orientaçao a objeto
class Carro():
    
    #Construtor
    def __init__(self, modelo = '', cor = '', velociadade = '', ano = ''): #self é o único parametro obrigatorio
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
        self.ano = ano
        
    def acelerar(self):
        self.velocidade += 10
    
    def frear(self):
        self.velocidade -= 10
        if self.velocidade == 0:
            print('O carro está parado')
      
    
#criar objeto
fusca = Carro('Fusca', 'Vermelho', 0,  1975)
verona = Carro()

print(fusca.modelo)
print(fusca.cor)
print(fusca.velocidade)
print(fusca.ano)

fusca.acelerar()
fusca.acelerar()
print(fusca.velocidade)
