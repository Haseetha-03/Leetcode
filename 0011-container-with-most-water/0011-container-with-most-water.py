from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            # compute area formed by lines at l and r
            h = min(height[l], height[r])
            width = r - l
            area = h * width

            # update maximum
            if area > max_area:
                max_area = area

            # move the pointer pointing to the shorter line
            # because moving the taller one cannot produce a larger area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
