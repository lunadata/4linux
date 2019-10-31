#Dcion[arios - soma
dicionario = {'n1': 8.3, 'n2': 7.2}

#1 calcular soma
soma = 0

for elemento in dicionario.values():
    soma = soma + elemento
    
print(soma)

#2 - Calcular média
media = soma / len(dicionario)
print(media)
