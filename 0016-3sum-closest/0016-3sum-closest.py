from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                pass

            l, r = i + 1, n - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if abs(curr - target) < abs(best_sum - target):
                    best_sum = curr
                if curr == target:
                    return curr
                elif curr < target:
                    l += 1
                else:
                    r -= 1

        return best_sum
