from queue import Queue

class Bip:

 def is_bipartite(adj_matrix):
    
    colors = {}

    q = Queue()
    for i in range(len(adj_matrix)):
        colors[i] = None
    for start in range(len(adj_matrix)):
     
        if colors[start] is None:
            colors[start] = 0
            q.put(start)    

            
            while not q.empty():
                curr = q.get()
                for neighbor in range(len(adj_matrix)):
                    if adj_matrix[curr][neighbor] == 1:
                        if colors[neighbor] == colors[curr]:
                            return False
                        elif colors[neighbor] is None:
                            colors[neighbor] = 1 - colors[curr]
                            q.put(neighbor)

    return True


 def is_connected(adj_matrix):
    
    visited = [False] * len(adj_matrix)
    def bfs(start):
        visited[start] = True
        q = Queue()
        q.put(start)

        while not q.empty():
            curr = q.get()
            for neighbor in range(len(adj_matrix)):
                if adj_matrix[curr][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    q.put(neighbor)

    
    bfs(0)

    
    return all(visited)




