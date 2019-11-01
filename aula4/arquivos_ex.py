 #Criar um arquivo e armazenar um registro
 nome = input('Diga seu nome: ')
 idade = input('Digite sua idade: ')
 cpf = input('Digite o cpf: ') 
 
 pessoa = '\n' + nome + ';' + idade + ';'+ cpf + ';'
 
 with open('registro.txt', 'a+') as f:
     f.write(pessoa.txt)
 
 
#leitura de um dado a partir de arquivo
cpf = input('Digite o cpf: ')
with open('registro.txt') as f:
    conteudo = f.readlines()
    
for each_pessoa in conteudo:
    if cpf in registro.split(';'):
        print(pessoa)
