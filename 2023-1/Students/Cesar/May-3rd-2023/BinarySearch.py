#Implements nonrecursive binary search
#Input: An array A[0..n − 1] sorted in ascending order and
#a search key K
#Output: An index of the array’s element that is equal to K


K = 55 #Chave que desejo encontrar
m = 13 #tamanho do Array
A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98] #Array
l = A[m] #último valor do Array
r = A[m-1] #penúltimo valor do Array

def BS():
    while l < r : #Se último valor do Array for menor que o penúltimo valor do Array
        m = l+r/2 #soma o último e o penúltimo valor e divide por dois para encontrar o próximo indice
        if K == A[m]: #Se a chave K for encontrada
            print(A[m]) #Imprima a chave
        elif K < A[m]: #Se a chave o valor presente na posição do Array for menos que a achave K
                r = A[m-1] #Coleta o valor do "índice atual menos 1"
        else: #Se nenhuma das condições forem satisfeitas
               l = A[m+1]  #Coleta o valor do "índice atual mais 1"
    print("-1") #Encerrada a busca, imprima "-1"


# Expressão Matemática 
# -> Somatório de 1 até n-1 de (n/2)+1

#Cálculo da função de custo
# -> f(n) = (n/2)+1


#Classe de eficiência
# -> Pior caso = Não existe a chave buscada no array = O(n) -> Definição: implica que a ordem de gradenza neste caso tende zero
# -> Melhor caso = A chave buscada existe no array = O(1) -> Definição: implica que a ordem de grandeza neste caso é constante
# -> Caso médio = A chave pode ou não ser encontrada no array = O(log n) -> Definição: implica que a ordem de grandeza neste caso tende ao infinito 

    