class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for k in range(len(nums)):
            target = (-1) * nums[k]
            l = 0
            r = len(nums) - 1

            while(l <= r):
                if nums[l] + nums[r] == target:
                    mylist = [nums[l], nums[r], nums[k]]
                    mylist.sort()
                    if mylist not in ans and l != r and l != k and r != k:
                        ans.append(mylist)
                    l += 1
                    r -= 1
                
                elif nums[l] + nums[r] < target:
                    l += 1

                elif nums[l] + nums[r] > target:
                    r -= 1

            


        return ans