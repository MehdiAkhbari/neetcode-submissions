# You need to know the XOR (^) generates 0 if applied to same number and return the only unique number when all elements are XORed.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans = ans ^ x

        return ans
            