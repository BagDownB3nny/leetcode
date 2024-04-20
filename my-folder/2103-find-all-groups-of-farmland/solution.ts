function findFarmland(land: number[][]): number[][] {    
    const isNewFarmland = (row: number, col: number) => {
        return (row >= 0 && row < land.length && col >= 0 && col < land[0].length && land[row][col]);
    }
    
    const getFarmland = (r1, c1) => {
        let r2 = r1;
        let c2 = c1;
        while (isNewFarmland(r2, c1)) {
            r2++;
        }
        while (isNewFarmland(r1, c2)) {
            c2++;
        }
        for (let row = r1; row < r2; row++) {
            for (let col = c1; col < c2; col++) {
                land[row][col] = 0;
            }
        }
        return [r1, c1, r2 - 1, c2 - 1];
    }
    
    let ans = [];
    
    for (let row = 0; row < land.length; row++) {
        for (let col = 0; col < land[0].length; col++) {
            if (isNewFarmland(row, col)) {
                const newFarmland = getFarmland(row, col);
                ans.push(newFarmland);
            }
        }
    }
    return ans;
};
