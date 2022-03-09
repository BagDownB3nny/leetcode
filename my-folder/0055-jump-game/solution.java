import java.util.Hashtable;

class Solution {
    public boolean canJump(int[] nums) {
        class Jumper {
            boolean canJumpy(int[] nums, int pointer) {
                if (pointer == 0) {
                    return true;
                }
                for (int i = 0; i < pointer; i++) {
                    if (nums[i] >= pointer - i) {
                        return canJumpy(nums, i);
                    }
                }
                return false;
            }
        }
        Jumper j = new Jumper();
        return j.canJumpy(nums,nums.length - 1);
    }
}
