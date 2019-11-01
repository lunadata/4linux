#Arquivos

with open('pessoa.json', 'r') as f:
    conteudo = f.read()
    
print(conteudo)
quebrado = conteudo.split()
print(quebrado)


exit()
conteudo += 'Olá '

with open ('pessoa.json', 'w+') as f:
    f.write(conteudo)
