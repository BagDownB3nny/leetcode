import java.util.HashSet;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<Integer> tracker = new HashSet<Integer>();
        Set<List<Integer>> set = new HashSet<List<Integer>>();
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            if (tracker.contains(nums[i])) {
                continue;
            } else {
                tracker.add(nums[i]);
            }
            int target = - nums[i];
            HashSet<Integer> hashset = new HashSet<>();
            for (int j = i + 1; j < nums.length; j++) {
                if (hashset.contains(target - nums[j])) {
                    ArrayList<Integer> newList = new ArrayList<Integer>(
                        Arrays.asList(nums[i], nums[j], target - nums[j]));
                    Collections.sort(newList);
                    set.add(newList);
                } else {
                    hashset.add(nums[j]);
                }
            }
        }
        Iterator<List<Integer>> itr = set.iterator();
        while (itr.hasNext()) {
            list.add(itr.next());
        }
        return list;
    }
}
