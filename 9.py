"""977. Squares of a Sorted Array"""

class Solution:
    def sortedSquares(self, nums):
        temp = []
        for num in nums:
            temp.append(num * num)
        return sorted((temp))
sol = Solution()
# print(sol.sortedSquares(nums1)) #[0, 1, 9, 16, 100]
# print(sol.sortedSquares(nums2)) #[4, 9, 9, 49, 121]
"""above is a nub solution"""
#split and merge

class Solution:
    def sortedSquares(self, nums):
        #edge cases
        if not nums:
            return nums
        if nums[0] > 0:
            return [num ** 2 for num in nums]
        #split and merge
        s = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                s = i
                break
        a, b = nums[:s:1][::-1], nums[s:] 
        a = [n * -1 for n in a]
        res = []
        l, r = 0, 0
        while l < len(b) and r < len(a):
            if abs(b[l]) < abs(a[r]):
                res.append(b[l])
                l = l + 1
            else:
                res.append(a[r])
                r = r + 1
        while l < len(a):
            res.append(a[l])
            l = l + 1
        while r < len(b):
            res.append(b[r])
            r = r + 1
        return [n ** 2 for n in res]
sol = Solution()
# print(sol.sortedSquares(nums1)) #[0, 1, 9, 16, 100]
# print(sol.sortedSquares(nums2)) #[4, 9, 9, 49, 121]
# print(sol.sortedSquares(nums3)) #[]
# print(sol.sortedSquares(nums4)) #[1, 4, 9, 16]
# print(sol.sortedSquares(nums5)) #[25, 9, 4, 1]  wrong answer
#❌❌❌Wrong Answer❌❌❌

nums1, nums2 = [-4,-1,0,3,10], [-7,-3,2,3,11] 
nums3, nums4 = [], [1, 2, 3, 4]
nums5 = [-5,-3,-2,-1]
class Solution:
    def sortedSquares(self, nums):
        if not nums:
            return nums
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            l_square = nums[l] ** 2
            r_square = nums[r] ** 2
            if l_square > r_square:
                res.append(l_square)
                l += 1
            else:
                res.append(r_square)
                r -= 1
        return res[::-1]
sol = Solution()
print(sol.sortedSquares(nums1)) #[0, 1, 9, 16, 100]
print(sol.sortedSquares(nums2)) #[4, 9, 9, 49, 121]
print(sol.sortedSquares(nums3)) #[]
print(sol.sortedSquares(nums4)) #[1, 4, 9, 16]
print(sol.sortedSquares(nums5)) #[1, 4, 9, 25]

