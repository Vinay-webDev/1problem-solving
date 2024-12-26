"""977. Squares of a Sorted Array"""
nums1 = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]
class Solution:
    def sortedSquares(self, nums):
        temp = []
        for num in nums:
            temp.append(num * num)
        return sorted((temp))
sol = Solution()
print(sol.sortedSquares(nums1)) #[0, 1, 9, 16, 100]
print(sol.sortedSquares(nums2)) #[4, 9, 9, 49, 121]


