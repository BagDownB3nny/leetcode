import math

class Solution:
    def myAtoi(self, s: str) -> int:
        print(s)
        isPositive = True
        ptr = 0
        whitespaceStage = True
        signStage = False
        numStage = False
        digits = []
        ans = 0
        smallest = int(math.pow(2, 31) * -1)
        biggest = int(math.pow(2, 31) - 1)
        while ptr < len(s):
            if whitespaceStage:
                if s[ptr] == " ":
                    ptr += 1
                    continue
                else:
                    signStage = True
                    whitespaceStage = False
            if signStage:
                if s[ptr] == "-":
                    isPositive = False
                    ptr += 1
                    signStage = False
                    numStage = True
                    continue
                elif s[ptr] == "+":
                    ptr += 1
                    signStage = False
                    numStage = True
                    continue
                else:
                    signStage = False
                    numStage = True
                    continue
            if numStage:
                if s[ptr].isnumeric():
                    digits.append(s[ptr])
                else:
                    break
            ptr += 1
        for i, digit in enumerate(digits):
            power = len(digits) - i - 1
            ans += math.pow(10, power) * int(digit)
        if not isPositive:
            ans = int(ans) * -1
            ans = max(smallest, ans)
        return min(int(ans), biggest)
