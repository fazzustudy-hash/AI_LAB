# State Space Representation

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

visited = []

def search(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        if node == 'G':
            print("\nGoal State Reached!")
            return True

        for neighbour in graph[node]:
            if search(neighbour):
                return True

    return False

# Initial State
search('A')
