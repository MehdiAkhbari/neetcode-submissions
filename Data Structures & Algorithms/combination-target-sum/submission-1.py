# Idea: backtracking with some twist: For each element: there's a decision tree
# 1. Include it in the answer
# 2. Don't use it in the answer
# Define function dfs(i, cur, total) where i is the first element allowed to use in the answer, cur is the current list, and total is the sum of the elements in the list
# If total > target or i >= len(nums): we've reached the end of the tree with no good answer, so return
# If total == target, we found a solution, so append "cur" it to "res" (set of results), and return IMPORTANT: Since cur is changing all the time use cur.copy() otherwise the results in not correct
# Otherwise, you have the two options below: include nums[i] or not
# If include: dfs(i, cur, total + nums[i])
# If not include: dfs(i+1, cur.pop(), total)
# initialize with dfs(0, [], 0)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, cur, total):
            if i >= len(nums) or total > target:
                return
            elif total == target:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])

            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, cur, 0)
        return res

