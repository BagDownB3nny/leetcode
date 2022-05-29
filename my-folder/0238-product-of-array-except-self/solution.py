class Solution(object):
    def productExceptSelf(self, nums):
        contains_zero = False
        contains_multiple_zeroes = False
        total_product = 1
        for num in nums:
            if num == 0:
                if contains_zero:
                    contains_multiple_zeroes = True
                else:
                    contains_zero = True
            else:
                total_product *= num
        new_arr = []
        if contains_multiple_zeroes:
            return map(lambda x: 0, nums)
        for num in nums:
            if num == 0:
                new_arr.append(total_product)
            else:
                if contains_zero:
                    new_arr.append(0)
                else:
                    new_arr.append(total_product / num)
        return new_arr
            
        
