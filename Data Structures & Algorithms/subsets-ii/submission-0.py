class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()


        res = []

        def fun(cur, i):
            print(cur, i)
            if i >= len(nums):
                res.append(cur.copy())
                print(f"res = {res}")
                return
            

            cur.append(nums[i])
            fun(cur, i + 1)
        
            cur.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            fun(cur, i + 1)
            

        fun([], 0)
        return res
            