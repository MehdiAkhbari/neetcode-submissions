class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = []
        for x in nums:
            seen.append(x)

        for i in range(len(nums) + 1):
            if i not in seen:
                return i
