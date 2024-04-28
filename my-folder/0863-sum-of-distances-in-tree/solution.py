class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        closest = [0 for _ in range(n)]
        
        
        visited = set()
        def dfs(cur):
            nonlocal visited, ans, closest
            if cur not in visited:
                visited.add(cur)
                closestNodes = 1
                for child in graph[cur]:
                    closestChildNodes = dfs(child)
                    closestNodes += closestChildNodes
                ans[0] += closestNodes
                closest[cur] = closestNodes
                return closestNodes
            else:
                return 0
         
        dfs(0)
        
        def dfs2(cur, parentBase):
            nonlocal visited, ans, closest
            if cur not in visited:
                visited.add(cur)
                nodeAns = parentBase - closest[cur] + (n - closest[cur])
                ans[cur] = nodeAns
                for child in graph[cur]:
                    dfs2(child, nodeAns)
                    
        visited = set()
        dfs2(0, ans[0])
        return ans
            
            
                
