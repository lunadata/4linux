#criar um arquivo e armazenar um registro
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
cpf = input("Digite o CPF: ") 

registro = '\n' + nome + ';' + idade + ';' + cpf + ';'

with open('registro.txt','a+') as f:
f.write(registro)


exit()
cpf = input('Digite o cpf: ')

with open('arquivo_pessoa.json') as f:
    conteudo = f.readlines()
    
# lista ['111.222.333-45;guilherme;30;', 
#        111.222.333-46;luciana;28;]

for registro in conteudo:
    #'111.222.333-45;guilherme;30;'
    if cpf in registro:
        saida = registro.split(';')
        print('CPF:', saida[0])
        print('Nome:', saida[1])
        print('Idade:', saida[2])
print(conteudo)
        
exit()
#criar um arquivo e armazenar um registro
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
cpf = input("Digite o CPF: ") 


