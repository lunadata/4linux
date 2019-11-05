class Pai():
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.nacionalidade = 'brasileira'
        
    def falar_portugues(self):
        print('Olá!. Como vai você?')
        
class Mae():
    def __init__(self):
        self.nome = ''
        self.idade = 0
        
    def falar_frances(self):
        print('Bonjour! Como vai você?')
    
       
class Filha(Pai, Mae):
    def __init__(self):
        Pai.__init__(self)
        self.profissao = ''

## Instanciar
f1 = Filha()
f1.falar_portugues()

f1.nome = 'Gabriela'
