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
            h = height[l] if height[l] < height[r] else height[r]
            current_max_area = h * w
            max_area = max(max_area, current_max_area)
            if height[l] == height[r]:
                l = l + 1
                r = r - 1
            elif height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return max_area

