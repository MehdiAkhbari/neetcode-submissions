class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if len(cost) <= 1:
            totalcost = 0
        first = 0
        second = 0
        # else:
        #     return min(self.minCostClimbingStairs(cost[:n-1]) + cost[n-1], self.minCostClimbingStairs(cost[:n-2]) + cost[n-2])


        for i in range(1, n):
            cost1 = first + cost[i]
            cost2 = second + cost[i-1]
            totalcost = min(cost1, cost2)
            # update first and second
            second = first
            first = totalcost
            # print(totalcost)
        return totalcost


