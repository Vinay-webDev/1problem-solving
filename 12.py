"""845. Longest Mountain in Array"""

# class Solution:
#     def longestMountain(self, arr):
#         length = 0
#         l, r = 0, len(arr) - 1
#         while l <= r:
#             if arr[l] < arr[l + 1]:
#                 l += 1
#                 length = 0
#                 continue
#             if arr[r - 1] < arr[r]:
#                 r -= 1
#                 length = 0
#                 continue
#             l += 1
#             r -= 1
#             length += 1
#         return length

            
""""""""""""""""""""""""""""""""""""""""""
arr1 = [2,1,4,7,3,2,5]
arr2 = [2,2,2]
arr3 = [1,3,1]
class Solution:
    def longestMountain(self, arr):
        length = 0
        n = len(arr)
        if n < 3:
            return 0
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = i - 1
                r = i + 1
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1
                #formula to calulate length of subarray => r - l + 1
                length = max(length, r - l + 1)
        return length
sol = Solution()
print(sol.longestMountain(arr1))    #5
print(sol.longestMountain(arr2))    #0
print(sol.longestMountain(arr3))    #3


