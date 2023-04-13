# Implementação do algoritmo Selection Sort
# Operação básica: Comparação para encontrar o menor elemento

def selection_sort(array):
    size = len(array) # 1
    for position in range(size): # n(n-1) = n^2-1
        index_min = position # 1
        for step in range(position+1, size): # n(n-(n+1)) = n+1
            if array[step] < array[index_min]: # n-n = 1
                index_min = step # 1
        if index_min != position:
            array[position], array[index_min] = array[index_min], array[position] #n^2
    return array


array = [-5, 2, 8, 0, 3]
print("Arranjo:", array)
sorted_array = selection_sort(array)
print("Arranjo ordenado:", sorted_array)


# Expressão matemática = 2n^2+(n+1)+3
# Cálculo da função de custo = 2n^2
# Indicação da classe de eficiência (O ou Theta) = O(n^2) e Theta (n^2)
# Justificativa: O = Quando a entrada for menor ou igual ao array, ele será exponecial e adaptável a quantidade de entradas