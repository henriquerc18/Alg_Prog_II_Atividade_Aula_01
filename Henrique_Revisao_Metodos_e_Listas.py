# Autor: Henrique Rosa Carvalho
# Aula 01 - 19/08/2020

'''
Atividade:
• Construir um algoritmo que contenha 3 listas:
      • Nomes de produtos
      • Preços de cada produto
      • Quantidades de cada produto
• Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas
'''


nomes = []
precos = []
quantidades = []

def produto_repetido(produto_Digitado):
    if produto_Digitado in nomes:
        return True
    return False

def preco_repetido(preco_Digitado):
    if preco_Digitado in precos:
        return True
    return False

def qtd_repetida(qtd_Digitada):
    if qtd_Digitada in quantidades:
        return True
    return False

def cadastrar_produto():
    while True:
        prod = input("Nome: ")
        if prod:
            if produto_repetido(prod):
                input("Produto já existe! [Enter]")
            else:
                input("Produto cadastrado com sucesso! [Enter]")
                return prod
        else:
            input("Digite algo! [Enter]")

def cadastrar_preco():
    while True:
        p = float(input("Preço: "))
        if p:
            if preco_repetido(p):
                input("Preço já cadastrado! Digite outro valor! [Enter]")
            else:
                input("Preço cadastrado com sucesso! [Enter]")
                return p
        else:
            input("Digite algo! [Enter]")

def cadastrar_quantidade():
    while True:
        qtd = int(input("Quantidade: "))
        if qtd:
            if qtd_repetida(qtd):
                input("Quantidade já cadastrada! Digite outro valor! [Enter]")
            else:
                input("Quantidade cadastrada com sucesso! [Enter]")
                return qtd
        else:
            input("Digite algo! [Enter]")

def cad_geral():
    nomes.append(cadastrar_produto())
    print("___________________________________________________")
    print("Nome: ", nomes)

    print("___________________________________________________")
    precos.append(cadastrar_preco())
    print("Preço: ", precos)

    print("___________________________________________________")
    quantidades.append(cadastrar_quantidade())
    print("Quantidades: ", quantidades)

def listar_produtos():
    print("Nome    Preço    Quantidade")
    for ind_prod, i in enumerate(nomes):
        print(nomes[ind_prod], " ", precos[ind_prod], "      ", quantidades[ind_prod])
    input("[Enter p/ continuar]")

def remover_produto():
    while True:
        produto = input("Produto p/ remover da lista: ")
        if produto_repetido(produto):
            nomes.remove(produto)
            listar_produtos() 
            break 
        else:
            input("Produto não encontrado! [Enter]")
            break

def menu_principal():
    opcao = input('''
        Menu
            0 - Finalizar o Programa
            1 - Cadastrar produto
            2 - Remover produto
            3 - Listar produtos
        Escolha: ''')
    if opcao in ('0','1','2','3'):
        return opcao
    input("Opção inválida! [Enter]")
    
# Programa principal
while True:
    resp = menu_principal()
    if resp == '0':
        break
    elif resp == '1':
        cad_geral()
    elif resp == '2':
        remover_produto()
    elif resp == '3':
        listar_produtos()
    
print("Fim")


