import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        char[] charArr = s.toCharArray();
        Character[] brackets = new Character[] {
            '(', ')',
            '[', ']',
            '{', '}'
        };
        for (int i = 0; i < charArr.length; i++) {
            for (int j = 0; j < brackets.length; j++) {
                if (charArr[i] == brackets[j]) {
                    // Check to see if bracket is opening
                    if (j % 2 == 0) {
                        // Bracket is opening
                        stack.push(charArr[i]);
                    } else {
                        // Bracket is closing
                        if (stack.isEmpty()) {
                            return false;
                        }
                        if (stack.pop() != brackets[j - 1]) {
                            return false;
                        }
                    }
                    break;
                }
            }
        }
        return stack.isEmpty();
    }
}
