class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # odd length pals:
        for i in range(len(s)):
            j = 0
            while (i - j >= 0) and (i + j < len(s)):
                if s[i-j] == s[i+j]:
                    count +=1
                    j += 1
                else:
                    break


        # even length pals:
        for i in range(len(s)):
            j = 0
            while (i - j >= 0) and (i + j + 1 < len(s)):
                if s[i - j] == s[i + j + 1]:
                    count +=1
                    j += 1
                else:
                    break

        return count

        