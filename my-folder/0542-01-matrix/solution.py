from queue import Queue

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = Queue()
        out_mat = [[-1 for cell in row] for row in mat]
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                if cell == 0:
                    out_mat[r][c] = 0
                    q.put([r, c])
        while not q.empty():
            pos = q.get()
            val = out_mat[pos[0]][pos[1]]
            adjacent_positions = self.getAdjacentPositions(mat, pos)
            for adj_pos in adjacent_positions:
                r = adj_pos[0]
                c = adj_pos[1]
                if out_mat[r][c] == -1:
                    out_mat[r][c] = val + 1
                    q.put([r, c])
    
        return out_mat

    def getAdjacentPositions(self, mat, pos):
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_row = len(mat) - 1
        max_col = len(mat[0]) - 1
        valid_positions = []
        for move in moves:
            row = pos[0] + move[0]
            col = pos[1] + move[1]
            if 0 <= row <= max_row and 0 <= col <= max_col:
                valid_positions.append([row, col])
        return valid_positions

