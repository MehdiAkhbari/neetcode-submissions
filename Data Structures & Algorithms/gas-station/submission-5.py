# My pwn solution was not fast enough
# points to solve the problem: 
    # 1. if sum(cost) > sum(gas) its impossible to finish. Check it first to save time
    # 2. if net gas < 0 from 0 to j, and its positive from 0 to some k (k<j), it has to be negative from k to j as well for all 0 < k < j, so I can update new beginning index to j+1 (rather than 1). This saves a lot of time and leads to O(n) timing. 


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        net = 0
        idx = 0
        for i in range(len(gas)):
            net += (gas[i] - cost[i])

            if net < 0:
                net = 0
                idx = i + 1

        return idx
            

