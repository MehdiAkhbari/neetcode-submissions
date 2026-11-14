class Solution:
    def isValid(self, s: str) -> bool:

        left_chars = ["(", "[", "{"]
        right_chars = [")", "]", "}"]
        stack = []

        for i in s:
            if i in left_chars:
                stack.append(i)

            elif i in right_chars:
                pos = right_chars.index(i)

                if stack != [] and stack[len(stack)-1] == left_chars[pos]:
                    stack.pop()
                
                elif stack == [] or stack[len(stack)-1] != left_chars[pos]:
                    return False
                


        if stack == []:
            return True
        else:
            return False

        