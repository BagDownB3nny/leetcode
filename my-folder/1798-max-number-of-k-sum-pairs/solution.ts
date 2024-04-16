function maxOperations(nums: number[], k: number): number {
    interface hashmap {
        [n: number]: number;
    }
    const newMap: hashmap = {};
    for (const n of nums) {
        if (!newMap[n]) {
            newMap[n] = 1;
        } else {
            newMap[n] = newMap[n] + 1;
        }
    }
    
    let ans = 0;
    for (const n of Object.keys(newMap)) {
        const pair = k - parseInt(n);
        if (newMap[pair]) {
            ans += Math.min(newMap[n], newMap[pair]);
        }
    }
    return Math.floor(ans / 2);
};
