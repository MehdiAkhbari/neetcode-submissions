# Idea: First, sort the numbers to make skipping repeated numbers easier.
# Then, write a backtracking function with cur (current subset so for) and i (first allowed element of the subset), start with fun([], 0) obviously.
# For each element  no. i: either i is in the subset of not. if it is: append i to cur, then calculate fun(cur, i+1), if it's not: pop i from cur, then calculate fun(cur, i + 1) 
# Note: to avoid repeats: repeats happen only when element i is not in cur, but element i + 1 is equal to i. To aviod this, when i is not in cur, if nums[i] == nums[i + 1] (and i + 1 < len(nums)), let i = i + 1 (skip i+1), do tis while i= i + 1 to reach a new number.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()


        res = []

        def fun(cur, i):
            print(cur, i)
            if i >= len(nums):
                res.append(cur.copy())
                # print(f"res = {res}")
                return
            

            cur.append(nums[i])
            fun(cur, i + 1)
        
            cur.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            fun(cur, i + 1)
            

        fun([], 0)
        return res
            