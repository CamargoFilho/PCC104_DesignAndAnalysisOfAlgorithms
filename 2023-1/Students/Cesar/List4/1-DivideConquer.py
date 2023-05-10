######################################################
# Divide-and-Conquer of an Array of n elements
#######################################################

#Lista com n elementos
A = [8, 3, 2, 9, 7, 101, 1, 5, 4, 22, 1]; 

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


# Expressão Matemática 
# 

#Cálculo da função de custo
# 

#Classe de eficiência
# -> Pior caso =
# -> Melhor caso = 
# -> Caso médio =

#Teorema mestre


    