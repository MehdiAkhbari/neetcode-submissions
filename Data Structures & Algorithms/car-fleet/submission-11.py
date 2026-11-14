class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        # for p, s in pair:
        #     # print(p, s)
        #     while stack != [] & (p - stack[-1][1]) > 0 and ((stack[-1][0] - p) / (p - stack[-1][1])) < ((target - -stack[-1][0]) / stack[-1][1]):
                
        #         stack.pop()

        #     stack.append(p, s)

        for p, s in pair:
            stack.append([p, s])

            if  len(stack) >= 2  and (target - p) / s <= (target - stack[-2][0]) / stack[-2][1] :
                stack.pop()


        # print(stack)
        return len(stack)

