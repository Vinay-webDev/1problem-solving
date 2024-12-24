"""268.Missing Number"""
nums1 = [3, 0, 1]
nums2 = [2, 4, 5, 6, 8, 7, 9, 0, 1]
nums3 = [0, 1]
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for index, value in enumerate(nums):
            if index != value:
                return index
            if value == len(nums) - 1:
                return value + 1
sol = Solution()
# print(sol.missingNumber(nums1))     #2
# print(sol.missingNumber(nums2))     #3
# print(sol.missingNumber(nums3))     #2



