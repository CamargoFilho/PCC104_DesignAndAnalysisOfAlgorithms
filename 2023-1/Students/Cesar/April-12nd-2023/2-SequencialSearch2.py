# Implementação do algoritmo Sequential Search2
# Operação básica:  Comparar se o item atual é o item procurado

def sequential_search2(array, searched_item):
    array.append(searched_item)
    index = 0 # 1
    while array[index] != searched_item:
        index += 1 # n+1
    if index < len(array)-1: # 2(n-1)
        return print("A posição do valor procurado é:", index)
    else:
        return print("Valor não encontrado")


array = [-5, 2, 8, 0, 3]
searched_item = 3
print("Arranjo:", array)
print("Valor procurado:", searched_item)
sequential_search2(array, searched_item)
print("Arranjo com append:", array)


# Expressão matemática = 2(n-1)+(n+2)
# Cálculo da função de custo = 3n-1
# Indicação da classe de eficiência (O ou Theta) = O(n) e Theta (n)
# Justificativa: O = Quando a entrada for menor ou igual ao array, ele será constante e adaptável a quantidade de entradas