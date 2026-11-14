class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return Solution.climbStairs(self, n=n-1) + Solution.climbStairs(self, n=n-2)
