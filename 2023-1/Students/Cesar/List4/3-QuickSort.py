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

    #Mede o tamanho da lista inicial
    tam = len(A);
    itam = tam-1

    #Imprime a lista inicial não ordenada
    print("Lista A (Não ordenada)",A); 

    #Ordena a lista inicial
    A.sort();

    #Imprime a lista inicial ordenada
    print("Lista A (Ordenada)", A); 

       
    #Cria o contador do laço para dividir a lista em n partes
    i = 0;
    j = -1;
    k = 0;

    #Executa a divisão da lista inicial em n sublistas
    for i in range(tam):
        print("Sublista A",i+1,"=", A[i]);

    #Busca o maior valor entre as n listas
    if A[itam] > A[i]:
        print("O maior valor entre as listas é", A[itam]);
    else:
        print("O maior valor entre as listas é igual para todos",A[i]);


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