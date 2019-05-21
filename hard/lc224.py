## Basic Calculaor 
class Solution:
    def calculate(self, s: str) -> int:
        """
        Algorithm
        1. Init a stack for result and sign, result for result before parenthese, sign for positive or negative.
        2. Iterate string
            if digit, store to val num
            else, add num to result
                if +/-, change sign to 1/-1
                elif (, push result and sign to stack, initialize the two val.
                elif ), result = result * sign (pop first time) + prev_result(pop second time)
        3. Return result.
        """
        sign = 1
        result = 0
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            else:
                result += num * sign
                num = 0
                if c == '+':
                    sign = 1
                elif c == '-':
                    sign = -1
                elif c == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif c == ')':
                    result = result * stack.pop() + stack.pop()
            print(stack, result)
        result += num * sign
        return result
