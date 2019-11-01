#!/usr/bin/python3
#Funçao main

#Exercícios
        # Cirar lista de produtos
        # Preencher lista de compras (adicionar itens)
        # Somar os itens de uma lista
        # Apresentar o resultado

        # Obs criar uma as funçoes em arquivos separados da main()

# 1 - imports
from lib import *

# funcao principal
def main():
    dic = {'Banaa': 1.50, 'Morango': 8.00, 'Melancia': 12.80}
    
    while True:
        opcao = input('Escolha a fruta: \n1-Banana\n2-Morang\n3-Melancia\n ')

        if opcao == '1':
            adiciona_item(dic['Banana'])
            
        elif opcao == '2':
            adiciona_item(dic['Morango'])
            
        elif opcao == '3':
            adiciona_item(dic['Melancia'])
            
        elif opcao == '4':
            break
        
        else:
            print('Opcao inválida')
    
    print(total_carrinho(carrinho))
            
            
if __name__ == "__main__":
    main()
    
#documentaçao
