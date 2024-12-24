"""1. Two Sum"""
# nums1, target1 = [2,7,11,15], 9
# nums2, target2 = [3,2,4], 6
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
sol = Solution()
# print(sol.twoSum(nums1, target1))   #[0, 1]
# print(sol.twoSum(nums2, target2))   #[1, 2]
#Noob solution Time complexity O(N^2)☝️

nums1, target1 = [2,7,11,15], 9
nums2, target2 = [3,2,4], 6
class Solution:
    def twoSum(self, nums, target):
        nums_map = {}
        # i = index, v = value
        for i, v in enumerate(nums):
            if target - v in nums_map:
                return [i, nums_map[target - v]]
            else:
                nums_map[v] = i
sol = Solution()
print(sol.twoSum(nums1, target1))   #[1, 0]
print(sol.twoSum(nums2, target2))   #[2, 1]


"""another optimal solution from leetcode"""
class Solution:
    def twoSum(self, nums, target):
        d0=defaultdict(list)
        for i in range(len(nums)):
            d0[nums[i]].append(i)
        while 1:
            kn = [*d0.keys()][-1]
            
            v = d0.pop(kn)
            if kn*2 == target and len(v) > 1:
                return v

            if target-kn in d0.keys() :
                return [v[0],d0[target-kn][0]]

