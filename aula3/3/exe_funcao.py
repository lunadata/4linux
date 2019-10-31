
def idade(ano_atual, ano_nascimento):
    resultado_idade = (ano_atual - ano_nascimento)
    return resultado_idade

def media_aluno(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media
    
    
###################################################################################

def main ():

    print(idade(2019, 1976))

    media_final = media_aluno(8.5, 8.8, 5.9, 7.8)
    print(media_final)
    
if __name__ == "__main__":
    main()
