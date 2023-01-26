from random import choice as cho
#criar a função matriz 4x4
def cria_matriz_4x4():
    ''' Está função cria uma matriz 4x4 e distribui aleatoriamente número de 0 a 15 nela'''
    #criar variavel contadora para colocar os números nas linhas e colunas, assim, como a variável da linha e a matriz em si
    lista_disponiveis=list(range(16))
    linha=[]
    matriz=[]
    #criador de linhas
    for t in range(4):
        #resetando o valor da linha
        linha.clear()
        #criador de colunas
        for i in range(4):
            #escolhendo um número disponivel da lista
            cont=cho(lista_disponiveis)
            #adicionador do cont na coluna
            linha.append(cont)
            #removaendo o número para ele não ser repetido
            lista_disponiveis.remove(cont)
        #adicionando a linha na matriz
        matriz.append(linha.copy())
    #retornando a matriz
    return matriz
#criando função que mostra a matriz
    #crindo ciclo for que vai passar por todos os elementos da matriz
        #imprimindo cada linha da matrz separadamente