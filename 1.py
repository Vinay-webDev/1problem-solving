"""217. Contains Duplicates"""
# nums1 = [1, 2, 2, 3, 4]
# nums2 = [100, 100, 294, 393, 9399030, 838]
# nums3 = [10, 20, 39, 93]
class Solution:
    def containsDuplicates(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
sol = Solution()
# print(sol.containsDuplicates(nums1))  #True
# print(sol.containsDuplicates(nums2))  #True
# print(sol.containsDuplicates(nums3))  #False


class Solution:
    def containsDuplicates(self, nums):
        if (len(set(nums)) == len(nums)):
            return False
        else:
            return True
sol = Solution()
# print(sol.containsDuplicates(nums1))  #True
# print(sol.containsDuplicates(nums2))  #True
# print(sol.containsDuplicates(nums3))  #False

class Solution:
    def containsDuplicates(self, nums):
        Map = {}
        for num in nums:
            if num in Map:
                return True
            else:
                Map[num] = 1
        return False
sol = Solution()
# print(sol.containsDuplicates(nums1))  #True
# print(sol.containsDuplicates(nums2))  #True
# print(sol.containsDuplicates(nums3))  #False




