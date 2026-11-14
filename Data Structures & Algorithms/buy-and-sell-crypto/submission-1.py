class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        r = 1
        while r < len(prices):
            temp = prices[r] - prices[l]
            if temp > ans:
                ans = temp
            
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1

        return ans