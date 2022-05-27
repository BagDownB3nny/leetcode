using System;
using System.Collections.Generic;

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numsDict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (numsDict.ContainsKey(target - nums[i])) {
                return new int[2] {i, numsDict[target - nums[i]]};
            } else {
                if (!numsDict.ContainsKey(nums[i])) {
                    numsDict.Add(nums[i], i);
                }
            }
        }
        return null;
    }
}
