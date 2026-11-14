class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0











    # O(n^2) solution:    
        # ans = [0] * len(nums)
        # ans[0] = 1
        # for i in range(1, len(nums)):
            
        #     for j in range(i):
        #         ans[i] += ans[j] * (nums[j] >= i - j)

        # return ans[-1] >= 1