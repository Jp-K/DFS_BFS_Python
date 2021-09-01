# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def dfs(visited, graph, node):
    if node not in visited:
        # print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited


def bfs(graph, node):  # function for BFS
    visited = []  # List for visited nodes.
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        # print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


if __name__ == '__main__':
    graph1 = {'A': {},
              'B': ['A', 'D', 'E'],
              'C': ['A', 'F'],
              'D': {},
              'E': {},
              'F': {'C', 'E'}}
    bfs_visitados = []
    for item in graph1:
        retorno = bfs(graph1, item)
        for nodo in retorno:
            if nodo not in bfs_visitados:
                bfs_visitados.append(nodo)
    print(bfs_visitados)

    dfs_visitados = []
    visiteds = []
    inicio = 'C'
    returns = dfs(visiteds, graph1, inicio)
    for item in graph1:
        if item not in returns:
            dfs_visitados = dfs(visiteds, graph1, item)

    print(dfs_visitados)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
