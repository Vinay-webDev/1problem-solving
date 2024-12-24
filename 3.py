"""448. Find All Numbers Disappeared in an Array"""
#1 to n range [1 - n]
nums1 = [4,3,2,7,8,2,3,1]
nums2 = [1,1]
class Solution:
    def findAllNumbers(self, nums):
        nums_set = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                res.append(i)
        return res
sol = Solution()
print(sol.findAllNumbers(nums1))    #[5, 6]
print(sol.findAllNumbers(nums2))    #[2]




