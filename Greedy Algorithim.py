def dijkstra_with_path(graph, s, d):
    best = {node: float('inf') for node in graph}
    from_node = {node: None for node in graph}  
    best[s] = 0
    
    known = set()
    done = set()
    todo = s
    
    while len(done) < len(graph):
        for b in graph[todo]:
            new_distance = best[todo] + graph[todo][b]
            
            if new_distance < best[b]:
                best[b] = new_distance
                from_node[b] = todo  
                known.add(b)
        
        done.add(todo)
        
        next_todo = None
        smallest = float('inf')
        for node in (known - done):
            if best[node] < smallest:
                smallest = best[node]
                next_todo = node
        
        if next_todo is None:
            break
        todo = next_todo
    

    path = []
    current = d
    while current is not None:
        path.append(current)
        current = from_node[current]
    path.reverse()  
    
    return best[d], path


graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 3},
    'C': {'B': 1, 'D': 7},
    'D': {}
}

distance, path = dijkstra_with_path(graph, 'A', 'D')
print(f"Distance: {distance}, Path: {path}")
