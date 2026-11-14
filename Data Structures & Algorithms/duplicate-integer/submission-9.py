class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        print(x)
        ans = len(x) != len(nums)
        return ans
        