# Idea: start from i=j=0, count number of characters needed to be changed to get a pure string in s[i: j+1],this would be: j - i + 1 - max_freq 
# if this number is less than k, j+=1
# else: i += 1 AND j += 1 (this is important, otherwise the length of the answer goes down, which is unnecessary, we spend more time checking useless cases)
# update the hash map on the fly  

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0 
        j = 0
        out = 0
        mydict = {}
        for j in range(len(s)):
            mydict[s[j]] = mydict.get(s[j], 0) + 1
            max_freq = max(mydict.values())
            changes = j - i + 1 - max_freq
            if changes <= k:
                 out = max(out, j - i + 1)
            else:
                mydict[s[i]] -= 1
                i += 1
                
            print(out)
            

        return out


            
