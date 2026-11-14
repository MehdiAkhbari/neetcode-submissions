class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # x = set(nums)
        # print(x)
        # ans = len(x) != len(nums)
        my_set = set()
        for x in nums:
            if x in my_set:
                return True

            else: 
                my_set.add(x)

        return False
        