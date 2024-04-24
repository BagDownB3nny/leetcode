class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        numbers = [0, 1, 1]
        ptr = 0
        for _ in range(n - 2):
            numbers[ptr] = numbers[0] + numbers[1] + numbers[2]
            ptr = (ptr + 1) % 3
        return max(numbers)
