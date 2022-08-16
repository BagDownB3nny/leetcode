import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charArr1 = s.toCharArray();
        char[] charArr2 = t.toCharArray();
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : charArr1) {
            if (map.containsKey(c)) {
                map.replace(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for (char c : charArr2) {
            if (map.containsKey(c)) {
                map.replace(c, map.get(c) - 1);
                if (map.get(c) == 0) {
                    map.remove(c);
                }
            } else {
                return false;
            }
        }
        return map.isEmpty();
    }
}
