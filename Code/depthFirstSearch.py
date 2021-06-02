def depthFirstSearch(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)
    
    while stack:
        curr = stack.pop()
        print(curr)

        for child in graph[curr]:

            if child not in visited:
                visited.append(child)
                stack.append(child) 

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

depthFirstSearch(graph, 'A')

