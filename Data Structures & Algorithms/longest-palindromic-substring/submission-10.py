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
