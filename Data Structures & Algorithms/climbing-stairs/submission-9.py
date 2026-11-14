class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n <= 2:
            return n
        for i in range(1, n - 1):
            temp = first + second
            first = second
            second = temp

        return second

