class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0 
        j = 0
        out = 0
        mydict = {}
        for j in range(len(s)):
            # print(s[i:j + 1])
            # print(i, j)
            mydict[s[j]] = mydict.get(s[j], 0) + 1
            # print(mydict)
            max_freq = max(mydict.values())
            # print(f"max_freq = {max_freq}")
            changes = j - i + 1 - max_freq
            # print(f"changes= {changes}")
            if changes <= k:
                 out = max(out, j - i + 1)
            
            else:
                mydict[s[i]] -= 1
                i += 1
                
            print(out)
            

        return out


            
