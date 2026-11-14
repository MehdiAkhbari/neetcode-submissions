class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        for i in s1:
            s1dict[i] = s1dict.get(i, 0) + 1

        s2dict = {}
        for i in s2[0 : len(s1)]:
            s2dict[i] = s2dict.get(i, 0) + 1
        if s2dict == s1dict:
                return True

        for i in range(1, len(s2)- len(s1) + 1):

            j = i + len(s1) - 1
            # remove s2[i] from dict and add s2[j] to it
            s2dict[s2[i-1]] = s2dict.get(s2[i-1], 1) - 1
            if s2dict[s2[i-1]] == 0:
                s2dict.pop(s2[i-1])
            s2dict[s2[j]] = s2dict.get(s2[j], 0) + 1
            print(s2dict)
            if s2dict == s1dict:
                return True            
        return False


            








