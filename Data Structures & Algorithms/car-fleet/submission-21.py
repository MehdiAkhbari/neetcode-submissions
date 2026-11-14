class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [(p, s) for p, s in zip(position, speed)]
        # pair.sort(reverse=True)
        # stack = []
        # for p, s in pair:
        #     stack.append([p, s])

        #     if  len(stack) >= 2  and (target - p) / s <= (target - stack[-2][0]) / stack[-2][1] :
        #         stack.pop()

        # return len(stack)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        stack.append(pair[0]) #[[position[0], speed[0]]]


        for i in range(1, len(pair)):
            stack.append(pair[i])
            if (target - stack[-1][0]) / stack[-1][1] <= (target - stack[-2][0]) / stack[-2][1]:
                stack.pop()
                print("poped")
        return len(stack)

        


