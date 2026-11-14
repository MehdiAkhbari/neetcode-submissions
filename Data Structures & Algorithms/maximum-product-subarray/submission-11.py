# Idea: at each iteration number i, the maximum (and minimum) product is the maximum of 3 options:
# 1. starting a new subarray: nums[i]
# 2. nums[i] * max product so far
# 3. nums[t] * min product (negative) so far
# save the maximum and minimum of these three
# if max so far > ma, update max (similarly for min)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxi = nums[0]
        mini = nums[0]
        max_current = nums[0]
        min_current = nums[0]

        for i in range(1, len(nums)):


            v1 = max_current * nums[i]
            v2 = min_current * nums[i]
            max_current = max(nums[i], v1, v2) 
            min_current = min(nums[i], v1, v2)

            if max_current > maxi:
                maxi = max_current
            if min_current < mini:
                mini = min_current
            
        print(max_current, min_current)
        return maxi


            