class Solution:
    
    def isHappy(self, n: int) -> bool:
        res = []
        while True:
            n = self.sumDigits(n)
            if n == 1:
                return True
            elif n not in res:
                res.append(n)
            else:
                return False






    def sumDigits(self, n):
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n = n // 10
        return sum

