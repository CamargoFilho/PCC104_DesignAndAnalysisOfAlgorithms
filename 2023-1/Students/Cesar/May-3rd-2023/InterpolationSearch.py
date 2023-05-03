#Implements nonrecursive interpolationsearch
#Input: An array A[0..n − 1] sorted in ascending order and
#a search key K
#Output: An index of the array’s element that is equal to K


K = 55 #Chave que desejo encontrar
m = 13 #posição final
n = 0 #posição inicial
A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98] #Array
l = A[m] #último valor do Array
r = A[n] #primeiro valor do Array

def IS():
    while K != A[n]:
        if K == A[n]: #Se a chave K for encontrada
            print(A[n]) #Imprima a chave
        else: #Se nenhuma das condições forem satisfeitas
            n = A[n] + (K - n)*((A[m]-A[n])/(m-n)) #calcula a posição estimada da chave K
    print("-1") #Encerrada a busca, imprima "-1"


# Expressão Matemática 
# -> Somatório de n até n-1 de (log2 n+1)

#Cálculo da função de custo
# -> f(n) = (log2 n+1)


#Classe de eficiência
# -> Pior caso = Não existe a chave buscada no array = O(n) -> Definição: implica que a ordem de gradenza neste caso tende zero
# -> Melhor caso = A chave buscada existe no array = O(1) -> Definição: implica que a ordem de grandeza neste caso é constante
# -> Caso médio = A chave pode ou não ser encontrada no array = O(log n) -> Definição: implica que a ordem de grandeza neste caso tende ao infinito 

    