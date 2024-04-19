function numIslands(grid: string[][]): number {
    interface cell {
        row: string;
        col: string;
    }
    const map = new Map();
    let ans = 0;
    
    const genKey = (row, col) => {
        return row.toString() + " " + col.toString();
    }
    
    const dfs = (row: number, col: number) => {
        const queue = [{row: row, col: col}];
        while (queue.length) {
            const data = queue.shift();
            if (data.row + 1 < grid.length && grid[data.row + 1][data.col] == "1" && !map.get(genKey(data.row + 1, data.col))) {
                queue.push({row: data.row + 1, col: data.col});
                map.set(genKey(data.row + 1, data.col), true);
            }
            if (data.row - 1 >= 0 && grid[data.row - 1][data.col] == "1" && !map.get(genKey(data.row - 1, data.col))) {
                queue.push({row: data.row - 1, col: data.col});
                map.set(genKey(data.row - 1, data.col), true);
            }
            if (data.col + 1 < grid[0].length && grid[data.row][data.col + 1] == "1" && !map.get(genKey(data.row, data.col + 1))) {
                queue.push({row: data.row, col: data.col + 1});
                map.set(genKey(data.row, data.col + 1), true);
            }
            if (data.col - 1 >= 0 && grid[data.row][data.col - 1] == "1" && !map.get(genKey(data.row, data.col - 1))) {
                queue.push({row: data.row, col: data.col - 1});
                map.set(genKey(data.row, data.col - 1), true);
            }
        }
    }
    
    
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] == "1" && !map.get(genKey(row, col))) {
                dfs(row, col);
                ans++;
            }
        }
    }
    return ans;
 }
