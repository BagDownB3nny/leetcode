class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        rows = len(grid)
        isFlippedArr = [True for _ in grid]
        
        for i, row in enumerate(grid):
            isFlippedArr[i] = not row[0]

        power = n - 1
        for i in range(n):
            ones = 0
            zeroes = 0
            for j, row in enumerate(grid):
                if (row[i] and not isFlippedArr[j]) or (not row[i] and isFlippedArr[j]):
                    ones += 1
                else:
                    zeroes += 1
            ans += max(ones, zeroes) * pow(2, power)
            power -= 1
                
        return ans
            
