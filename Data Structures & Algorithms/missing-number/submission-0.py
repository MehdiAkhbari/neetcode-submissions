class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        matrix_sum = 0
        for i in nums:
            matrix_sum += i
        
        total_sum = int(len(nums) * (len(nums) + 1) / 2)
        return total_sum - matrix_sum
