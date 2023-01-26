from random import choice as cho
#criar a função matriz 4x4
def cria_matriz_4x4():
    ''' Está função cria uma matriz 4x4 e distribui aleatoriamente número de 1 a 15 nela a não ser na priomeira casa onde fica o 0
    Argumentos: nehum'''
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
    """mostra o tabuleiro do jogo.
    Argumentos: nehum"""
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
    """mostra o menu de movimentação enquanto ao 0
    Argumentos: nehum"""
    #print das setas e as teclas para acionar o movimento
    print('''       /ŵ\\
 <--a       d-->
       \s/''')
#criando a função que recebe e verifica se o movimento é legal
def recebe_movimento():
    """recebe e verifica se o movimento do usuário é válido, após isso executa a função movimentação 
com o valor do respectivo movimento caso ele seja válido
Argumentos: nehum"""
    global matriz_real
    #pedir a escolha do usuário
    jogada=input("escolha a sua jogada: ")
    #verificar se foi para cima
    if jogada == "w":
        #verificar se o movimento é legal
        if matriz_real[0][0]!= 0 != matriz_real[0][1] and matriz_real[0][2]!= 0 != matriz_real[0][3]:
            #se sim realizar o movimento
            movimenta(2)
        #se não
        else:
            #mostrar explicação
            print("jogada invalida. ")
            #devolver erro
            return False
    #verificar se foi para baixo
    elif jogada == "s":
        #verificar se o movimento é legal
        if matriz_real[3][0]!= 0 != matriz_real[3][1] and matriz_real[3][2]!= 0 != matriz_real[3][3]:
            #se sim realizar o movimento
            movimenta(3)
        #se não
        else:
            #mostrar explicação
            print("jogada invalida. ")
            #devolver erro
            return False
    #verificar se foi para a esquerda
    elif jogada == "a": 
        #verificar se o movimento é legal
        if matriz_real[0][0]!= 0 != matriz_real[1][0] and matriz_real[2][0]!= 0 != matriz_real[3][0]:
            #se sim realizar o movimento
            movimenta(0)
        #se não
        else:
            #mostrar explicação
            print("jogada invalida. ")
            #devolver erro
            return False
    #verificar se foi para a direita
    elif jogada == "d":
        #verificar se o movimento é legal
        if matriz_real[0][3]!= 0 != matriz_real[1][3] and matriz_real[2][3]!= 0 != matriz_real[3][3]:
            movimenta(1)
        #se não
        else:
            #devolver erro
            return False
    else:
        print("entrada não reconhecida tente novamente.")
        return False
#criar a função de movimentação pedindo a direção do movimento
def movimenta(l):
    """esta função realiza a movimentação das pessa do tabuleiro precisa de argumento, porém são dados automaticamente pela função que recebe os movimento, sendo eles:
    esquerda[0];
    direita[1];
    por cima[2]; ou
    por baixo[3]. """
    #receber a matriz e o valor so zero como globais
    global posição_0, matriz_real
    #mapeando os índices do 0: x e y
    x,y=posição_0
    #caso seja pela esquerda[0]
    if l == 0:
        #trocar com um elemento na mesma linha com o índice uma unidade menor
        #indo até o 0 atribuindo o oi a ele
        oi=matriz_real[x][y]
        #indo no índice do número da troca e atribuindo  oi2 a ele 
        oi2=matriz_real[x][y-1]
        #atualizando a posição do 0
        posição_0=(x,y-1)
        #realizando a troca de valores
        matriz_real[x][y]=oi2
        matriz_real[x][y-1]=oi
    elif l == 1:
        #trocar com um elemento na mesma linha com o índice uma unidade menor
        #indo até o 0 atribuindo o oi a ele
        oi=matriz_real[x][y]
        #indo no índice do número da troca e atribuindo  oi2 a ele 
        oi2=matriz_real[x][y+1]
        #atualizando a posição do 0
        posição_0=(x,y+1)
        #realizando a troca de valores
        matriz_real[x][y]=oi2
        matriz_real[x][y+1]=oi
    elif l == 2:
        #trocar com um elemento na mesma linha com o índice uma unidade menor
        #indo até o 0 atribuindo o oi a ele
        oi=matriz_real[x][y]
        #indo no índice do número da troca e atribuindo  oi2 a ele 
        oi2=matriz_real[x-1][y]
        #atualizando a posição do 0
        posição_0=(x-1,y)
        #realizando a troca de valores
        matriz_real[x][y]=oi2
        matriz_real[x-1][y]=oi
    elif l == 3:
        #trocar com um elemento na mesma linha com o índice uma unidade menor
        #indo até o 0 atribuindo o oi a ele
        oi=matriz_real[x][y]
        #indo no índice do número da troca e atribuindo  oi2 a ele 
        oi2=matriz_real[x+1][y]
        #atualizando a posição do 0
        posição_0=(x+1,y)
        #realizando a troca de valores
        matriz_real[x][y]=oi2
        matriz_real[x+1][y]=oi
def veri_v():
    """verifica se o usuário ganhou a partida."""
    #conciderar as variaveis globais matriz
    global matriz_real
    #criar a variavel contadora para verificar se foi atingida a sequência de 15 números que determinam
    #criar a variavel anterior como nulo para não dar erro quando for citada pela primeira vez 
    cont_v=0
    ant=0
    #criar um for loop para percorrer todas as linhas
    for i in matriz_real:
        #criar um for loop para percorrer os valorese das linhas
        for g in i:
            #verificar se o valor atual é maior do que o anterior
            if ant<g:
                #adicionar a variavel contadora
                cont_v+=1
                ant=g
            #se não verificar se a variavel contadora chegou em 15
            elif cont_v == 15:
                #mostrar a mensagem de vitória
                print("parabéns você venceu o jogo.")
                # se sim devolver verdadeiro
                return False
    #se não retornar falso
    return True
def partida():
    print('''                    Bem-vindo ao Jogo do 15!
    Nele você terá que fazer o tabuleiro ficar dessa forma:
    -------------
    | 1| 2| 3| 4|
    -------------
    | 5| 6| 7| 8|
    -------------
    | 9|10|11|12|
    -------------
    |13|14|15| 0|
    -------------.
    Sendo que as peças vão começar organizadas de maneira aleatória e você só pode
    mudar o zero de lugar com as peças que estão em cima, em baixo,
    na esquerda ou na direita dele.
    Boa sorte!!''')
    while veri_v():
        v=0
        mostra_matriz()
        movimentos()
        while v ==0:
            v=recebe_movimento()
    else:
        mostra_matriz()
#definindo valores iniciais e cahamando a função partida(main)
matriz_real=cria_matriz_4x4()
#posição inicial do zero
posição_0=(0,0)
partida()