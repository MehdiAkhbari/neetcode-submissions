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
