import java.util.HashMap;

class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> letters = new HashMap<>();
        char[] charArr = s.toCharArray();
        for (Character c : charArr) {
            if (letters.containsKey(c)) {
                letters.replace(c, letters.get(c) + 1);
            } else {
                letters.put(c, 1);
            }
        }
        System.out.println(letters);
        int ans = 0;
        int highestOdd = 0;
        for (Integer value : letters.values()) {
            if (value % 2 == 0) {
                ans += value;
            } else if (value > highestOdd) {
                if (highestOdd != 0) {
                    ans += highestOdd - 1;
                }
                highestOdd = value;
            } else {
                ans += value - 1;
            }
        }
        return ans + highestOdd;
    }
}
