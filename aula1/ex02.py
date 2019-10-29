#Motorista habilitado
# 1 - verificar idade

# 2 - verificar se possui habilitacao

idade = int(input('Digite sua idade: '))
cnh = input('Possui CNH: ')

#verificar se dade é maior que 18
if (idade >= 18):
    if(cnh =='sim'):
        print('Pode conduzir')
    else:
        print('Nao possui habilitacao')
else:
    print('Nao possui idade mínima')
    
