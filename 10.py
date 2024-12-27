"""Two Sum II"""
numbers1, target1 = [2,7,11,15], 9
numbers2, target2 = [2,3,4], 6
numbers3, target3 = [-1,0], -1
class Solution:
    def twoSumII(self, numbers, target):
        l, r = 0, len(numbers) - 1
        i1, i2 = 0, 0
        while l < r:
            x = numbers[l] + numbers[r]
            if x == target:
                i1 = l + 1
                i2 = r + 1
                return [i1, i2]
            elif x < target:
                l += 1
            else:
                r -= 1
sol = Solution()
print(sol.twoSumII(numbers1, target1))  #[1, 2]
print(sol.twoSumII(numbers2, target2))  #[1, 3]
print(sol.twoSumII(numbers3, target3))  #[1, 2]
