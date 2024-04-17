function trap(height: number[]): number {
    let start = 0;
    let end = height.length - 1;
    let highestLeft = height[start];
    let highestRight = height[end];
    let ans = 0;
    while (start < end) {
        if (highestLeft <= highestRight) {
            start++;
            if (height[start] > highestLeft) {
                highestLeft = height[start];
            } else {
                ans += highestLeft - height[start];
            }
        } else {
            end--;
            if (height[end] > highestRight) {
                highestRight = height[end];
            } else {
                ans += highestRight - height[end];
            }
        }
    }
    return ans;
};
