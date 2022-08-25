import java.util.HashMap;

class Solution {
    HashMap<Integer, Integer> memo = new HashMap<>();
    
    public int climbStairs(int n) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }  else if (n == 1) {
            return 1;
        } else if (n == 0) {
            return 1;
        } else {
            int ans = climbStairs(n - 1) + climbStairs(n - 2);
            memo.put(n, ans);
            return ans;
        }
    }
}
