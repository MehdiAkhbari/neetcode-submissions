class Solution:
    def rob(self, nums: List[int]) -> int:
        p_2 = 0
        p_1 = 0 
        for i in range(len(nums)):
            p = max(p_2 + + nums[i], p_1)
            p_2 = p_1
            p_1 = p

        return p

        
            