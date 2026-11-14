# idea: similar to largest product I did before. At each position i, maximum sum comes from either:
# adding current number to the max so far OR starting a new subarray from positin i.
# when you sweep all i, the maximum is found

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sofar = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            max_sofar = max(nums[i], max_sofar + nums[i])
            if max_sofar > maximum:
                maximum = max_sofar

        return maximum