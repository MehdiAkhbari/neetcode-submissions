
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # mylist = [x]
        y = x
        power = 1
        # r = []
        ans = 1
        m = n
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        while power <= n:
            r = m % 2
            m = m // 2
            print(y)
            if r != 0:
                ans *= y * r
            y = (y * y)
            
            power *= 2
            

        return ans


