class Solution:
    def minEnd(self, n: int, x: int) -> int:
        binaryX = bin(x)
        zeroes = []
        highest = 0
        power = 1
        for i in reversed(range(2, len(binaryX))):
            digit = binaryX[i]
            if digit == "0":
                zeroes.append(power)
            power = power * 2
                
        print(zeroes)
        current = n -1
        binaryCurrent = bin(current)[2:]
        newAns = x
        while len(binaryCurrent) > len(zeroes):
            zeroes.append(power)
            power = power * 2
        for i in reversed(range(len(binaryCurrent))):
            index = -i - 1
            digit = binaryCurrent[index]
            if digit == "1":
                newAns += zeroes[i]
        return newAns
