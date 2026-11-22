# Similar to the precious question, the only difference is tha using the same algorithm leads to repeated sets
# To avoid that: sort the list
# note that repetition only happens when element i is not used (when it's used and we still have it, we can use it again). So, when we are not using i, we skip the elements in the sorted list as long as the same values is repeated.
 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # cur = []
        candidates.sort()
        # print(candidates)
        def dfs(i, cur, tot):
        
            if tot == target:
                res.append(cur.copy())    
                return

            if i >= len(candidates) or tot > target:
                return

            
            cur.append(candidates[i])
            dfs(i + 1, cur, tot + candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, tot)

        dfs(0, [], 0)

        return res