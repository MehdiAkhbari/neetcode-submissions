class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        for i in range(2 ** l):
            ans.append([])
            
            for j in range(l):
                if (i & (1 << j)):
                    ans[i].append(nums[j])

        return ans
