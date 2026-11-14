# Idea: for each character in string, find the longest palindrome in which that character is the middle element
# if palindrome has an odd length: for i'th char, iteratively check if s[i-j] and s[i+j] are equal for i = 1, 2, ... and increase j if equality holds
 # if palindrome has an even length: for i'th char, iteratively check if s[i-j] and s[i+j+1] are equal for i = 0, 1, ... and increase j if equality holds
# store the longest palindrome in ans and update it as required

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd length palindrome
        ans = s[0]
        for i, x in enumerate(s):
            j = 1
            current = x
            while (i-j >= 0) and (i+j < len(s)):
                if s[i - j] == s[i + j]:
                    current = s[i - j : i + j + 1]
                    j += 1
                    if len(current) > len(ans):
                        ans = current
                else:
                    break
            # print(ans, i)
            
        # even length palindrome
        for i, x in enumerate(s):
            j = 0
            current = ""
            while (i + j + 2 <= len(s)) and (i - j >= 0):
                if s[i- j] == s[i + j + 1]:
                    current = s[i - j: i + j + 2]
                    j +=1
                    if len(current) > len(ans):
                        ans = current
                else:
                    break
            # print(ans, i)

        return ans
