#  This solution seems strange at the beginning. The idea is instead of solving it forward, think backward. Initially your goal is to reach l-1. Then, find the closest (highest) index from which you can reach l-1, say l-m. Then, l-m will be your next goal. If moving backward, your goal will ever be 0, you can reverse this to get to l-1.


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