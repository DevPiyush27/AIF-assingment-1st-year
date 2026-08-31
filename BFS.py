
graph = {
    1: [2, 3],      
    2: [4, 5],      
    3: [6],         
    4: [7, 8],   
    5: [9],      
    6: [10],         
    7: [],
    8: [],
    9: [],
    10: []
}


queue = []


visited = set()


start = 1


queue.append(start)
visited.add(start)

print("BFS Traversal:")


while queue:
   
    node = queue.pop(0)

   
    print(node, end=" ")

    
    for neighbour in graph[node]:
    
        if neighbour not in visited:
           
            visited.add(neighbour)
            queue.append(neighbour)