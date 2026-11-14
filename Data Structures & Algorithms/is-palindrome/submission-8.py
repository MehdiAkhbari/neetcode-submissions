class Solution:
    def isPalindrome(self, s: str) -> bool:
        count = 0
        chars = 0
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l].isalnum() == False:
                l += 1
            if s[r].isalnum() == False:
                r -= 1
            elif s[l].isalnum() == True and s[r].isalnum() == True:
                s_l = s[l].lower()
                s_r = s[r].lower()
                chars += 2
                if s_l == s_r:
                    count += 2

                l += 1
                r -= 1
                

        print(count)
        print(chars)
        return count == chars




        