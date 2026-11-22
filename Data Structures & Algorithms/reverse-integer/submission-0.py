class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        if x < 0:
            return -self.reverse(-x)
        while x != 0:
            r = x % 10
            x = x // 10
            y = y * 10 + r
        if y > pow(2, 31):
            return 0
        return y
