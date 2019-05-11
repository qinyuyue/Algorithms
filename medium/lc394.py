## Decode string

"""
        Algorithm:
        1. initialize two stack store number and char, two variable store the deepest string in square bracket and the associate number
        2. for i in str, if it is digit or alpha, add to string
            if meet '[', add number and string to the stack separately.
            if meet ']', current string += current string * n_stack.pop()
        """
        output = ''
        num_stack = []
        char_stack = []
        curr_num = ''
        curr_char = ''
        for c in s:
            if c.isalpha():
                curr_char += c
            elif c.isdigit():
                curr_num += c
            elif c == '[':
                char_stack.append(curr_char)
                num_stack.append(int(curr_num))
                curr_char = ''
                curr_num = ''
            elif c == ']':
                # output.append(curr_char * num_stack.pop())
                curr_char = char_stack.pop() + curr_char * num_stack.pop()
            output = curr_char

        return output
                
