import java.util.Hashtable;

class Solution {
    ArrayList<Boolean> list = new ArrayList<>();
    Hashtable<String, Boolean> h = new Hashtable();
    public boolean wordBreak(String s, List<String> wordDict) {
        if (h.get(s) != null) {
            return h.get(s);
        }
        if (wordDict.contains(s)) {
            h.put(s, true);
            return true;
        }
        for (int i = 0; i <= s.length(); i++) {
            if (wordDict.contains(s.substring(0,i))) {
                list.add(wordBreak(s.substring(i,s.length()), wordDict));
            }
        }
        if (list.size() == 0) {
            h.put(s, false);
            return false;
        } else {
            for (Boolean i : list) {
                if (i) {
                    h.put(s, true);
                    return true;
                }
            }
            h.put(s, false);
            return false;
        }
    }
}
