"""15. 3Sum"""

# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         def binarySearch_for_x(b1, b2, target):
#             l, r = 0, len(nums) - 1
#             while l < r:
#                 if l == b1 or l == b2:
#                     l += 1
#                 if r == b1 or r == b2:
#                     r -= 1
#                 mid = (l + r) // 2
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] < target:
#                     l += 1
#                 else:
#                     r -= 1
#             return None
#         l, r = 0, len(nums) - 1
#         while l < r:
#             y = nums[l]
#             z = nums[r]
#             x = -1 * y - z
            
#             if binarySearch_for_x(l, r, x) != None:
###################################################################
nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r  = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
sol = Solution()
print(sol.threeSum(nums1))  #[[-1, -1, 2], [-1, 0, 1]]
print(sol.threeSum(nums2))  #[]
print(sol.threeSum(nums3))  #[[0, 0, 0]]




