function dailyTemperatures(temperatures: number[]): number[] {
    interface data {
        index: number;
        temp: number;
    }
    
    const stack = [];
    const ans = [];
    
    for (let i = 0; i < temperatures.length; i++) {
        while (stack.length && (stack[stack.length - 1].temp < temperatures[i])) {
            const poppedData = stack.pop();
            ans[poppedData.index] = i - poppedData.index;
        }
        stack.push({index: i, temp: temperatures[i]});
    }
    while (stack.length) {
        const popped = stack.pop();
        ans[popped.index] = 0;
    }
    return ans;
};
