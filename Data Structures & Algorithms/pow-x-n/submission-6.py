# Solution 3 is most optimied, but the idea is the same as this and this is easier to understand.
# Steps (for n > 0):
# 1. Create a list of x^1, x^2, x^4, ... up to x^(2^k) such that x^(2^k) <= n 
# 2. Write x^n as a multiplication of the elements of the list above, to do that you need to find the binary reperesentation of n, ex: 10 = (1010) binary. Then x^10 = (x^1)^0 * (x^2)^1 * (x^4)^0 * (x^8)^1
# Then calculate the multiplicand by: ans = prod(xlist[i] * r[i]) if r[i] == 1
# if n == 0: return 0
# if n < 0: return 1/x^(-n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        mylist = [x]
        power = 1
        r = []
        ans = 1
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        while power <= n // 2:
            mylist.append(mylist[-1] * mylist[-1])
            power *= 2

        while n != 0:
            r.append(n % 2)
            n = n // 2

        print(r)
        print(mylist)
        for i in range(len(r)):
            if r[i] == 1:
                ans *= r[i] * mylist[i]
        return ans


