import java.util.Hashtable;

class Solution {
    static Hashtable<Integer, Integer> h = new Hashtable<>();
    public int climbStairs(int n) {
        if (n==0) {
            return 1;
        } else if (n < 0) {
            return 0;
        } else {
            int x;
            int y;
            Integer xs = h.get(n-1);
            Integer ys = h.get(n-2);
            if (xs != null) {
                x = xs;
            } else {
                x = climbStairs(n-1);
                h.put(n-1, x);
            }
            if (ys != null) {
                y = ys;
            } else {
                y = climbStairs(n-2);
                h.put(n-2, y);
            }
            return x + y;
        }
    }
}
