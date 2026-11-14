# Idea: greedy algorithm: start with i, j = 0 and calculate what are the minimum and maximum indices you can reach from them nums[i : j]. The update j = maximum index, i = minimum index, and repeat until you reach j >= len(nums) - 1. Count the number of times needed to reach and return it.

class Solution:
    def jump(self, nums: List[int]) -> int:
        i, j = 0, 0
        c = 0
        while j < len(nums) - 1:
            max_idx , min_idx = 0, len(nums)

            for k in range(i , j + 1):
                max_idx = max(max_idx, k + nums[k])
                min_idx = min(min_idx, k + int(nums[k] > 0))  
            i, j = min_idx, max_idx

            # print(i, j)
            c += 1
        return c



