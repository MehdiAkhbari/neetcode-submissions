class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # out = digits
        i = len(digits) - 1
        while True:
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                i -= 1 
            
            if i == -1:
                digits = [1] + digits
                break

        return digits

                
        