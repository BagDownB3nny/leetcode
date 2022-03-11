import java.util.Hashtable;

class Solution {
    Hashtable<Integer, Integer> h = new Hashtable<>();
    public int combinationSum4(int[] nums, int target) {
        if (h.get(target) != null) {
            return h.get(target);
        }
        if (target == 0) {
            return 1;
        } else if (target < 0) {
            return 0;
        }
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            ans += combinationSum4(nums, target - nums[i]);
        }
        h.put(target, ans);
        return ans;
    }
}
