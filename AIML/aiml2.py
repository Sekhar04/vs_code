# A* Algorithm
# f(n) = g(n) + h(n)
# f(n) is the estimated cost of the cheapest and shortest path
# g(n) is the cost of the path from the start node to n
# h(n) is the estimated cost from n to the goal node
import heapq

# heap = []

# heapq.heappush(heap,20)
# heapq.heappush(heap,5) 
# heapq.heappush(heap,15) 
# heapq.heappush(heap,10) 

# print(heap)  # Output: [5, 10, 15, 20] 

# # pop the smallest element
# print(heapq.heappop(heap))  # Output: 5

# # peek at the smallest element
# print(heap[0])  # Output: 10

# # convert a list into a heap
# numbers = [20, 5, 15, 10]
# heapq.heapify(numbers)
# print(numbers)  # Output: [5, 10, 15, 20]

#Heuristic values
# heuristic = {
#     'A': 7,
#     'B': 6,
#     'C': 2,
#     'D': 1,
#     'E': 3,
#     'F': 4,
#     'G': 0,
#     'H': 5,
#     'I': 8,
#     'J': 9
# }

# # Graph adjacency list with edge weights
# graph = {
#     'A': {'B': 1, 'C': 4},

#     'B': {'A': 1, 'D': 2, 'E': 5},
#     'C': {'A': 4, 'F': 3},
#     'D': {'B': 2, 'G': 1},
#     'E': {'B': 5, 'H': 2},
#     'F': {'C': 3, 'I': 6},
#     'G': {'D': 1, 'J': 2},
#     'H': {'E': 2, 'J': 3},
#     'I': {'F': 6, 'J': 1},
#     'J': {'G': 2, 'H': 3, 'I': 1}
# }

import heapq

# Heuristic values (h)
heuristic = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3,
    'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
}

# Graph adjacency list with edge weights
graph = {
    'A': {'B': 6, 'D': 2, 'F': 3},
    'B': {'A': 6, 'C': 3, 'D': 1},
    'C': {'B': 3, 'E': 5},
    'D': {'A': 2, 'B': 1, 'E': 8, 'G': 7},
    'E': {'C': 5, 'D': 8, 'J': 5},
    'F': {'A': 3, 'G': 1, 'H': 7},
    'G': {'D': 7, 'F': 1, 'I': 3},
    'H': {'F': 7, 'I': 2},
    'I': {'G': 3, 'H': 2, 'J': 3},
    'J': {'E': 5, 'I': 3}
}

def astar(graph, start, goal, heuristic):
    # Priority queue: (f, g, node, path)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    
    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        # Goal reached
        if node == goal:
            return path, g

        # Explore neighbors
        for neighbor, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
    
    return None, float('inf')


# Example Run
path, cost = astar(graph, 'A', 'J', heuristic)
print("Shortest Path using A*:", path)
print("Total Cost:", cost)