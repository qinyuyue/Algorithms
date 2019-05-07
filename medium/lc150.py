## Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Algorithm:
        1. initialize a new stack.
        2. iterate each item in tokens:
            push it to stack unitl it is the first operator:
            if operator is * :
                pop twice and multiple
            if operator is + :
                pop twice and add
            if operatio is / :
                reciprocal first pop, mutliple with second pop
            push the result above back to stack
        3. return last pop item
        """
        # first version, 85%

        stack = []
        operator = {'*', '+', '/', '-'}
        for i in tokens:
            # print(stack)
            if i not in operator:
                # print(int(i))
                stack.append(int(i))
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack.pop()
