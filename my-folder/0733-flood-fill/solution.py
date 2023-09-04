class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        filled = set()
        to_fill = [[sr, sc]]
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        original_color = image[sr][sc]

        while len(to_fill) > 0:
            cell = to_fill.pop()
            row = cell[0]
            col = cell[1]
            if (image[row][col] != original_color):
                continue
            if (row, col) in filled:
                continue
            else:
                filled.add((row, col))
            image[row][col] = color
            print("ADD")
            for move in moves:
                adjacent_tile = [row + move[0], col + move[1]]
                if self.isValidTile(image, adjacent_tile):
                    to_fill.append(adjacent_tile)
        return image

            

    def isValidTile(self, image, cell):
        row = cell[0]
        col = cell[1]
        rows = len(image)
        cols = len(image[0])
        return 0 <= row < rows and 0 <= col < cols

