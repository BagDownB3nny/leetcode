import queue

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        q = queue.Queue()
        visited = set()
        q.put(source)
        visited.add(source)
        while not q.empty():
            node = q.get()
            for edge in edges:
                if edge[0] == node and edge[1] not in visited:
                    if edge[1] == destination:
                        return True
                    q.put(edge[1])
                    visited.add(edge[1])
                if edge[1] == node and edge[0] not in visited:
                    if edge[0] == destination:
                        return True
                    q.put(edge[0])
                    visited.add(edge[0])
        return False
                    
            
