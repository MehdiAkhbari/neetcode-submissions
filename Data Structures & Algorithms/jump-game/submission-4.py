class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            
            for j in range(i):
                ans[i] += ans[j] * (nums[j] >= i - j)

        return ans[-1] >= 1