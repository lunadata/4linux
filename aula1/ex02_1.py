#Escrever um script em Python que simule uma calculadora
# O usuário deverá digitar dois números e escolher a operaçao 
# Ao final, mostrar o resultado da operaçao escolhida com os números

#1 - Entrada de dados - interaçao
num1 = int(input('Digite uma número: '))
num2 = int(input('Digite outro número: '))
oper = input('Sinal de operaçao: ')

# Identificando operaçao

if (oper == '+'):
    print(num1 + num2)
elif (oper == '-'):
    print(num1 - num2)
elif (oper == '*'):
    print(num1 * num2)
elif (oper == '/'):
    print(num1 / num2)
elif (oper == '**'):
    print(num1 ** num2)
else:
    print('Opcao invalida. Digite um sinal de operacao')
    
    
    





exit()

nome = input('Seu nome: ')
idade = int(input('Sua idade: '))
cnh = input('Possui habilitacao: ')

if (idade >= 18 and cnh == 'Sim'):
    print('Pode dirigir')
else:
    print('Nao pode dirigir')
    
