#Montar listas com base em dicionário

frutas = {'Banana': 1.50, 'Morango': 3.99, 'Melancia': 5.00}
carrinho = []
soma = 0

while True:
    
    opcao = int(input('Escolha a opcao : \n 1 - Banana\n 2 - Morango\n 3 - Melancia: '))
    
    if opcao == 1:
        carrinho.append('Banana')
    
    elif opcao == 2:
        carrinho.append('Morango')
    
    elif opcao == 3:
        carrinho.append('Melancia')
    
    elif opcao == 4:
        break
        
    else:
        print('Opcao inválida')
        
soma = 0

for fruta in carrinho:
    soma = soma + frutas[fruta]
    
print('Itens comprados: ')
print(carrinho)
print('O total de compras foi de R$ ', soma)




####################################################################################################

exit()
frutas = {'Banana': 1.50, 'Morango': 3.99, 'Melancia': 5.00}
cesta = []
soma = 0

while True:
    
    print('Escolha a sua fruta')
    print( 'banana')
    print('morango')
    print('melancia')
    
    nome_fruta = input('Digite a fruta: ')

    #nome_fruta = input('Nome da fruta na lista: ')
    if nome_fruta == ('Banana'):
        cesta.append(frutas['Banana'])
        
    elif nome_fruta == 'Morango':
        cesta.append(frutas['Morango'])

    elif nome_fruta == 'Melancia':
        cesta.append(frutas['Melancia'])
        
    elif nome_fruta is None or nome_fruta not in frutas:
        break

for item in cesta:
    soma = soma + item
    
print(cesta)
print(soma)
