######################################################
# Divide-and-Conquer of an Array of n elements
#######################################################

#Lista com n elementos, n > 1
A = [8, 3, 2, 9, 7, 101, 1, 5, 4, 22, 1]; 

#Lista com n elementos, n = n
#A = [8, 8, 8, 8, 8, 8]; 

#Cria o método Dividir e Conquistar
def DivideConquer():

    #Imprime a lista inicial
    print("Lista A",A); 

    #Cria sublista 1 vazia
    A1 = []; 

    #Cria sublista 2 vazia
    A2 = []; 
    
    #Cria o contador do laço para dividir a lista em 2 sublistas
    i = 0;
    
    #Mede o tamanho da lista inicial
    tam = len(A);

    #Calcula o resto da divisão por do total da lista por 2
    mod = tam % 2
    
    #Compara se uma das sublistas irão ter qtd. de valores em par ou ímpar
    if mod != 0: 
        #Se o resto da divisão for diferente de zero, dividir uma das listas em qtd. de valores ímpar
        div = int(tam/2)+mod;
    else:
        #Se o resto da divisão for igual a zero, dividir amba as listas em qtd. de valores par
        div = int(tam/2);
    
    #Executa a divisão da lista inicial em 2 sublistas
    for i in range(tam):
        if i < div:
            A1.append(A[i])
        else:
            A2.append(A[i])
    print("Sublista A1 = ", A1)
    print("Sublista A2 = ", A2)

    #Cria as variáveis para armazenar os maiores valores obtidos de cada sublista
    BigN1 = max(A1);
    BigN2 = max(A2);

    #Valida qual dos maiores valores de cada sublista é o maior valor da lista original
    if BigN1 > BigN2:
        print("O maior número da lista A =", BigN1)
    else:
        print("O maior número da lista A =", BigN2)

#Invoca o método Dividir e Conquistar
DivideConquer();



# Respostas
# a) Será qualquer valor do arranjo, pois todos serão o maior valor
#
# b) T(n) = aT(n/b) + f (n)
#   onde "a" = Constantes conta a recorrência da função base
#   onde "b" = Constante que será divido o arranjo 
#   onde "n" > 1
#   onde "f(n)" = uma função que contabiliza o tempo gasto na divisão de uma instância
#
# c) Nem todo algoritmo de dividir para conquistar é necessariamente mais eficiente
#    do que mesmo uma solução de força bruta, mas na maioria dos casos comparado com outros algoritmos
#    ele possuem um tempo de execução relativamente menor. (Levitin, 2012)


# Expressão Matemática 
# T(n) = aT(n/b) + f(n)

#Cálculo da função de custo
# T(n) = 2T(n/2) + T(n)

#Classe de eficiência
# -> Melhor caso = Encontrar na primeira comparação o maior valor -> O (1)
# -> Pior caso = Todos os valores são menor que 1 -> O (n)
# -> Caso médio = Não encontrar o maior valor, todos são iguais -> O (log n)

#Teorema mestre
# Se
#   O(n^d), se a < b^d,
#   O(n^d log n), se a = b^d,
#   O(n^log b^a), se a > b^d,
# Então
#   a = 2
#   b = 2
#   d = 1
# Logo 
#   O (n log n)