class BFS: 
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.visited = set()
        self.queue = [start]
        self.visited.add(start)
        self.parent = {start: None}
        
    def run(self, target):
        while self.queue: 
            node = self.queue.pop(0)
            if node == target:
                print('\nFound', node)
                return self._reconstruct_path(target)
            
            print(node, end = " ")
            
            for neighbor in self.graph[node]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.queue.append(neighbor)
                    self.parent[neighbor] = node
                    
        print('Not Found')
        return None 
    
    def _reconstruct_path(self, target):
        path = []
        while target is not None:
            path.append(target)
            target = self.parent[target]
        path.reverse()
        return path


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

bfs = BFS(graph, "A")
result = bfs.run("E")
print(result)