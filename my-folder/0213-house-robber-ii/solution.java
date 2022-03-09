import java.util.Hashtable;

class Solution {
    public int rob(int[] nums) {
        class P {
            Hashtable<Integer, Integer> h = new Hashtable<>();
            int prob(int[] nums, int start, boolean firstHouseRobbed) {
                int x;
                int y;
                Integer xs;
                Integer ys;
                if (firstHouseRobbed) {
                    if (start >= nums.length - 1) {
                        return 0;
                    }
                    xs = h.get(-start - 1);
                    if (xs != null) {
                        x = xs;
                    } else {
                        x = prob(nums, start + 1, true);
                        h.put(-start - 1, x);
                    } 
                    ys = h.get(-start - 2);
                    if (ys != null) {
                        y = ys + nums[start];
                    } else {
                        y = prob(nums, start + 2, true);
                        h.put(-start - 2, y);
                        y = y + nums[start];
                    } 
                } else {
                    if (start >= nums.length) {
                        return 0;
                    }
                    xs = h.get(start + 1);
                    if (xs != null) {
                        x = xs;
                    } else {
                        x = prob(nums, start + 1, false);
                        h.put(start + 1, x);
                    }
                    if (start == 0) {
                        ys = h.get(-start - 2);
                        if (ys != null) {
                            y = ys + nums[start];
                        } else {
                            y = prob(nums, start + 2, true);
                            h.put(-start - 2, y);
                            y = y + nums[start];
                        }
                    } else {
                        ys = h.get(start + 2);
                        if (ys != null) {
                            y = ys + nums[start];
                        } else {
                            y = prob(nums, start + 2, false);
                            h.put(start + 2, y);
                            y = y + nums[start];
                        }
                    }
                }
                return Math.max(x, y);
            }
        }
        P p = new P();
        return p.prob(nums, 0, false);
    }
}
