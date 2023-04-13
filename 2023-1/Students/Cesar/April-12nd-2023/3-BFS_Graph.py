# Implementação do algoritmo Busca em largura com grafo (BFS)
# Operação básica: adicionar nós para serem visitados na fronteira.

from queue import Queue

def search_bfs(graph, start, goal):
    visited, frontier = set(), Queue()
    frontier.put((start, [start]))
    while frontier: # n
        (node, path) = frontier.get() #pop # 1
        if node == goal: # 1
            return path
        for neighbour in graph[node] - visited: # n-1
            visited.add(node) # 1
            frontier.put((neighbour, path + [neighbour])) # n+1
    return None

if __name__ == '__main__':
    graph = {0: set([1, 2]),
             1: set([3, 4]),
             2: set([5, 6]),
             3: set([7, 8]),
             4: set([9, 10]),
             5: set([11, 12]),
             6: set([13, 14]),
             7: set([]),
             8: set([]),
             9: set([]),
             10: set([]),
             11: set([]),
             12: set([]),
             13: set([]),
             14: set([])}
    start, goal = 0, 10
    path = search_bfs(graph, start, goal)
    if path is None:
        print("Caminho não definido.")
    else:
        print("Caminho do nó inicial (start) até o nó objetivo (goal)", path)


# Expressão matemática = (n+1)+(n-1)+(n)+3
# Cálculo da função de custo = 3n+3
# Indicação da classe de eficiência (O ou Theta) = O(n) e Theta (n)
# Justificativa: O = Quando a entrada for menor ou igual ao array, ele será constante e adaptável a quantidade de entradas