## Basic calculator II
## key: stack, pattern recognition 

class Solution:
    def calculate(self, s: str) -> int:
        """
        Algorithms:
        1. initialize a stack
        2. while loop, iterate list
            if *, pop stack, multiple and push to stack
            elif /, pop stack, divide and push
            elif -, push -num to stack
        """

        stack = []
        sign = '+'
        num = ''
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                # stack.append(curr_num)
                # curr_num = ''
                num = int(num)
                print(num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                elif sign == '-':
                    stack.append(-num)
                else:
                    stack.append(num)
                sign = s[i]
                num = ''
        return sum(stack)
