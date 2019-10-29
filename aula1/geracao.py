ano_nasc = int(input('ano de nascimento: '))
geracao = str('Qual a sua geraçao?: ' )

# BBoomer = nascido até 1964
# Geracao X = 1964 até 1981
#Geracao y = 1981 até 1996
# Geraçao z = depois de 1996

# Calculo
if (ano_nasc <= 1964):
    print('Vocé é da geracao BBoomer')
elif (ano_nasc >  1964 and ano_nasc < 1981):
    print('Vocé é da geracao X')
elif (ano_nasc > 1981 and ano_nasc <1996):
    print('Vocé é da geracao Y')
else:
    print('Vocé é da geracao Z')
    
