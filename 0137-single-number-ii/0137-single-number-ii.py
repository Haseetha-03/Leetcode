class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        
        for x in nums:
            twos |= ones & x
            ones ^= x
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        
        return ones
