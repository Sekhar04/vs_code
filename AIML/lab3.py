# AO* Algorithm Implementation
# Heuristic values
H = {
    'A': -1, 'B': 5, 'C': 2, 'D': 4,
    'E': 7, 'F': 9, 'G': 3, 'H': 0,
    'I': 0, 'J': 0
}

# Conditions (AND-OR graph representation)
Conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}


# Cost Function

def Cost(H, condition, weight=1):
    cost = {}

    # If AND condition exists
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)  # Path label
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    # If OR condition exists
    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B = ' OR '.join(OR_nodes)  # Path label
        PathB = min(H[node] + weight for node in OR_nodes)
        cost[Path_B] = PathB

    return cost


# Update Cost Function
def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse()  # Process from bottom-up
    least_cost = {}

    for key in Main_nodes:
        condition = Conditions[key]
        print(key, ":", condition, "------->", Cost(H, condition, weight))
        c = Cost(H, condition, weight)

        # update heuristic with minimum cost
        H[key] = min(c.values())
        least_cost[key] = Cost(H, condition, weight)

    return least_cost



# Shortest Path Function

def shortest_path(Start, Updated_cost, H):
    Path = Start

    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)

        # FIND MINIMUM PATH KEY
        Next = key[Index].split()

        # ADD TO PATH FOR OR PATH
        if len(Next) == 1:
            Start = Next[0]
            Path += ' = ' + shortest_path(Start, Updated_cost, H)
        else:
            Path += ' = (' + key[Index] + ')'
            Start = Next[0]
            Path += ' [' + shortest_path(Start, Updated_cost, H) + ' + '
            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, H) + ']'

    return Path



# MAIN PROGRAM

print("Initial Heuristic:", H)
result = update_cost(H, Conditions)
print("\nUpdated Heuristic:", H)
print("\nFinal Least Cost of Each Node:", result)

print("\nShortest Path from A:")
print(shortest_path('A', result, H))

# Hill Climbing Algorithm Implementation