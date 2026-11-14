class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        my_dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in my_dict.keys():
                j = my_dict[temp]
                return [j ,i]

            if nums[i] not in my_dict:
                my_dict[nums[i]] = i 


        # return False

            

             