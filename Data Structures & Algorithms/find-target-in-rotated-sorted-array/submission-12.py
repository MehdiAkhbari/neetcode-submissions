# idea: each such array consists of a maximum of two increasing sub-arrays. We can find these two sub-arrays, and the do binary search in each of them to see if the answer is in any of them.
# initial goal: find the beginning of the last sub-array (smallest element), say index k. then define subarrays as [0:k], [k:-1]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                break


        k = l
        print(k)
                
        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, k)
        if result != -1:
            return result
        else:
            return binary_search(k, len(nums) -1)

        