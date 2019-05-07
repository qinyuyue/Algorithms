## Valid parenthese

class Solution:
    def isValid(self, s: 'str') -> 'bool':
        """
        Algorithms:
        1. initialize an empty stack.
        2. initialize a dict to store parenthese.
        3. iterate each element in string:
            if it is left open, append to stack
            else: pop first out and compare, if not paired, retrun False
        4. if len of stack > 0: return False

        """
        ## first version 24%
        # dicts = {'{':'}', '[':']', '(':')'}
        # chars = list(s)
        # # print(chars)
        # stack = []
        # for i in chars:
        #     if i in {'{', '[', '('}:
        #         stack.append(i)
        #     else:
        #         if len(stack) > 0:
        #             left_open = stack.pop()
        #             if dicts[left_open] != i:
        #                 return False
        #         else:
        #             return False
        # if len(stack) > 0:
        #     return False
        # return True

        ## 89%
        dicts = {'{':'}', '[':']', '(':')'}
        chars = list(s)
        stack = []
        for i in chars:
            if i in {'{', '[', '('}:
                stack.append(i)
            elif len(stack) == 0 or dicts[stack.pop()] != i:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
