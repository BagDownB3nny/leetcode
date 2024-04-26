class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        optimal = [[-1 for _ in range(n)] for _ in range(n)]
        ans = -1
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if i == 0:
                    optimal[i][j] = cell
                else:
                    optimalCell = -1
                    for col, aboveCell in enumerate(optimal[i - 1]):
                        if (optimalCell == -1 or aboveCell < optimalCell) and col != j:
                            optimalCell = aboveCell
                    optimal[i][j] = optimalCell + cell
                if i == n - 1:
                    if optimal[i][j] < ans or ans == -1:
                        ans = optimal[i][j]
        return ans
