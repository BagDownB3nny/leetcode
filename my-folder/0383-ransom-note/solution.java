import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine)     {
        HashMap<Character, Integer> magLetters = new HashMap<>();
        char[] magCharArr = magazine.toCharArray();
        for (Character c : magCharArr) {
            if (magLetters.containsKey(c)) {
                magLetters.replace(c, magLetters.get(c) + 1);
            } else {
                magLetters.put(c, 1);
            }
        }
        char[] charArr = ransomNote.toCharArray();
        for (Character c : charArr) {
            if (magLetters.containsKey(c)) {
                int uses = magLetters.get(c) - 1;
                if (uses == 0) {
                    magLetters.remove(c);
                } else {
                    magLetters.replace(c, magLetters.get(c) - 1);
                }
            } else {
                return false;
            }
        }
        return true;
    }
}
