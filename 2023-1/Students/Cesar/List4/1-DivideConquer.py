# Divide-and-Conquer of an Array of n elements

A = [8, 3, 2, 9, 7, 1, 5, 4];
A1 = [];
A2 = [];
i = 1;
tam = len(A);
print("tam",tam)
if tam % 2 != 0:
    div = int(tam/2)+1;
else:
    div = int(tam/2);
print("div = ",div)
j = int(div);
print("j = ",j)
k = 1;
BigNum1 = 1;
BigNum2 = 2;

def DivideConquer():
    for i in range(tam):
        if i < div:
            A1.append(A[i])
        else:
            A2.append(A[i])
    print("A1 = ", A1)
    print("A2 = ", A2)


    

    if BigNum1 < BigNum2:
        print("Lista =", A)
        print("O maior número da lista acima é =", BigNum2)    
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

    