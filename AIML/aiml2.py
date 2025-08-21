# A* Algorithm
# f(n) = g(n) + h(n)
# f(n) is the estimated cost of the cheapest and shortest path
# g(n) is the cost of the path from the start node to n
# h(n) is the estimated cost from n to the goal node
import heapq

heap = []

heapq.heappush(heap,20)
heapq.heappush(heap,5) 
heapq.heappush(heap,15) 
heapq.heappush(heap,10) 

print(heap)  # Output: [5, 10, 15, 20] 

# pop the smallest element
print(heapq.heappop(heap))  # Output: 5

# peek at the smallest element
print(heap[0])  # Output: 10

# convert a list into a heap
numbers = [20, 5, 15, 10]
heapq.heapify(numbers)
print(numbers)  # Output: [5, 10, 15, 20]

#Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 4,
    'G': 0,
    'H': 5,
    'I': 8,
    'J': 9
}

# Graph adjacency list with edge weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 1},
    'E': {'B': 5, 'H': 2},
    'F': {'C': 3, 'I': 6},
    'G': {'D': 1, 'J': 2},
    'H': {'E': 2, 'J': 3},
    'I': {'F': 6, 'J': 1},
    'J': {'G': 2, 'H': 3, 'I': 1}
}