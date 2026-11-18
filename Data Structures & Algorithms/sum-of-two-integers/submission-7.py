class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        j = 1
        ans = 0
        for i in range(32):
            s = ((1 & (a >> i)) ^ (1 & (b >> i)) ^ c) 
            c = ((1 & (a >> i)) & (1 & (b >> i))) | ((1 & (a >> i)) & c) | ((1 & (b >> i)) & c)
            print(s, c)
            ans = ans ^ (s << i)
            if ans >= (1 << 31):
                return   ~(ans ^ (0xFFFFFFFF))
        return ans
            
