graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 9,
    'H': 0
}

visited = []
queue = ['A']

goal = 'H'

while queue:

    # heuristic ke hisaab se sort karo
    queue.sort(key=lambda x: heuristic[x])

    current = queue.pop(0)

    if current not in visited:
        print(current, end=" ")
        visited.append(current)

        if current == goal:
            print("\nGoal Found")
            break

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                
                
