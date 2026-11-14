class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while True:
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif target > nums[r]:
                return -1
            elif target < nums[l]:
                return -1
            elif r - l <= 1:
                break
            elif target < nums[r] and target > nums[l]:
                mid = (r + l) // 2
                if target >= nums[mid]:
                    l = mid
                if target < nums[mid]:
                    r = mid
            


        return -1

        
