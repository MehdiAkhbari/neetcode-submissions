# I couldn't solve this with a nice code.
# This is the algorithm: we are looking for the smallest number for which hours(piles, k) <= h. So, if for some (small) number hours(piles, k) > h, we can drop 1,..,k from our search space. but if for some k, hours(piles, k) <= h, we can't drop it, we can only say tha k is an upper bound for the answer. So, the algorithm is:
# start with l = 1, r = max(piles) (the maximum usable speed)
# mid = (r + l) // 2
    #if hours(piles, mid) > h -> all numbers from 1, ..., mid are dropped -> l = mid + 1 
    # if hours(piles, mid) <= h -> mid is an upper bound, so let r = mid
    # repeat until l and r are equal, then return eother of them 

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