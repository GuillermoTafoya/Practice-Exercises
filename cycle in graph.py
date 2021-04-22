def cycleInGraph(edges):
    if not edges:
        return
    queue = [[0,edges[0]]]
    visited = set()
    print(queue)

    while queue:
        idx,current = queue.pop(0)
        visited.add(idx)
        for node in current:
            if node in visited:
                return True
            queue.append([node,edges[node]])
            
    return False

inp = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]

print(cycleInGraph(inp))