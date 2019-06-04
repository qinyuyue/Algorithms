## Reserve words in a string II

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        much faster than second one algo
        '''
        lst = s.split()
        lst = [i[::-1] for i in lst]
        return ' '.join(lst)

        # lst = s.split()
        # for n in range(len(lst)):
        #     new = list(lst[n])
        #     i = 0
        #     j = len(lst[n])-1
        #     while i < j :
        #         new[i], new[j] = new[j], new[i]
        #         i += 1
        #         j -= 1
        #     # print(new)
        #     lst[n] = ''.join(new)
        #     # print(n)
        # return ' '.join(lst)
