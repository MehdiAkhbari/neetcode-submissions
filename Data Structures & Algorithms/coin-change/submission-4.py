# the idea is simple: # coins to construct x: f(x) = min(1 + f(x-d)) where d in coins


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mylist = [-1] * (amount + 1)
        mylist[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i >= j:
                    if mylist[i - j] != -1:
                        temp = 1 + mylist[i - j]
                        if temp < mylist[i] or mylist[i] == -1:
                            mylist[i] = temp


        return mylist[-1]


