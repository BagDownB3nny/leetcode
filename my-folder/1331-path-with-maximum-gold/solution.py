import copy

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:  
        m = len(grid)
        n = len(grid[0])
        
        def dfs(grid, i, j):
            nonlocal m, n
            
            if i < 0 or i == m or j < 0 or j == n:
                return 0
            if not grid[i][j]:
                return 0
            newGrid = copy.deepcopy(grid)
            newGrid[i][j] = 0
            ans = max(dfs(newGrid, i - 1, j), dfs(newGrid, i + 1, j), dfs(newGrid, i, j - 1), dfs(newGrid, i, j + 1))
            ans += grid[i][j]
            return ans
            
                                
            
        maxGold = 0
        gold = 0
        
        for i in range(m):
            for j in range(n):
                gold += grid[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxGold = max(maxGold, dfs(grid, i, j))
                    if maxGold == gold:
                        return maxGold
        return maxGold
