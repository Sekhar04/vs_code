graph1 = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
def bfs(graph, start): 
    visited = set()
    queue = [start]
    order = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(graph[vertex]-visited)
    return order

print(bfs(graph1, 'A'))

def dfs(graph, start):
   visited = set()
   stack = [start]
   order = []
   while stack:
       vertex = stack.pop()
       if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            stack.extend(graph[vertex]- visited)
            return order
       
print(dfs(graph1, 'A'))
