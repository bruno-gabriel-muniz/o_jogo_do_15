from random import choice as cho
#criar a função matriz 4x4
def cria_matriz_4x4():
    ''' Está função cria uma matriz 4x4 e distribui aleatoriamente número de 0 a 15 nela'''
    #criar variavel contadora para colocar os números nas linhas e colunas, assim, como a variável da linha e a matriz em si
    lista_disponiveis=list(range(1,16))
    linha=[]
    matriz=[]
    #criando a verificação para adcionar a cas vazia na primeira linha
    primeira=1
    #criador de linhas
    for t in range(4):
        #resetando o valor da linha
        linha.clear()
        #criador de colunas
        for i in range(4):
            #verificando se é a primiera linha para adicionar a casa vazia
            if primeira==1:
                #verificando que a casa vazia foi adcionada
                primeira=0
                #adcionando a casa vazia
                linha.append(0)
            #verificando sa a casa vazia não foi adcionada
            else:
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
def mostra_matriz():
    global matriz_real
    #crindo ciclo for que vai passar por todos os elementos da matriz
    for i in matriz_real:
        #imprimindo a divisoria das linhas
        print("-"*13)
        #imprimindo cada linha da matriz separadamente
        v1=i[0]
        v2=i[1]
        v3=i[2]
        v4=i[3]
        print("|%2i|%2i|%2i|%2i|"%(v1,v2,v3,v4))
    print("-"*13)
#função que mostra os movimentos disponivei para o jogador
def movimentos():
    #print das setas e as teclas para acionar o movimento
    print('''       /ŵ\\
 <--a       d-->
       \s/''')
#criando a função que recebe e verifica se o movimento é legal
def recebe_movimento():
    global matriz_real
    #pedir a escolha do usuário
    jogada=input("escolha a sua jogada: ")
    #verificar se foi para cima
    if jogada == "w":
        #verificar se o movimento é legal
        if matriz_real[0][0]!= 0 != matriz_real[0][1] and matriz_real[0][2]!= 0 != matriz_real[0][3]:
            #se sim realizar o movimento
            print("realizar o movimento")
        #se não
        else:
            #devolver erro
            print("não realizar o movimento")
    #verificar se foi para baixo
    elif jogada == "s":
        #verificar se o movimento é legal
        if matriz_real[3][0]!= 0 != matriz_real[3][1] and matriz_real[3][2]!= 0 != matriz_real[3][3]:
            #se sim realizar o movimento
            print("realizar o movimento")
        #se não
        else:
            #devolver erro
            print("não realizar o movimento")
    #verificar se foi para a esquerda
    elif jogada == "a": 
        #verificar se o movimento é legal
        if matriz_real[0][0]!= 0 != matriz_real[1][0] and matriz_real[2][0]!= 0 != matriz_real[3][0]:
            #se sim realizar o movimento
            "realizar o movimento"
        #se não
        else:
            #devolver erro
            print("não realizar o movimento")
    #verificar se foi para a direita
    elif jogada == "d":
#verificar se o movimento é legal
        if matriz_real[0][3]!= 0 != matriz_real[1][3] and matriz_real[2][3]!= 0 != matriz_real[3][3]:
            print("realizar o movimento")
        #se não
        else:
            #devolver erro
            print("não realizar o movimento")
matriz_real=cria_matriz_4x4()
mostra_matriz()
movimentos()
recebe_movimento()