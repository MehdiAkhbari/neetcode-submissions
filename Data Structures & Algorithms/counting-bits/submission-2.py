class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            res = 0
            for i in range(32):
                if (1 << i) & num :
                    res += 1

            ans.append(res)
        return ans
            