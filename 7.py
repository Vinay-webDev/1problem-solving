"""11.Container with most water"""
height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            current_max_area = h * w
            max_area = max(max_area, current_max_area)
            if height[l] < height[r]: 
                l = l + 1
            else:
                r = r - 1
        return max_area
sol = Solution()
print(sol.maxArea(height1)) #49
print(sol.maxArea(height2)) #1

