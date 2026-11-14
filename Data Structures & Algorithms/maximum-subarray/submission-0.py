class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sofar = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            max_sofar = max(nums[i], max_sofar + nums[i])
            if max_sofar > maximum:
                maximum = max_sofar

        return maximum