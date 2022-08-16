class Solution {
    public boolean isPalindrome(String s) {
        char[] charArr = s.toCharArray();
        int leftPointer = 0;
        int rightPointer = charArr.length - 1;
        while (rightPointer > leftPointer) {
            if (!Character.isLetterOrDigit(charArr[leftPointer])) {
                leftPointer++;
                continue;
            } else if (!Character.isLetterOrDigit(charArr[rightPointer])) {
                rightPointer--;
                continue;
            } else if (Character.toLowerCase(charArr[leftPointer]) != Character.toLowerCase(charArr[rightPointer])) {
                return false;
            } else {
                leftPointer++;
                rightPointer--;
            }
        }
        return true;
    }
}
        
