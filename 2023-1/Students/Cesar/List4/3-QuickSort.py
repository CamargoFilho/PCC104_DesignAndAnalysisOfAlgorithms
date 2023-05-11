######################################################
# Divide-and-Conquer of an Array of n elements
#######################################################
# 
# QUICK SORT
#
# HoarePartition(A[l..r])
# //Partitions a subarray by Hoare’s algorithm, using the first element
# // as a pivot
# //Input: Subarray of array A[0..n − 1], defined by its left and right
# // indices l and r (l < r)
# //Output: Partition of A[l..r], with the split position returned as
# // this function’s value
#   p ← A[l]
#   i ← l; 
#   j ← r + 1
#   
#   repeat
#       repeat i ← i + 1 until A[i] ≥ p
#       repeat j ← j − 1 until A[j] ≤ p
#       swap(A[i], A[j ])
#   until i ≥ j
#   swap(A[i], A[j ]) //undo last swap when i ≥ j
#   swap(A[l], A[j ])
#   return j
#######################################################
#Cria o método Dividir e Conquistar
def QuickSort():

    #Lista com n elementos, n > 1
    A = [8, 3, 2, 9, 7, 101, 1, 5, 4, 22, 1]; 

    #Lista com n elementos, n = n
    #A = [8, 8, 8, 8, 8, 8]; 

    #Ordena a lista inicial
    A.sort();

    #Mede o tamanho da lista inicial
    tam = len(A);

    #Calcula o resto da divisão por do total da lista por 2
    mod = tam % 2
    
    #Define o pivot inicial da lista (primeiro elemento da lista)
    if mod != 0: 
        #Se o resto da divisão for diferente de zero, dividir uma das listas em qtd. de valores ímpar
        pivot = int(tam/2)+mod;
    else:
        #Se o resto da divisão for igual a zero, dividir amba as listas em qtd. de valores par
        pivot = int(tam/2);

    indexList = [];
    i = 0;
    for i in range(tam):
        indexList.append(i)

    l = tam-1
    r = 0

    #Imprime a lista inicial não ordenada e o pivot inicial
    print("Lista A ->",A);
    print("Indices da lista ->",indexList);
    print("Pivot [INICIO] (s) ->",pivot);
    print("Primeiro valor a esquerda [INICIO] (l) ->",r);
    print("último valor a direita [INICIO] (r) ->",l);


    i = l;
    j = r+1;

    #Executa o QuickSort
    


#Invoca o método Dividir e Conquistar
QuickSort();



# Respostas
#   O Mergesort, comparado com os algoritmos quicksort e heapsort não é estável, 
#   pois a quantidade linear de armazenamento extra que o algoritmo requer o torna instável

# Expressão Matemática 
# T(n) = aT(n/b) + f(n)

#Cálculo da função de custo
# C(n) = 2C(n/2) + Cmerge(n)

#Classe de eficiência
# -> Melhor caso = Encontrar na primeira comparação o maior valor -> O (1)
# -> Pior caso = Todos os valores são menor que 1 -> O (n)
# -> Caso médio = Não encontrar o maior valor, todos são iguais -> O (n log n)

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