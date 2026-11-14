class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if self.hours(piles, mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l

    def hours(self, piles, k):
        total_h = 0
        for p in piles:
            total_h += -(-p // k)
        return total_h