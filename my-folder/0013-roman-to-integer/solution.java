import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> vals = new HashMap<>();
        vals.put('I', 1);
        vals.put('V', 5);
        vals.put('X', 10);
        vals.put('L', 50);
        vals.put('C', 100);
        vals.put('D', 500);
        vals.put('M', 1000);
        char[] charArr = s.toCharArray();
        int ans = 0;
        int prev = 0;
        for (char c : charArr) {
            int val = vals.get(c);
            System.out.println(val);
            if (val > prev) {
                ans -= 2 * prev;
            }
            ans += val;
            prev = val;
        }
        return ans;
    }
}
