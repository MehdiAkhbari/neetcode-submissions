# This is similar to the previous question (at each point you either rob it and get f(n-2) + num(s) or not rob it and gain f(n-1))
# The only difference is that first and last house can't be robbed together. 
# To solve this, consider two cases:
# 1. you choose robbed houses from 0 to len(nums) - 1
# 2. you choose robbed houses from 1 to len(nums)
# the final answer is the maximum of the two

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        out1 = [0, nums[0]]
        out2 = [0, nums[1]]
        for i in range(1, len(nums)-1):
            out1.append(max(out1[-1], out1[-2] + nums[i]))
        for i in range(2, len(nums)):
            out2.append(max(out2[-1], out2[-2] + nums[i]))
        # print(out1, out2)    
        return max(out1[-1], out2[-1])
