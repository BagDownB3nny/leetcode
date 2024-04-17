function orangesRotting(grid: number[][]): number {
    interface data {
        row: number;
        col: number;
    }
    
    let fresh = 0;
    let rottenOranges: data[] = [];
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] == 2) {
                rottenOranges.push({row: row, col: col});
            } else if (grid[row][col] == 1) {
                fresh++;
            }
        }
    }
    let count = 0;
    
    while (rottenOranges.length && fresh) {
        const newRottenOranges = [];
        for (const rotten of rottenOranges) {
            const rottenRow = rotten.row;
            const rottenCol = rotten.col;
            if (rottenRow + 1 < grid.length && grid[rottenRow + 1][rottenCol] == 1) {
                newRottenOranges.push({row: rottenRow + 1, col: rottenCol});
                grid[rottenRow + 1][rottenCol] = 2;
                fresh--;
            }
            if (rottenCol + 1 < grid[0].length && grid[rottenRow][rottenCol + 1] == 1) {
                newRottenOranges.push({row: rottenRow, col: rottenCol + 1});
                grid[rottenRow][rottenCol + 1] = 2;
                fresh--;
            }
            if (rottenRow - 1 >= 0 && grid[rottenRow - 1][rottenCol] == 1) {
                newRottenOranges.push({row: rottenRow - 1, col: rottenCol});
                grid[rottenRow - 1][rottenCol] = 2;
                fresh--;
            }
            if (rottenCol - 1 >= 0 && grid[rottenRow][rottenCol - 1] == 1) {
                newRottenOranges.push({row: rottenRow, col: rottenCol - 1});
                grid[rottenRow][rottenCol - 1] = 2;
                fresh--;
            }
        }
        rottenOranges = newRottenOranges;
        count++;
    }
    if (fresh) {
        return -1;
    } else {
        return count;
    }
};
