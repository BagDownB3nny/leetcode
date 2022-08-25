class Solution {
    public int charToInt(char c) {
        if (c == '1') {
            return 1;
        }
        if (c == '0') {
            return 0;
        }
        return -1;
    }
    
    public String addBinary(String a, String b) {
        StringBuilder ans = new StringBuilder();
        char[] aChars = a.toCharArray();
        char[] bChars = b.toCharArray();
        
        int aPtr = aChars.length - 1;
        int bPtr = bChars.length - 1;
        
        
        int carryOver = 0;
        while (aPtr >= 0 || bPtr >= 0) {
            int aValue = (aPtr >= 0)
                ? charToInt(aChars[aPtr])
                : 0;
            int bValue = (bPtr >= 0)
                ? charToInt(bChars[bPtr])
                : 0;
            int sum = aValue + bValue + carryOver; 
            carryOver = sum / 2;
            ans.insert(0, sum % 2);
            aPtr--;
            bPtr--;
        }
        System.out.println("Carryover: " + carryOver);
        if (carryOver == 1) {
            ans.insert(0, 1);
        }
        return ans.toString();
    }
}
