class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l < 2:
            return 0
        else:
            return min(Solution.minCostClimbingStairs(self, cost[0 : l - 1]) + cost[l - 1], Solution.minCostClimbingStairs(self, cost[0 : l - 2]) + cost[l - 2])