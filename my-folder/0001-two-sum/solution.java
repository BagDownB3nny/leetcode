import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> storage = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (storage.containsKey(difference)) {
                return new int[] {storage.get(difference), i};
            } else {
                storage.put(nums[i], i);
            }
        }
        return null;
    }
}
