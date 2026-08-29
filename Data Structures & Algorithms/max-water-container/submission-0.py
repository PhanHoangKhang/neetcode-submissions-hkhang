class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        water = 0
        hmin = 0

        while left < right:
            hmin = min(heights[left], heights[right])
            water = max((right - left) * hmin, water)

            if heights[left] <= heights[right]:
                left+=1

            else:
                right-=1

        return water