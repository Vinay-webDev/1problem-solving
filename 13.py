"""SLIDING WINDOW"""
"""FIXED WINDOW LENGTH"""
"""Maximum Average Subarray I"""
nums1, k1 = [1,12,-5,-6,50,3], 4
nums2, k2 = [5], 1
nums3, k3 = [1,2,3,1,2,3], 3
class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        max_avg = curr_sum / k
        for i in range(k, n):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            avg = curr_sum / k
            max_avg = max(max_avg, avg)
        return max_avg
sol = Solution()
print(sol.findMaxAverage(nums1, k1))    #12.75
print(sol.findMaxAverage(nums2, k2))    #5.0
print(sol.findMaxAverage(nums3, k3))    #2.0








