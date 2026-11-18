# just AND number with 2^n for n= 0 : 31
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        num = 1
        for i in range(32): 
            if (num & n):
                res += 1
            num *= 2
        return res