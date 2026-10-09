def get_user_inputs():
    #1.take inputs for heuristic values
    heuristic = {}
    num_nodes = int(input("enter total number of nodes: "))
    print("\nEnter Heuristic value h(n) for each node:")
    for _ in range(num_nodes):
        node = input(" Node name: ").strip().upper()
        h_val = float(input(f" Heuristic h({node}): "))
        heuristic[node] = h_val
    #2.take input for graph edges
    graph = {node: [] for node in heuristic}
    num_edges = int(input("\nEnter total number of directed edges: "))
    print("\nEnter edges in format (from_node to_node weight)")
    for i in range(num_edges):
        u, v, w = input(f" Edge {i+1}: ").strip().split()
        weight = float(w)
        graph[u].append((v,weight))

    return graph, heuristic
def astar(graph, heuristic, start,goal):
    open_list = [(start,0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        # Select mpde with minimum f = g + h
        current = min(open_list, key=lambda x: x[1] + heuristic[x[0]])
        open_list.remove(current)

        current_node = current[0]

        #Goal check & path reconstruction
        if current_node == goal:
            path = [goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_cost[goal]

    #Neighbor exploration
    for neighbor, cost in graph.get(current_node, []):
        new_cost = g_cost[current_node] + cost

        if neighbor not in g_cost or new_cost < g_cost[neighbor ]:
            g_cost[neighbor] = new_cost
            came_from[neighbor] = current_node
            open_list.append((neighbor, new_cost))
    return None, float('inf')   
# --Main Driver Program--
if __name__ == "__main__":
    print("===A* Algorithm Input Setup ===\n")
    graph, heuristic = get_user_inputs()
    print("\n--- Path Finding ---")
    start = input("Enter Start Node: ").Strip().upper()
    goal = input("Enter Goal Node: ").strip().upper()
    path, cost = astar(graph, heuristic, start, goal)
    print("\n=== Result ===")
    if Path:
        print("Shortest Path:","->".join(path))
        print("Total Path Cost:", cost)
    else:
        print("Path not found.")