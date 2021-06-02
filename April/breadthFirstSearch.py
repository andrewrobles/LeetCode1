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

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

breadthFirstSearch(graph, 'A')