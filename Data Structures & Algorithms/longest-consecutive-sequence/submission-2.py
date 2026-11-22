# Idea: 1. create a set (hash set) from the list because searching in a set is O(1) instead of O(n)
        # 2. Find each element n for which n-1 is not is the set, and only check existence of n + c, c= 1, 2, ... for those


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        ans = 0
        for n in nums:
            if n - 1 not in nums: 
                c = 1
                while True:
                    if n + c in nums:
                        c += 1
                    else:
                        break
                
                ans =max(ans, c)

        return ans


            

