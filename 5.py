"""1365. How many Nubmers are smaller than the current number"""

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
# print(sol.smallerNumbersThanCurrent(nums1)) #[4, 0, 1, 1, 3]
# print(sol.smallerNumbersThanCurrent(nums2)) #[2, 1, 0, 3]

nums1 = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [4, 4, 8, 10, 11, 23, 8, 0, 1, 3, 101, 99]
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        temp_nums = sorted((nums))
        nums_map = {}
        for i, num in enumerate(temp_nums):
            if num not in nums_map:
                nums_map[num] = i
        res = []
        for num in nums:
            res.append(nums_map[num])
        return res
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums1)) 
#[4, 0, 1, 1, 3]
print(sol.smallerNumbersThanCurrent(nums2)) 
#[2, 1, 0, 3]
print(sol.smallerNumbersThanCurrent(nums3)) 
#[3, 3, 5, 7, 8, 9, 5, 0, 1, 2, 11, 10]




