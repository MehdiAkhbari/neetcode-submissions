def drop_char_i(s:str, i: int):
    if len(s) <= 1:
        return ""
    elif i==0:
        return s[1:]
    else:
        return s[0:i] + s[i+1:]


class Solution:



    def isAnagram(self, s: str, t: str) -> bool:
        pass
        s_temp = s
        t_temp = t
        count = 0
        if len(s) != len(t):
            return False
        else:
            while len(s_temp) > 0:
                print(1)
                for j in range(len(t_temp)):
                    # print(j)
                    # print(t_temp)
                    if s_temp[0] == t_temp[j]:
                        s_temp = drop_char_i(s_temp, 0)
                        t_temp = drop_char_i(t_temp, j)
                        # print(s_temp)
                        # print(t_temp)
                        count += 1
                        break
                    elif j == len(t_temp)-1:
                        return False

        if count == len(s):
            return True
        else:
            return False


        