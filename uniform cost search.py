import heapq

# Uniform Cost Search
def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = {}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        # Goal found
        if current == goal:
            return path, cost

        # Visit neighboring nodes
        for neighbor, weight in graph[current]:
            if neighbor not in visited or cost + weight < visited[neighbor]:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None, float('inf')


# Main Program
print("===== UNIFORM COST SEARCH =====")

n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))
print("Enter edges (source destination cost):")

for i in range(e):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))

# Perform UCS
path, cost = ucs(graph, start, goal)

# Display result
if path is not None:
    print("\nGoal Found!")
    print("Path:", " -> ".join(map(str, path)))
    print("Total Cost:", cost)
else:
    print("\nGoal not found.")