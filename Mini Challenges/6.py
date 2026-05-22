nomes = []

def cadastro(nomes):
    nome = input("Digite o nome de cadastro: ")
    nomes.append(nome)
    return nomes

def tem_ou_não(nome):
    if nome == nomes:
        print("Está na lista")
    else:
        print("Não está na lista")






