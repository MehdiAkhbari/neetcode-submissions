# a shifted ascending list has two sections (at most): 1. First, an ascending section 2. then a descending section
# the minimum element is the beginning of the descending section
# when an element is smaller than an element with a higher index, it means that the minimum is between those numbers
#, to find it using bisection:
# start with l = 0 and r = len(nums) - 1 
    # if nums[l] < nums[r]: we are in the increasing section, so nums[l] is the answer
    # if nums[l] > nums[r]: the minimum is between l and r, so do bisection: mid = (r+l)// 2, 
            # if nums[l] > nums[mid]: the answer is between l and mid, so r = mid 
            # if nums[r] < nums[mid]: the answer is between mid+1 and r, so l = mid + 1  
            # repeat until l = r


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] > nums[r]:
                if nums[l] > nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                 return nums[l]

        return nums[l]


        