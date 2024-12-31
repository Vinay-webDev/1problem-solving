"""Contains Duplicate II"""
nums1, k1 = [1,2,3,1], 3
nums2, k2 = [1,0,1,1], 1
nums3, k3 = [1,2,3,1,2,3], 2
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
sol = Solution()
print(sol.containsNearbyDuplicate(nums1, k1))   #True
print(sol.containsNearbyDuplicate(nums2, k2))   #True
print(sol.containsNearbyDuplicate(nums3, k3))   #False



