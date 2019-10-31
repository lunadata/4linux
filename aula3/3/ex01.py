#Dicionário
#Criar cesta de frutas baseada na lista abaixo
# Passos
 # 1 - Criar lista de frutas
 # 2 - criar o menu [repetiçao]
 # 3 - Adicionar a entrada de acordo com a fruta escolhida na cesta
 # 4 - Ao sair, apresentar a cesta
 
fruta = ['banana', 'morango', 'melancia']
cesta = list()

while True:
 
 print('Escolha a sua fruta')
 print( '1 - banana')
 print('2- morango')
 print('3 - melancia')
 print('4 - sair')
 
 escolha = int(input('Digite a opcao:')
 
 if escolha == 4:
     print('Opcao invalida')
     break

 else:
     cesta.append(escolha, -1)
print(cesta)
    
        
 
exit()
frutas = ['bana', 'morango', 'melancia']

cesta = []

while True:
    print('Escolha a posiçao de uma fruta na cesta: \n 0 - banana \n 1 - morango \n 2- melancia')
    
    
   # for fruta in frutas:
    posicao = int(input('Poiscao da fruta na cesta: '))
    if posicao == 0:
        cesta.append(frutas[0])
    elif posicao == 1:
        cesta.append(frutas[0])
    elif posicao == 2:
        cesta.append(frutas[2])
    elif posicao == 4:
        break
        
        
        #if posicao == frutas[0]:
         #   cesta.append(frutas[1])
        #elif posicao == frutas[1]:
            #cesta.append(frutas[1])
        #elif posicao == frutas[2]:
            #cesta.append(frutas[2])
print(cesta)
