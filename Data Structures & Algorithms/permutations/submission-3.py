class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # cur = []
        def fun(cur):
            # print(cur)
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            else:
                for x in nums:
                    cur_set = set(cur)
                    if x not in cur_set:    
                        # print(f"x= {x}")                   
                        fun(cur + [x])

        fun([])

        return res
        
                 
            
        