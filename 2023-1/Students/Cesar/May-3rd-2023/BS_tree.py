#Implements recursive Binary Search Tree
#Input: An array A[0..n − 1] sorted in ascending order and
#a search key K
#Output: An index of the array’s element that is equal to K

K = 55 #Chave que desejo encontrar
m = 13 #posição final
A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98] #Array

def BStree_Search():
    while K != A[m]:
        if A[m] < K:
            m = m+1
        else:
            m = m-1
    return -1


# Expressão Matemática 
# -> Recorrência de n até n-1 de n+1 se K > A[m]
# -> Recorrência de n até n+1 de n+1 se K < A[m]


#Cálculo da função de custo
# -> f(n) = (n+1)
# -> f(n) = (n-1)

#Classe de eficiência
# -> Pior caso = Não existe a chave buscada no array = O(n) -> Definição: implica que a ordem de gradenza neste caso tende zero
# -> Melhor caso = A chave buscada existe no array = O(1) -> Definição: implica que a ordem de grandeza neste caso é constante
# -> Caso médio = A chave pode ou não ser encontrada no array = O(log n) -> Definição: implica que a ordem de grandeza neste caso tende ao infinito 

##############################################################3    

X = 60 #Chave que desejo inserir
m = 13 #posição final
A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98] #Array
i = 0

def BStree_Insert():
       for i in range(m):
        if A[i] > X :
            m = m+1
            A[i] = X
        else:
            i = i+1
        return -1

# Expressão Matemática 
# -> Somatório de 1 até n+1 de n

#Cálculo da função de custo
# -> f(n) = (n+1)


#Classe de eficiência
# -> Pior caso = Não há espaço no array = O(1) -> Definição: implica que a ordem de gradenza neste caso é constante
# -> Melhor caso = Há espaço no array = O(n) -> Definição: implica que a ordem de grandeza neste caso tende a zero
# -> Caso médio = Pode ou não haver espaço no array = O(log n) -> Definição: implica que a ordem de grandeza neste caso tende ao infinito 

    