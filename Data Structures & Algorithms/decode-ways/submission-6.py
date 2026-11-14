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
        

        # single = [0, 1]
        # double = [0, 0]

        # for i in range(1, len(s)):
        #     num = int(s[i - 1 : i + 1])
        #     temp = int(num > 9 and num<= 26)
        #     single.append((single[-1] + double[-1]) * int(s[i] != '0'))
        #     double.append(single[-3] + temp)
        # print(single , double)
        # return single[-1] + double[-1]
