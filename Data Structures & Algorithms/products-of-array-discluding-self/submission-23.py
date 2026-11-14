class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        out = []
        l = len(nums)
        for i in range(1, l):
            pre.append(pre[i-1] * nums[i-1])
            post.append(post[i-1] * nums[l-i])
            
        # print(pre)
        post = post[: : -1]
        
        # print(post)
        for i in range(l):
            out.append(pre[i] * post[i])
        # print(out)
        return out
