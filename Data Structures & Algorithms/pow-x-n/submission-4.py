
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


