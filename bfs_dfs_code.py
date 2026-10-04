from collections import deque
import timeit

def create_graph(depth):
    graph = {}
    total_nodes = (2 ** (depth + 1)) - 1

    for i in range(total_nodes):
        graph[i] = []
        left = 2 * i + 1
        right = 2 * i + 2

        if left < total_nodes:
            graph[i].append(left)
        if right < total_nodes:
            graph[i].append(right)

    return graph


def bfs(graph, start, target):
    queue = deque([start])
    visited = {start}
    nodes_explored = 0

    while queue:
        node = queue.popleft()
        nodes_explored += 1

        if node == target:
            return nodes_explored

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return nodes_explored


def dfs(graph, start, target):
    stack = [start]
    visited = {start}
    nodes_explored = 0

    while stack:
        node = stack.pop()
        nodes_explored += 1

        if node == target:
            return nodes_explored

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return nodes_explored


depth = 10
graph = create_graph(depth)
start = 0
target = 2 ** depth - 1
runs = 1000

bfs_time = timeit.timeit(
    lambda: bfs(graph, start, target),
    number=runs
)

dfs_time = timeit.timeit(
    lambda: dfs(graph, start, target),
    number=runs
)

bfs_average = (bfs_time / runs) * 1000
dfs_average = (dfs_time / runs) * 1000

bfs_nodes = bfs(graph, start, target)
dfs_nodes = dfs(graph, start, target)

print("SLE-2: BFS vs DFS Performance Analysis")
print("----------------------------------------")
print("Total graph nodes:", len(graph))
print("Target node:", target)

print("\nBFS Results")
print("Nodes explored:", bfs_nodes)
print("Average time (ms):", round(bfs_average, 6))

print("\nDFS Results")
print("Nodes explored:", dfs_nodes)
print("Average time (ms):", round(dfs_average, 6))
