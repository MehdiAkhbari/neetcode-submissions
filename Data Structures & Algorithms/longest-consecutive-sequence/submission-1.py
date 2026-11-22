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


            

