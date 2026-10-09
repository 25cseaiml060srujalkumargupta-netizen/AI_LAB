def bfs(graph,start_node):
    visited = []
    queue = [start_node]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"exploring node: {current_node}")
            visited.append(current_node)
            #.get() prevents error if a node has no outgoing edges
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    return visited


                # --- USER INPUT SECTION --
print("--- BUILD YOUR GRAPH ---")
student_graph = {}

                # GET THE TOTAL NUMBER OF CONNECTIONS
num_edges = int(input("How many edges (connections) does your graph have"))
print("enter each edge separeted by a space (e.g.,A B):")
for i in range(num_edges):
                    #Read the input and split it into two variables
    u, v = input(f"Edge{i+1}: ").split()


    # Initialize the lists if the nodes don't exist yet
    if u not in student_graph:
        student_graph[u]=[]
    if v not in student_graph:
        student_graph[v] = [v]


                            #ADD THE CONNECTION (UNDIRECTED GRAPH)
    student_graph[u].append(v)
    student_graph[v].append(u)

                            #GET THE STARTING POINT
start = input("Enter the starting mode for BFS: ")

print(f"\nYour Graph Dictionary:m{student_graph}")
print("starting BFS Traversal...")

bfs(student_graph,start) 

