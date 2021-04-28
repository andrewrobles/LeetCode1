def breadthFirstSearch(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)
    
    while queue:
        curr = queue.pop(0)
        print(curr)

        for child in graph[curr]:

            if child not in visited:
                visited.append(child)
                queue.append(child) 