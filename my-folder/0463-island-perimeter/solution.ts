function islandPerimeter(grid: number[][]): number {
    let perimeter = 0;

    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[row].length; col++) {
            if (grid[row][col] === 1) {
                if (row - 1 < 0 || grid[row - 1][col] == 0) {
                    perimeter++;
                }
                if (col - 1 < 0 || grid[row][col - 1] == 0) {
                    perimeter++;
                }
                if (row + 1 == grid.length || grid[row + 1][col] == 0) {
                    perimeter++;
                }
                if (col + 1 == grid[0].length || grid[row][col + 1] == 0) {
                    perimeter++;
                }
            }
        }
    }
    return perimeter;
};
