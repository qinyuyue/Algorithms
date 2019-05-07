## Daily Temperatures 

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Algorithms:
        1. initialize an empty stack and an [0] list with same lenght of T.
        2. push (T[0],idx) to stack
        3. iterate T from index 1
            while latest item in stack < T[i]:
                pop latest, change the relative index of output to i - idx, push T[i] to stack
        4. return output
        """

        ## my first version, 31%
        # output = [0] * len(T)
        # if len(T) > 0:
        #     stack = [(T[0],0)]
        #     for i in range(1, len(T)):
        #         while stack and stack[-1][0] < T[i]:
        #             output[stack[-1][1]] = i - stack[-1][1]
        #             stack.pop()
        #         stack.append((T[i], i))
        # return output

        ## 71%
        output = [0] * len(T)
        if len(T) > 0:
            stack = [(T[0],0)]
            for i in range(1, len(T)):
                while stack and stack[-1][0] < T[i]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append((T[i], i))
        return output
