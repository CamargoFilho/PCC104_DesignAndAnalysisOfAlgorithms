######################################################
# Divide-and-Conquer of an Array of n elements
#######################################################
#
# MERGE SORT
# 
#ALGORITHM Merge(B[0..p − 1], C[0..q − 1], A[0..p + q − 1])
# //Merges two sorted arrays into one sorted array
# //Input: Arrays B[0..p − 1] and C[0..q − 1] both sorted
# //Output: Sorted array A[0..p + q − 1] of the elements of B and C
#   i ← 0; 
#   j ← 0; 
#   k ← 0
#   
#   while i < p and j < q do
#       if B[i] ≤ C[j]
#           A[k]← B[i]; 
#           i ← i + 1
#       else 
#           A[k]← C[j]; 
#           j ← j + 1
#       k ← k + 1
#   if i = p
#       copy C[j..q − 1] to A[k..p + q − 1]
#   else copy B[i..p − 1] to A[k..p + q − 1]
#######################################################
#Cria o método Dividir e Conquistar
def MergeSort():

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

    #Executa a divisão da lista inicial em n sublistas
    for i in range(tam):
        print("Sublista A",i+1,"=", A[i]);

    #Busca o maior valor entre as n listas
    if A[itam] > A[i]:
        print("O maior valor entre as listas é", A[itam]);
    else:
        print("O maior valor entre as listas é igual para todos",A[i]);


#Invoca o método Dividir e Conquistar
MergeSort();



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