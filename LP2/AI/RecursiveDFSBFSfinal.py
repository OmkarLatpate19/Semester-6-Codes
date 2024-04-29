# Define a function for Depth First Search (DFS)
def dfs_recursive(visited, graph, node):
    # If the node has not been visited
    if node not in visited:
        # Print the node
        print(node, end=" ")
        # Mark the node as visited
        visited.add(node)
        # Explore all neighbors of the current node recursively
        for neighbour in graph[node]:
            dfs_recursive(visited, graph, neighbour)

# Define a function for Breadth First Search (BFS)
def bfs_recursive(visited, graph, queue):
    # Base case: if the queue is empty, BFS is complete
    if not queue:
        return
    else:
        # Dequeue a node from the queue
        node = queue.pop(0)
        # Print the dequeued node
        print(node, end=" ")
        # Mark the dequeued node as visited
        visited.add(node)
        # Enqueue all unvisited neighbors of the dequeued node
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    # Recursive call to explore the next level of nodes
    bfs_recursive(visited, graph, queue)

# Main function
def main():
    visited_dfs = set()  # To keep track of DFS visited nodes
    visited_bfs = set()  # To keep track of BFS visited nodes
    queue = []           # For BFS

    # Input the number of nodes in the graph
    n = int(input("Enter the number of nodes: "))
    graph = {}  # Initialize an empty dictionary to represent the graph

    # Input the edges for each node
    for i in range(1, n+1):
        edges = int(input("Enter the number of edges for node {}: ".format(i)))
        graph[i] = []  # Initialize an empty list for the edges of the current node
        for j in range(1, edges+1):
            # Input the edges for the current node
            node = int(input("Enter edge {} for node {}: ".format(j, i)))
            graph[i].append(node)

    print("DFS Traversal:")
    # Perform DFS traversal starting from node 1
    dfs_recursive(visited_dfs, graph, 1)
    print()

    print("BFS Traversal:")
    # Enqueue the starting node for BFS traversal
    queue.append(1)
    # Perform BFS traversal starting from node 1
    bfs_recursive(visited_bfs, graph, queue)

if __name__ == "__main__":
    main()
