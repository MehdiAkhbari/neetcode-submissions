# 1. find i'th digit of n by bit = (n >> i) & 1
# 2. shift it left for 31 - i positions
# 3. add that to the result var
class Solution:
    def reverseBits(self, n: int) -> int:
        res=  0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << 31- i)
        return res
            