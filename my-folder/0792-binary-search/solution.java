class Solution {
    public int search(int[] nums, int target) {
        return search2(nums, 0, nums.length - 1, target);
    }
    
    public int search2(int[] nums, int start, int end, int target) {
        if (start >= end) {
            if (nums[start] == target) {
                return start;
            } else {
                return -1;
            }
        }
        int mid = start + (end - start) / 2;
        if (nums[mid] > target) {
            return search2(nums, start, mid - 1, target);
        } else if (nums[mid] < target) {
            return search2(nums, mid + 1, end, target);
        } else {
            return mid;
        }
    }
}

