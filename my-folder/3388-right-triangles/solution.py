class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rowCounter = [0 for row in range(rows)]
        colCounter = [0 for col in range(cols)]
        corners = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    rowCounter[i] += 1
                    colCounter[j] += 1
                    corners.append((i,j))
                    
        ans = 0
        for corner in corners:
            ans += (rowCounter[corner[0]] - 1) * (colCounter[corner[1]] - 1)
        return ans
        
