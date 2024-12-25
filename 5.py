"""1365. How many Nubmers are smaller than the current number"""
nums1 = [8,1,2,2,3]
nums2 = [6,5,4,8]
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        return res
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums1)) #[4, 0, 1, 1, 3]
print(sol.smallerNumbersThanCurrent(nums2)) #[2, 1, 0, 3]





