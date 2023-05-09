# Divide-and-Conquer of an Array of n elements
#MergeSort
#//Merges two sorted arrays into one sorted array
#//Input: Arrays B[0..p − 1] and C[0..q − 1] both sorted
#//Output: Sorted array A[0..p + q − 1] of the elements of B and C

A = [8, 3, 2, 9, 7, 1, 5, 4];
B = [];
C = [];
i = 0; 
j = 0; 
k = 0;

def MergeSort():
    while i < p and j < q:
        if B[i] < C[j]:
            A[k] = B[i]; 
            i = i + 1;
        else A[k] = C[j];
            j = j + 1;
            k = k + 1;
        if i = p:
            copy C[j..q − 1] to A[k..p + q − 1]
        else 
            copy B[i..p − 1] to A[k..p + q − 1]


MergeSort();


# Expressão Matemática 
# -> T (n) = aT (n/b) + f (n)

#Cálculo da função de custo
# -> A(n) = 2A(n/2) + 1


#Classe de eficiência
# -> Pior caso = Todos os valores comparados são iguais, não há número maior = O(n)
# -> Melhor caso = Encontrar o maior valor comparado nas duas listas simultaneamente = O(1)
# -> Caso médio = Encontrar o maior valor comparado em uma lista e não em outra lista = O(log n)

    