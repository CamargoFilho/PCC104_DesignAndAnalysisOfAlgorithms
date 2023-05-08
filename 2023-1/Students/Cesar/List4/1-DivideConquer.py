# Divide-and-Conquer of an Array of n elements

A = [8, 3, 2, 9, 7, 1, 5, 4];
A1 = [];
A2 = [];
i = 0;
tam = len(A);
div = tam/2;
j = div;

def DivideConquer():
    for i in range(div):
        A1[i] = A[i]

    for j in range(tam):
        A2[j] = A[j]

    
    for i in range(div):    
        if A1[i] < A1[k]:
            BigNum1 = A1[k]
        else:
            if k < div:
                k = i+1
            else:
                exit

    for j in range(tam):    
        if A2[j] < A2[m]:
            BigNum2 = A1[k]
        else:
            if m < tam:
                m = j+1
            else:
                exit


    if BigNum1 < BigNum2:
        print(BigNum2)
    else:
        print(BigNum1)    

DivideConquer();


# Expressão Matemática 
# -> Somatório de 1 até n-1 de (n/2)+1

#Cálculo da função de custo
# -> f(n) = (n/2)+1


#Classe de eficiência
# -> Pior caso = Não existe a chave buscada no array = O(n) -> Definição: implica que a ordem de gradenza neste caso tende zero
# -> Melhor caso = A chave buscada existe no array = O(1) -> Definição: implica que a ordem de grandeza neste caso é constante
# -> Caso médio = A chave pode ou não ser encontrada no array = O(log n) -> Definição: implica que a ordem de grandeza neste caso tende ao infinito 

    