class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                # (i, j) represents the top left corners of the 4 possible 2x2 matrices
                blacks = 0
                for x in range(2):
                    for y in range(2):
                        # (i + x, j + y) represents the 4 squares in the 2x2 matrix
                        if grid[i + x][j + y] == "B":
                            blacks += 1
                if blacks != 2:
                    return True
        return False
                    
