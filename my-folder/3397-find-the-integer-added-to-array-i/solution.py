class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1Total = 0
        nums2Total = 0
        for num in nums1:
            nums1Total += num
        for num in nums2:
            nums2Total += num
        return int((nums2Total - nums1Total) / len(nums1))
