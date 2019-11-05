class Pessoa():
    
    #Construtor
    def __init__(self, nome = '', sexo = '', peso = '', cor = '', nacionalidade = ''):
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.cor = cor
        self.nacionalidade = nacionalidade
        
    #Criar métodos
    def falar(self):
        self.peso = 30
        if self.peso >= 120:
            print('Obeso')
        else:
            print('Dentro do peso')
            
#Instanciando um objeto

joao = Pessoa('Joao', 125, 'Parda', 'Alema')
print(joao.nome)
print(joao.falar)
joao.falar()

