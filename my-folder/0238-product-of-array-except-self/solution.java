class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int product = 1;
        int noOfZeros = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] != 0) {
                product = product * nums[i];
            } else {
                noOfZeros++;
            }
        }
        int[] arr = new int[len];
        for (int i = 0; i < len; i++) {
            if (nums[i] != 0) {
                if (noOfZeros == 0) {
                    arr[i] = product / nums[i];
                } else {
                    arr[i] = 0;
                }
            } else {
                if (noOfZeros == 1) {
                    arr[i] = product;
                } else {
                    arr[i] = 0;
                }
            }
        }
        return arr;
    }
}
