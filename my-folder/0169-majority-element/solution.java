import java.util.HashMap;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> nums2 = new HashMap<>();
        if (nums.length == 1) {
            return nums[0];
        }
        for (int num : nums) {
            if (nums2.containsKey(num)) {
                nums2.replace(num, nums2.get(num) + 1);
                if (nums2.get(num) > nums.length / 2) {
                    return num;
                }
            } else {
                nums2.put(num, 1);
            }
        }
        return 0;
    }
}
