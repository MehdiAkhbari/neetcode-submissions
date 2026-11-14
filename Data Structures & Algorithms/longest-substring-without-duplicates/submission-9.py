class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        seen = set()
        

        while r < len(s):
            if s[r] not in seen:
                sum = r - l + 1
                seen.add(s[r])
                r += 1
                

            else:
                while s[r] in seen:
                    seen.discard(s[l])
                    l += 1
            
            if sum > ans:
                ans = sum
        return ans



            
