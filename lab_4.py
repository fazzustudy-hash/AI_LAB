from heapq import heappush, heappop

def a_star(graph, heuristic, start, goal):
    

    print("Initial State:", start)
    print("Goal State:", goal)

    print("\nHeuristic Values:")
    for node in heuristic:
        print(f"h({node}) = {heuristic[node]}")

    print("\nSearch Process:")

    # Priority Queue: (f_cost, g_cost, node, path)
    open_list = []

    # f(n) = g(n) + h(n)
    heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = {}

    while open_list:

        f_cost, g_cost, current, path = heappop(open_list)

        print(
            f"Current Node: {current}, "
            f"Path: {' -> '.join(path)}, "
            f"g(n) = {g_cost}, "
            f"h(n) = {heuristic[current]}, "
            f"f(n) = {f_cost}"
        )

        # Goal reached
        if current == goal:
            return path, g_cost

        # Skip if already visited with lower cost
        if current in visited and visited[current] <= g_cost:
            continue

        visited[current] = g_cost

        # Explore neighbors
        for neighbor, cost in graph[current]:

            new_g = g_cost + cost
            new_f = new_g + heuristic[neighbor]

            print(
                f"    {current} -> {neighbor} | "
                f"Cost = {cost}, "
                f"g({neighbor}) = {new_g}, "
                f"h({neighbor}) = {heuristic[neighbor]}, "
                f"f({neighbor}) = {new_f}"
            )

            heappush(
                open_list,
                (new_f, new_g, neighbor, path + [neighbor])
            )

    return None, float('inf')




graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}




heuristic = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}


# -------------------------------
# Initial and Goal State
# -------------------------------

start = 'A'
goal = 'G'


# -------------------------------
# A* Search
# -------------------------------

path, cost = a_star(graph, heuristic, start, goal)


# -------------------------------
# Final Result
# -------------------------------

print("\n==============================")
print("FINAL RESULT")
print("==============================")

if path:
    print("Initial State :", start)
    print("Goal State    :", goal)
    print("Shortest Path :", " -> ".join(path))
    print("Total Cost    :", cost)
else:
    print("No path found.")
