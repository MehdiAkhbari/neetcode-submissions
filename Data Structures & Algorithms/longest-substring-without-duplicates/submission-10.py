# Create a list of seen variables so far
# Start from l = 0 and r = 0
    # if s[r] is in not seen: update the length variable (sum), add 1 to r
    # if s[r] is in seen: add 1 to l until there is no repeat, also remove corresponding s[l]'s from seen
    # update ans if sum is greater than it
# repeat this loop until r reaches last character    


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



            
