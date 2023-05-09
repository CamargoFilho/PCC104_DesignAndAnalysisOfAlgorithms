# Divide-and-Conquer of an Array of n elements

A = [8, 3, 2, 9, 7, 1, 5, 4];
A1 = [];
A2 = [];
i = 1;
tam = len(A);
div = int(tam/2);
j = div;
k = 1;

def DivideConquer():
    for i in range(div):
        A1.append(A[i])
        

    for j in range(tam):
        A2.append(A[j])
        
    
    for i in range(div):
        k = div-1
        if A1[i] < A1[k]:
            BigNum1 = A1[k]
        else:
            if k < div:
                continue
            else:
                exit

    for j in range(tam):
        m = tam-1  
        if A2[j] < A2[m]:
            BigNum2 = A1[k]
        else:
            if m < tam:
               continue 
            else:
                exit


    if BigNum1 < BigNum2:
        print(BigNum2)
    else:
        print("Lista =", A)
        print("O maior número da lista acima é =", BigNum1)    

DivideConquer();


# Expressão Matemática 
# -> T (n) = aT (n/b) + f (n)

#Cálculo da função de custo
# -> A(n) = 2A(n/2) + 1


#Classe de eficiência
# -> Pior caso = Todos os valores comparados são iguais, não há número maior = O(n)
# -> Melhor caso = Encontrar o maior valor comparado nas duas listas simultaneamente = O(1)
# -> Caso médio = Encontrar o maior valor comparado em uma lista e não em outra lista = O(log n)

    