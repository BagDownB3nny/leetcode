import java.util.HashMap;

// class Solution {
//     HashMap<Integer, Integer> memo;

//     public int helper(int[] coins, int amount) {
//         if (amount == 0) {
//             return 0;
//         } else if (amount < 0) {
//             return -1;
//         } else if (memo.containsValue(amount)) {
//             return memo.get(amount);
//         }
//         int min = -1;
//         for (int i = 0; i < coins.length; i += 1) {
//             int smallerProblem = helper(coins, amount - coins[i]);
//             if (smallerProblem != -1 && min == -1) {
//                 min = smallerProblem;
//             } else if (smallerProblem < min && smallerProblem != -1) {
//                 min = smallerProblem;
//             }
//         }
//         System.out.println(memo);
//         if (min == -1) {
//             memo.put(amount, -1);
//             return min;
//         } else {
//             int x = min + 1;
//             memo.put(amount, min + 1);
//             return min + 1;
//         }
//     }
    
//     public int coinChange(int[] coins, int amount) {
//         memo = new HashMap<>();
//         return helper(coins, amount);
//     }
// }

public class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount<1) return 0;
        return helper(coins, amount, new int[amount]);
    }

    private int helper(int[] coins, int rem, int[] count) { // rem: remaining coins after the last step; count[rem]: minimum number of coins to sum up to rem
        if(rem<0) return -1; // not valid
        if(rem==0) return 0; // completed
        if(count[rem-1] != 0) return count[rem-1]; // already computed, so reuse
        int min = Integer.MAX_VALUE;
        for(int coin : coins) {
            int res = helper(coins, rem-coin, count);
            if(res>=0 && res < min)
                min = 1+res;
        }
        count[rem-1] = (min==Integer.MAX_VALUE) ? -1 : min;
        return count[rem-1];
    }
}
