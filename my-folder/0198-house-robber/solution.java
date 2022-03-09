import java.util.Hashtable;

class Solution {
    public int rob(int[] nums) {
        class P {
            Hashtable<Integer, Integer> h = new Hashtable<>();
            int prob(int[] nums, int start) {
                if (start >= nums.length) {
                    return 0;
                }
                Integer xs = h.get(start + 1);
                int x;
                if (xs != null) {
                    x = xs;
                } else {
                    x = prob(nums, start + 1);
                    h.put(start + 1, x);
                }
                Integer ys = h.get(start + 2);
                int y;
                if (ys != null) {
                    y = ys + nums[start];
                } else {
                    y = prob(nums, start + 2) + nums[start];
                    h.put(start + 2, y);
                }
                return Math.max(x, y);
            }
        }
        P p = new P();
        return p.prob(nums, 0);
    }
}
