# Solve it recursively:
# for each i: there are two cases of decoding: 1. last digit (digit i) is used as a single digit 2. it is used a the second digit 
# for case 1: the number of such cases are f(n-1) * (s[i] != 0), if s[i] is 0, there are 0 cases
# for case 2: the number of cases are f(n-2) when last two digits (s[i-1:i+1]) are between 10 and 26, and zero otherwise: f(n-2) * [10 <= (s[i-1:i+1]) <= 26]
# the answer is the sum of these two numbers
# if first char is 0, there are no cases
# boundary conditions lead to initial answers being [1, 1] ex: if s="22", we should get ans = ans[0] + ans[1] = 2, also ans[1] = 1, so ans[0] has to be 1

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0


        ans = [1, 1]

        for i in range(1, len(s)):
            num = int(s[i - 1 : i + 1])
            temp = int(num > 9 and num<= 26)
            ans.append(ans[-1] * (s[i] != '0') + ans[-2] * temp)
        print(ans)
        return ans[-1]
        
