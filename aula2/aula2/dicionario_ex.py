#Dicionários

dicionario = {
    'noata1': 5.5, 
    'nota': 6.5, 
    'nota3': 3.5
}

soma = 0
media = 0


for chave in dicionario.keys():
    soma += dicionario[chave]
print(soma)

##########################################3
for valor in dicionario.values():
    soma += valor
print(soma)

media = soma / 3
print(media)

