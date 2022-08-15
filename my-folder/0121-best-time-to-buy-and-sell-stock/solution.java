class Solution {
    public int maxProfit(int[] prices) {
        int currentLowest = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < currentLowest) {
                currentLowest = prices[i];
            } else if (prices[i] - currentLowest > maxProfit) {
                maxProfit = prices[i] - currentLowest;
            }
        }
        return maxProfit;
    }
}
