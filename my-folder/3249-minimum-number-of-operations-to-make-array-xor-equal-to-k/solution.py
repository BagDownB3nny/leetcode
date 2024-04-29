class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        binaryK = bin(k)[2:]
        ones = [0 for _ in binaryK]
        
        for num in nums:
            binary = bin(num)[2:]
            # iterate through the binary starting at smallest binary
            # index must start from last
            for i in range(len(binary)):
                index = -i - 1
                digit = binary[index]
                if digit == "1":
                    while i >= len(ones):
                        ones.append(0)
                    ones[i] += 1
        
        n = len(nums)
        ans = 0
        for i in range(len(ones)):
            index = -i - 1
            digit = ""
            if i >= len(binaryK):
                digit = "0"
            else:
                digit = binaryK[index]
            if digit == "1":
                if ones[i] % 2 == 0:
                    ans += 1
            elif digit == "0":
                if ones[i] % 2 == 1:
                    ans += 1
        
        return ans
            
