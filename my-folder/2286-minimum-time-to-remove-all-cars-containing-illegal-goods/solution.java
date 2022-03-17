class Solution {
    public int minSubarray(String s) {
        int[] arr = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            int n = Integer.valueOf(s.substring(i, i + 1));
            if (n == 1) {
                arr[i] = 1;
            } else {
                arr[i] = -1;
            }
        }
        int min = 0;
        int section = 0;
        for (int i = 0; i < arr.length; i++) {
            section += arr[i];
            if (section >= 0) {
                section = 0;
                continue;
            }
            if (section < min) {
                min = section;
            }
        }
        return min;
    }
    
    public int minimumTime(String s) {
        if (!s.contains("1")) {
            return 0;
        }
        return s.length() + minSubarray(s);
    }
}


// left + right + 2 * middle(1)
// left + right + middle + 2 * middle(1) - middle
// n + middle(1) - middle(0)
// find min of middle(1) - middle(0)
// max subarray of s
// start and end points will be the points where middle is located
// remove left till start, remove right till end, remove middle
