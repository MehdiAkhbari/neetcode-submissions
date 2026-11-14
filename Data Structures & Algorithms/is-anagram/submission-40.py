class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for x in s:
            if x in s_dict:
                s_dict[x] += 1
            else:
                s_dict[x] = 1
        
        print(s_dict)


        t_dict = {}
        for x in t:
            if x in t_dict:
                t_dict[x] += 1
            else:
                t_dict[x] = 1  


        return s_dict == t_dict       
