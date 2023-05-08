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
# -> T (n) = aT (n/b) + f (n)

#Cálculo da função de custo
# -> A(n) = 2A(n/2) + 1


#Classe de eficiência
# -> Pior caso = Todos os valores comparados são iguais, não há número maior = O(n)
# -> Melhor caso = Encontrar o maior valor comparado nas duas listas simultaneamente = O(1)
# -> Caso médio = Encontrar o maior valor comparado em uma lista e não em outra lista = O(log n)

    