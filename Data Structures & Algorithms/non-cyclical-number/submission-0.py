class Solution:
    def isHappy(self, n: int) -> bool:
        for _ in range(10):
            n = self.sumDigits(n)
            if n == 1:
                return True

        return False






    def sumDigits(self, n):
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n = n // 10
        return sum

