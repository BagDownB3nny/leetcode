from queue import Queue
import copy

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        safety = [[-1 for _ in range(n)] for _ in range(n)]
        q = Queue() 
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.put([i, j, 0])
                    safety[i][j] = 0
                    
        def validCell(i, j):
            return i >= 0 and j >= 0 and i < n and j < n
        
        while not q.empty():
            cell = q.get()
            increments = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for increment in increments:
                i = cell[0] + increment[0]
                j = cell[1] + increment[1]
                if validCell(i, j) and safety[i][j] == -1:
                    safety[i][j] =  cell[2] + 1
                    q.put([i, j, cell[2] + 1])
        
        base = min(safety[0][0], safety[n - 1][n - 1])
        newQ = [[0, 0]]
        standbyQ = []
        while base > 0:
            while len(newQ):
                cell = newQ.pop()
                if safety[cell[0]][cell[1]] == -1:
                    continue
                safety[cell[0]][cell[1]] = -1
                if cell[0] == n - 1 and cell[1] == n - 1:
                    return base
                increments = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for increment in increments:
                    i = cell[0] + increment[0]
                    j = cell[1] + increment[1]
                    if not validCell(i, j) or safety[i][j] == -1:
                        continue
                    elif safety[i][j] >= base:
                        newQ.append([i, j])
                    else:
                        standbyQ.append([i, j])
            base -= 1
            newQ = copy.deepcopy(standbyQ)
            standbyQ = []
            
        return 0
