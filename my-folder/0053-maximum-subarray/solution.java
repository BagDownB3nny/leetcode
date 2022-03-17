class Solution {
    public int maxSubArray(int[] nums) {
        int max = 0;
        int section = 0;
        int greatestNegative = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > greatestNegative && nums[i] <= 0) {
                greatestNegative = nums[i];
            }
            section += nums[i];
            if (section < 0) {
                section = 0;
                continue;
            }
            if (section > max) {
                max = section;
            }
        }
        if (max == 0) {
            return greatestNegative;
        }
        return max;
    }
}
