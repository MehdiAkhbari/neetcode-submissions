class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num_1 = 0
        for i in range(len(num1)):
            num_1 = num_1 * 10 + int(num1[i])
        print(num_1)

        num_2 = 0
        for i in range(len(num2)):
            num_2 = num_2 * 10 + int(num2[i])
        print(num_2)
        
        return str(num_1 * num_2)
